# PBF-LB/M Submodel Parameter Reference

This document provides detailed descriptions for each property and collection defined in `am_machine.py`. Use these descriptions to customize or extend the generated Asset Administration Shell (AAS) submodel.

---

## Info Collection
General information about the additive manufacturing machine.

| Property | Type | Unit | Description |
| -------- | ---- | ---- | ----------- |
| `manufacturer_brand` | String | – | Name of the AM machine manufacturer (e.g., SLM, TRUMPF, EOS). |
| `model_type` | String | – | Type of machine indicating whether it processes metal or polymer. |
| `model_number` | String | – | Product model number of the machine. |
| `model_number_technical` | String | – | Technical designation of the machine model. |
| `serial_number` | String | – | Unique serial number assigned to the machine. |
| `host_name` | String | – | Network hostname used for machine connectivity. |
| `feed_model` | String | – | Variant of the material feed system. |
| `feedstock_equipped` | String | – | Type of material currently loaded. |
| `remote_control` | Boolean | – | `True` if remote operation is enabled. |
| `exposure_unit_count` | Integer | – | Number of exposure units such as laser sources. |
| `build_volume` | Collection | – | Nested collection describing the build space. |

### Build Volume (Nested Collection)

| Property | Type | Unit | Description |
| -------- | ---- | ---- | ----------- |
| `type` | String | – | Specifies whether the build volume is rectangular or cylindrical. |
| `x_dimension` | Double | mm | Build plate width (X‑axis). |
| `y_dimension` | Double | mm | Build plate depth (Y‑axis). |
| `z_dimension` | Double | mm | Maximum build height (Z‑axis). |
| `diameter` | Double | mm | Diameter if the build volume is cylindrical. |

## Exposure Unit Collection
Specifications of the laser and galvanometer system.

| Property | Type | Unit | Description |
| -------- | ---- | ---- | ----------- |
| `galvo_scan_head_model` | String | – | Model of the galvanometer-based scanning head. |
| `galvo_scan_head_interface` | String | – | Interface type used to control the scan head. |
| `galvo_scan_head_software` | String | – | Software or firmware version for the scan head. |
| `laser_source_model` | String | – | Model identifier of the laser source. |
| `laser_source_serial_number` | String | – | Serial number of the laser source. |
| `laser_source_software` | String | – | Firmware or software version of the laser. |
| `laser_source_rated_power` | Double | W | Maximum rated power output of the laser source. |
| `laser_powers` | Double | W | Available laser power settings. |
| `laser_mode` | String | – | Operating mode of the laser (continuous, pulsed, etc.). |
| `laser_configuration` | String | – | Configurable laser power settings. |
| `beam_focus_diameter_min` | Double | µm | Minimum focusable laser beam diameter. |
| `beam_focus_diameter_max` | Double | µm | Maximum focusable laser beam diameter. |

## Atmosphere Collection
Gas handling and filtration system specifications.

| Property | Type | Unit | Description |
| -------- | ---- | ---- | ----------- |
| `filtration_model` | String | – | Model of the filtration system used. |
| `filtration_serial_number` | String | – | Serial number of the filtration unit. |
| `filtration_safety_software` | String | – | Safety software version controlling the filtration. |
| `filtration_software` | String | – | Filtration unit software version. |
| `inert_gas_equipped` | String | – | Type of shielding gas used in the build chamber. |

## PLC Collection
Programmable Logic Controller specifications.

| Property | Type | Unit | Description |
| -------- | ---- | ---- | ----------- |
| `model` | String | – | PLC model or type. |
| `serial_number` | String | – | Serial number of the PLC unit. |
| `software_version` | String | – | Version of the PLC software. |

## MCSW Collection
Machine Control Software specifications.

| Property | Type | Unit | Description |
| -------- | ---- | ---- | ----------- |
| `print_domain` | String | – | Domain configuration for the printing process. |
| `control_system` | String | – | Supervisory control system of the machine. |
| `scada_system` | String | – | Version of the SCADA software used. |
| `db_scheme` | String | – | Database schema version. |
| `db_service` | String | – | Database service version used by the machine. |
| `hcs_service` | String | – | Hardware control system service version. |

---

### Example JSON Output
An example submodel JSON file can be generated using:

```bash
python am_machine.py --pretty -o example_submodel.json
```

A truncated excerpt is shown below:

```json
$(head -c 200 example_submodel.json)
```

The full file `example_submodel.json` will contain all collections and properties in accordance with the tables above.

