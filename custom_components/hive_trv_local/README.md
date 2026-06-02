# Hive TRV Local v3

Advanced group management for Hive/Danfoss TRVs in Home Assistant.

Built on [climate_group_helper](https://github.com/bjrnptrsn/climate_group_helper) by bjrnptrsn (MIT licence), extended with Hive-specific features.

## What v3 adds over climate_group_helper

| Feature | Description |
|---|---|
| **Hive/Danfoss TRV filter** | Entity picker shows only Hive/Danfoss Z2M TRV models |
| **Boiler demand** | Turns boiler/receiver on/off based on aggregate group heat demand |
| **Hive TRV Card** | Bundled Lovelace card — auto-registered, no manual resource setup |
| **Hive calibration defaults** | Offset mode for Hive TRVs, Scaled (x100) for Danfoss Ally |

## Full feature set (from climate_group_helper)

- **Unified control** — change group, all members update
- **Smart averaging** — mean/median/min/max of member temperatures
- **Master entity** — designate one TRV as group leader
- **External sensors** — use room sensors for accurate calibration
- **Device calibration** — write values back to TRV offset/external sensor
- **Sync modes** — Mirror, Lock, Master-Lock
- **Window control** — binary sensor integration with configurable delays
- **Member offsets** — per-TRV temperature offset (±20°C)
- **Member isolation** — isolate specific TRVs by sensor, HVAC mode, or manual off
- **Schedule automation** — HA schedule helper integration with boost, override duration
- **Boost service** — timed boost with absolute or relative temperature

## Installation

**HACS → Integrations → Custom repositories**
```
https://github.com/gashwell/Hive-TRV-Local-v3    category: Integration
```

## Setup

**Settings → Devices & Services → Helpers → + Create Helper → Hive TRV Group**

Select your Hive/Danfoss Z2M TRV climate entities. Configure boiler entity in the next step.

## Attribution

Core group engine: [climate_group_helper](https://github.com/bjrnptrsn/climate_group_helper) by bjrnptrsn, MIT licence.
