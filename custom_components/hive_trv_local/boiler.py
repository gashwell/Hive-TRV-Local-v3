"""Boiler demand manager for Hive TRV Local v3.

Watches hvac_action across all group climate entities created by this
integration. Turns the boiler/receiver on when any group is heating,
off when none are.
"""
from __future__ import annotations

import logging
from collections.abc import Callable
from typing import Any

from homeassistant.const import ATTR_ENTITY_ID, STATE_ON
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.event import async_track_state_change_event

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class BoilerDemandManager:
    """Drives a boiler/receiver entity based on aggregate heat demand."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry_id: str,
        boiler_entity: str | None,
    ) -> None:
        self._hass         = hass
        self._entry_id     = entry_id
        self._boiler       = boiler_entity
        self._demand       = False
        self._unsubscribers: list[Callable] = []

    async def async_setup(self) -> None:
        """Subscribe to state changes of all group climate entities."""
        self._subscribe()

    def update_boiler_entity(self, entity_id: str | None) -> None:
        self._boiler = entity_id

    def _group_entity_ids(self) -> list[str]:
        """Get all climate entity IDs created by our integration."""
        from homeassistant.helpers import entity_registry as er
        try:
            reg = er.async_get(self._hass)
            return [
                e.entity_id for e in reg.entities.values()
                if e.platform == DOMAIN and e.entity_id.startswith("climate.")
            ]
        except Exception:
            return []

    def _subscribe(self) -> None:
        for unsub in self._unsubscribers:
            unsub()
        self._unsubscribers.clear()
        eids = self._group_entity_ids()
        if eids:
            self._unsubscribers.append(
                async_track_state_change_event(
                    self._hass, eids, self._on_state_change
                )
            )

    def unsubscribe(self) -> None:
        for unsub in self._unsubscribers:
            unsub()
        self._unsubscribers.clear()

    @property
    def any_heat_required(self) -> bool:
        from homeassistant.components.climate import HVACAction
        for eid in self._group_entity_ids():
            state = self._hass.states.get(eid)
            if state and state.attributes.get("hvac_action") == HVACAction.HEATING:
                return True
        return False

    async def async_evaluate(self) -> None:
        if not self._boiler:
            return
        needed = self.any_heat_required
        if needed == self._demand:
            return
        self._demand = needed
        domain  = self._boiler.split(".")[0]
        service = "turn_on" if needed else "turn_off"
        try:
            await self._hass.services.async_call(
                domain, service,
                {ATTR_ENTITY_ID: self._boiler},
                blocking=False,
            )
            _LOGGER.debug("Boiler → %s (%s)", "ON" if needed else "OFF", self._boiler)
        except Exception as exc:
            _LOGGER.warning("Boiler service call failed: %s", exc)

    @callback
    def _on_state_change(self, _event: Any) -> None:
        self._hass.async_create_task(self.async_evaluate())
