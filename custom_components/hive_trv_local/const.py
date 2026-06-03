"""Constants for Hive TRV Local v3.

Based on climate_group_helper by bjrnptrsn (MIT).
Extended with Hive/Danfoss-specific features.
"""
# ── Re-export everything from the base implementation ─────────────────────────
# All climate_group_helper constants remain valid — we extend them below.

from __future__ import annotations

DOMAIN       = "hive_trv_local"
DEFAULT_NAME = "Hive TRV Group"

# ── Climate Group Helper base constants ───────────────────────────────────────
CONF_ADVANCED_MODE              = "advanced_mode"
CONF_MASTER_ENTITY              = "master_entity"
CONF_HVAC_MODE_STRATEGY         = "hvac_mode_strategy"
CONF_FEATURE_STRATEGY           = "feature_strategy"
CONF_UNION_OUT_OF_BOUNDS_ACTION = "union_out_of_bounds_action"
CONF_UNION_UNSUPPORTED_HVAC_ACTION = "union_unsupported_hvac_action"
CONF_TEMP_TARGET_AVG            = "temp_target_avg"
CONF_TEMP_TARGET_ROUND          = "temp_target_round"
CONF_TEMP_CURRENT_AVG           = "temp_current_avg"
CONF_TEMP_USE_MASTER            = "temp_use_master"
CONF_TEMP_SENSORS               = "temp_sensors"
CONF_TEMP_UPDATE_TARGETS        = "temp_update_targets"
CONF_TEMP_CALIBRATION_MODE      = "temp_calibration_mode"
CONF_CALIBRATION_HEARTBEAT      = "calibration_heartbeat"
CONF_CALIBRATION_IGNORE_OFF     = "calibration_ignore_off"
CONF_STAGGERED_CALL_DELAY       = "staggered_call_delay"
CONF_HUMIDITY_TARGET_AVG        = "humidity_target_avg"
CONF_HUMIDITY_TARGET_ROUND      = "humidity_target_round"
CONF_HUMIDITY_CURRENT_AVG       = "humidity_current_avg"
CONF_HUMIDITY_USE_MASTER        = "humidity_use_master"
CONF_HUMIDITY_SENSORS           = "humidity_sensors"
CONF_HUMIDITY_UPDATE_TARGETS    = "humidity_update_targets"
CONF_SYNC_MODE                  = "sync_mode"
CONF_SYNC_ATTRS                 = "sync_attributes"
CONF_IGNORE_OFF_MEMBERS_SYNC    = "ignore_off_members_sync"
CONF_WINDOW_MODE                = "window_mode"
CONF_WINDOW_ADOPT_MANUAL_CHANGES = "window_adopt_manual_changes"
CONF_WINDOW_ACTION              = "window_action"
CONF_WINDOW_TEMPERATURE         = "window_temperature"
CONF_ROOM_SENSOR                = "room_sensor"
CONF_ZONE_SENSOR                = "zone_sensor"
CONF_ROOM_OPEN_DELAY            = "room_open_delay"
CONF_ZONE_OPEN_DELAY            = "zone_open_delay"
CONF_CLOSE_DELAY                = "close_delay"
DEFAULT_ROOM_OPEN_DELAY         = 15
DEFAULT_ZONE_OPEN_DELAY         = 300
DEFAULT_CLOSE_DELAY             = 30
CONF_PRESENCE_MODE              = "presence_mode"
CONF_PRESENCE_SENSOR            = "presence_sensor"
CONF_PRESENCE_ZONE              = "presence_zone"
CONF_PRESENCE_ACTION            = "presence_action"
CONF_PRESENCE_AWAY_OFFSET       = "presence_away_offset"
CONF_PRESENCE_AWAY_TEMPERATURE  = "presence_away_temperature"
CONF_PRESENCE_AWAY_PRESET       = "presence_away_preset"
CONF_PRESENCE_AWAY_DELAY        = "presence_away_delay"
CONF_PRESENCE_RETURN_DELAY      = "presence_return_delay"
DEFAULT_PRESENCE_AWAY_DELAY     = 0
DEFAULT_PRESENCE_RETURN_DELAY   = 0
CONF_MEMBER_TEMP_OFFSETS        = "member_temp_offsets"
CONF_MEMBER_OFFSET_CORRECTION   = "member_offset_correction"
CONF_ISOLATION_SENSOR           = "isolation_sensor"
CONF_ISOLATION_ENTITIES         = "isolation_entities"
CONF_ISOLATION_ACTIVATE_DELAY   = "isolation_activate_delay"
CONF_ISOLATION_RESTORE_DELAY    = "isolation_restore_delay"
CONF_ISOLATION_TRIGGER          = "isolation_trigger"
CONF_ISOLATION_TRIGGER_HVAC_MODES = "isolation_trigger_hvac_modes"
CONF_SCHEDULE_ENTITY            = "schedule_entity"
CONF_SCHEDULE_BYPASS_ENTITY     = "schedule_bypass_entity"
CONF_RESYNC_INTERVAL            = "resync_interval"
CONF_OVERRIDE_DURATION          = "override_duration"
CONF_PERSIST_CHANGES            = "persist_changes"
CONF_PERSIST_ACTIVE_SCHEDULE    = "persist_active_schedule"
CONF_IGNORE_OFF_MEMBERS_SCHEDULE = "ignore_off_members_schedule"
CONF_IGNORE_OFF_MEMBERS_TEMPERATURE = "ignore_off_members_temperature"
CONF_DEBOUNCE_DELAY             = "debounce_delay"
CONF_RETRY_ATTEMPTS             = "retry_attempts"
CONF_RETRY_DELAY                = "retry_delay"
CONF_GRACE_PERIOD               = "grace_period"
DEFAULT_GRACE_PERIOD            = 3.0
CONF_MIN_TEMP_OFF               = "min_temp_off"
CONF_EXPOSE_SMART_SENSORS       = "expose_smart_sensors"
CONF_EXPOSE_MEMBER_ENTITIES     = "expose_member_entities"
CONF_EXPOSE_CONFIG              = "expose_config"
CONF_RANGE_TEMPLATE_ENTITIES    = "range_template_entities"
CONF_RANGE_TEMPLATE_DEADBAND_ACTION = "range_template_deadband_action"
CONF_EXPAND_SECTIONS            = "expand_sections"

# Strategy values
AUTO         = "auto"
NORMAL       = "normal"
OFF_PRIORITY = "off_priority"
INTERSECTION = "intersection"
UNION        = "union"
OFF          = "off"
CLAMP        = "clamp"
IGNORE       = "ignore"
MEAN         = "mean"
MEDIAN       = "median"
MIN          = "min"
MAX          = "max"
NONE         = "none"
HALF         = "half"
INTEGER      = "integer"
ABSOLUTE     = "absolute"
OFFSET_MODE  = "offset"
SCALED       = "scaled"
DISABLED     = "disabled"
LOCK         = "lock"
MIRROR       = "mirror"
MASTER_LOCK  = "master_lock"
MIRROR_LOCK  = "mirror_lock"
ENABLED      = "enabled"
ALL          = "all"
MASTER_ONLY  = "master_only"
TEMPERATURE  = "temperature"
FAN_ONLY     = "fan_only"
AWAY_OFFSET  = "away_offset"
AWAY_TEMPERATURE = "away_temperature"
AWAY_PRESET  = "away_preset"
SENSOR       = "sensor"
HVAC_MODE    = "hvac_mode"
MEMBER_OFF   = "member_off"

# Services
SERVICE_SET_SCHEDULE_ENTITY        = "set_schedule_entity"
SERVICE_SET_SCHEDULE_BYPASS_ENTITY = "set_schedule_bypass_entity"
SERVICE_BOOST                      = "boost"
SERVICE_APPLY_CONFIG               = "apply_config"

# Attributes
ATTR_SCHEDULE_ENTITY               = "schedule_entity"
ATTR_SCHEDULE_BYPASS_ENTITY        = "schedule_bypass_entity"
ATTR_SETTINGS                      = "settings"
ATTR_INCLUDE_MEMBER_LIST           = "include_member_list"
ATTR_INCLUDE_ENTITY_SELECTORS      = "include_entity_selectors"
ATTR_ACTIVE_OVERRIDE               = "active_override"
ATTR_ACTIVE_OVERRIDE_END           = "active_override_end"
ATTR_ACTIVE_SCHEDULE_BYPASS_ENTITY = "active_schedule_bypass_entity"
ATTR_ACTIVE_SCHEDULE_ENTITY        = "active_schedule_entity"
ATTR_ACTIVE_SCHEDULE_SLOT_TITLE    = "active_schedule_slot_title"
ATTR_ASSUMED_STATE                 = "assumed_state"
ATTR_BLOCKING_SOURCES              = "blocking_sources"
ATTR_CONFIG_OVERRIDES              = "config_overrides"
ATTR_CURRENT_HVAC_MODES            = "current_hvac_modes"
ATTR_GROUP_OFFSET                  = "group_offset"
ATTR_ISOLATED_MEMBERS              = "isolated_members"
ATTR_LAST_ACTIVE_HVAC_MODE         = "last_active_hvac_mode"
ATTR_MASTER_FALLBACK_ACTIVE        = "master_fallback_active"
ATTR_OOB_MEMBERS                   = "oob_members"
ATTR_SETTINGS_JSON                 = "settings_json"
ATTR_ENABLED_FEATURES              = "enabled_features"
ATTR_LAST_SOURCE                   = "last_source"
ATTR_LAST_CHANGED                  = "last_changed"
ATTR_LAST_ENTITY                   = "last_entity"
ATTR_ACTIVE_MEMBER_COUNT           = "active_member_count"
ATTR_TOTAL_MEMBER_COUNT            = "total_member_count"
ATTR_PRESENCE_FALLBACK             = "presence_fallback"
ATTR_EFFECTIVE_SYNC_MODE           = "effective_sync_mode"
ATTR_EFFECTIVE_SYNC_ATTRIBUTES     = "effective_sync_attributes"

# Key sets (required by meta_processor, state, etc.)
from homeassistant.const import CONF_ENTITIES, CONF_NAME

IDENTITY_KEYS: frozenset = frozenset({CONF_NAME})
MEMBER_LIST_KEYS: frozenset = frozenset({CONF_ENTITIES, CONF_TEMP_SENSORS,
    CONF_HUMIDITY_SENSORS, CONF_TEMP_UPDATE_TARGETS, CONF_ISOLATION_ENTITIES,
    CONF_RANGE_TEMPLATE_ENTITIES})
ENTITY_SELECTOR_KEYS: frozenset = frozenset({
    CONF_MASTER_ENTITY, CONF_ROOM_SENSOR, CONF_ZONE_SENSOR,
    CONF_SCHEDULE_ENTITY, CONF_SCHEDULE_BYPASS_ENTITY,
    CONF_PRESENCE_SENSOR, CONF_ISOLATION_SENSOR, CONF_PRESENCE_ZONE})

META_KEY_TURN_OFF    = "turn_off"
META_KEY_SYNC_MODE   = CONF_SYNC_MODE
META_KEY_GROUP_OFFSET = ATTR_GROUP_OFFSET
META_KEY_SYNC_ATTRS  = CONF_SYNC_ATTRS
META_STATE_KEYS: frozenset = frozenset({
    META_KEY_TURN_OFF, META_KEY_SYNC_MODE, META_KEY_GROUP_OFFSET, META_KEY_SYNC_ATTRS})

from homeassistant.components.climate import (
    ATTR_FAN_MODE, ATTR_HUMIDITY, ATTR_HVAC_MODE, ATTR_PRESET_MODE,
    ATTR_SWING_MODE, ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW,
)
from homeassistant.const import ATTR_TEMPERATURE

ATTR_SERVICE_MAP = {
    ATTR_HVAC_MODE:        "set_hvac_mode",
    ATTR_TEMPERATURE:      "set_temperature",
    ATTR_TARGET_TEMP_HIGH: "set_temperature",
    ATTR_TARGET_TEMP_LOW:  "set_temperature",
    ATTR_PRESET_MODE:      "set_preset_mode",
    ATTR_FAN_MODE:         "set_fan_mode",
    ATTR_SWING_MODE:       "set_swing_mode",
    ATTR_HUMIDITY:         "set_humidity",
}
MODE_MODES_MAP = {
    "set_hvac_mode":    ATTR_HVAC_MODE,
    "set_temperature":  ATTR_TEMPERATURE,
    "set_preset_mode":  ATTR_PRESET_MODE,
    "set_fan_mode":     ATTR_FAN_MODE,
    "set_swing_mode":   ATTR_SWING_MODE,
    "set_humidity":     ATTR_HUMIDITY,
}
SYNC_TARGET_ATTRS = list(ATTR_SERVICE_MAP.keys())
FLOAT_TOLERANCE    = 0.05
STARTUP_BLOCK_DELAY = 5.0

# ── Hive TRV Local v3 additions ────────────────────────────────────────────────

# Boiler demand
CONF_BOILER_ENTITY      = "boiler_entity"
CONF_ENABLE_DIAGNOSTICS = "enable_diagnostics"

# Hive/Danfoss TRV model strings for Z2M entity filtering
HIVE_DANFOSS_MODELS: frozenset = frozenset({
    "UK7004240",    # Hive Radiator Valve
    "TRV001",       # Hive Radiator Valve (alt)
    "SLT510",       # Hive Thermostat Mini
    "SLT6",         # Hive Thermostat
    "STHTR001",     # Hive Smart Thermostat
    "eTRV0100",     # Danfoss Ally
    "eTRV0103",     # Danfoss Ally
    "eTRV0111",     # Danfoss Ally
    "014G2461",     # Danfoss Icon
    "SORB",         # Danfoss Icon
    "POPP-009501",  # Popp POPZ701721
})

# Hive/Danfoss calibration defaults
# Danfoss uses external_measured_room_sensor (x100 = SCALED mode)
# Hive uses regulation_setpoint_offset (OFFSET mode)
HIVE_DEFAULT_CALIBRATION_MODE = OFFSET_MODE
DANFOSS_DEFAULT_CALIBRATION_MODE = SCALED

# Hive-specific Z2M attribute names
HIVE_ATTR_EXTERNAL_SENSOR  = "external_measured_room_sensor"
HIVE_ATTR_ORIENTATION      = "thermostat_orientation"
HIVE_ATTR_WINDOW_OPEN      = "window_open_external"
HIVE_ATTR_HEAT_REQUIRED    = "heat_required"
HIVE_ATTR_PI_DEMAND        = "pi_heating_demand"
HIVE_ATTR_ADAPTATION_RUN   = "adaptation_run_control"


# ── StrEnum classes (required by config_flow, climate, sync_mode etc.) ────────
from enum import StrEnum


class HvacModeStrategy(StrEnum):
    """HVAC mode aggregation strategy."""
    AUTO         = "auto"
    NORMAL       = "normal"
    OFF_PRIORITY = "off_priority"


class FeatureStrategy(StrEnum):
    """Feature aggregation strategy."""
    INTERSECTION = "intersection"
    UNION        = "union"


class UnionOutOfBoundsAction(StrEnum):
    """Out-of-bounds action when union strategy is active."""
    OFF   = "off"
    CLAMP = "clamp"


class UnsupportedHvacAction(StrEnum):
    """How to handle members that do not support the active HVAC mode."""
    IGNORE = "ignore"
    OFF    = "off"


class AverageOption(StrEnum):
    """Averaging options for temperature."""
    MEAN   = "mean"
    MEDIAN = "median"
    MIN    = "min"
    MAX    = "max"


class RoundOption(StrEnum):
    """Rounding options for temperature."""
    NONE    = "none"
    HALF    = "half"
    INTEGER = "integer"


class CalibrationMode(StrEnum):
    """Calibration modes for external sensors."""
    ABSOLUTE = "absolute"
    OFFSET   = "offset"
    SCALED   = "scaled"


class SyncMode(StrEnum):
    """Sync mode options."""
    DISABLED    = "disabled"
    LOCK        = "lock"
    MIRROR      = "mirror"
    MASTER_LOCK = "master_lock"
    MIRROR_LOCK = "mirror_lock"


class WindowControlMode(StrEnum):
    """Window control enable/disable."""
    DISABLED = "disabled"
    ENABLED  = "enabled"


class AdoptManualChanges(StrEnum):
    """Adopt manual changes options for window control."""
    OFF         = "off"
    ALL         = "all"
    MASTER_ONLY = "master_only"


class WindowControlAction(StrEnum):
    """Window control actions."""
    OFF         = "off"
    TEMPERATURE = "temperature"


class RangeTemplateDeadbandAction(StrEnum):
    """Physical action when a range-template member is inside the deadband."""
    OFF      = "off"
    FAN_ONLY = "fan_only"


class PresenceMode(StrEnum):
    """Presence control modes."""
    DISABLED = "disabled"
    ENABLED  = "enabled"


class PresenceAction(StrEnum):
    """Presence control actions."""
    OFF              = "off"
    AWAY_OFFSET      = "away_offset"
    AWAY_TEMPERATURE = "away_temperature"
    AWAY_PRESET      = "away_preset"


class IsolationTrigger(StrEnum):
    """Isolation trigger modes."""
    DISABLED  = "disabled"
    SENSOR    = "sensor"
    HVAC_MODE = "hvac_mode"
    MEMBER_OFF = "member_off"
