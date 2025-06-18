import argparse
import json

from basyx.aas import model, adapter
from basyx.aas.adapter import json as aas_json


def _flatten_parameters(params: dict) -> dict:
    """Recursively extract parameter datatypes from the structured dictionary."""
    result = {}
    for key, value in params.items():
        if isinstance(value, dict):
            if "type" in value and not isinstance(value["type"], dict):
                result[key] = value["type"]
            result.update(_flatten_parameters(value))
    return result

# Improved structured dictionary for PBF-LB/M machine parameters aligned with Eclipse BaSyx SDK
machine_parameters_basic = {
    "Info": {
        "manufacturer_brand": {"type": model.datatypes.String, "unit": None, "description": "Name of the AM machine manufacturer (e.g., SLM, TRUMPF, EOS)"},
        "model_type": {"type": model.datatypes.String, "unit": None, "description": "Type of machine, specifying whether it's for metal or polymer"},
        "model_number": {"type": model.datatypes.String, "unit": None, "description": "Product model number of the machine"},
        "model_number_technical": {"type": model.datatypes.String, "unit": None, "description": "Technical designation of the machine model"},
        "serial_number": {"type": model.datatypes.String, "unit": None, "description": "Unique serial number assigned to the machine"},
        "host_name": {"type": model.datatypes.String, "unit": None, "description": "Network hostname for machine connectivity"},
        "feed_model": {"type": model.datatypes.String, "unit": None, "description": "Variant of the material feed system"},
        "feedstock_equipped": {"type": model.datatypes.String, "unit": None, "description": "Type of material currently loaded into the machine"},
        "remote_control": {"type": model.datatypes.Boolean, "unit": None, "description": "Boolean flag indicating if remote operation is enabled"},
        "exposure_unit_count": {"type": model.datatypes.Integer, "unit": None, "description": "Number of exposure units (e.g., laser sources)"},
        "build_volume": {
            "type": {"type": model.datatypes.String, "unit": None, "description": "Specifies whether the build volume is rectangular or cylindrical"},
            "x_dimension": {"type": model.datatypes.Double, "unit": "mm", "description": "Build plate width (X-axis)"},
            "y_dimension": {"type": model.datatypes.Double, "unit": "mm", "description": "Build plate depth (Y-axis)"},
            "z_dimension": {"type": model.datatypes.Double, "unit": "mm", "description": "Maximum build height (Z-axis)"},
            "diameter": {"type": model.datatypes.Double, "unit": "mm", "description": "Diameter of the build volume (if cylindrical)"}
        }
    },
    "Exposure_unit": {
        "galvo_scan_head_model": {"type": model.datatypes.String, "unit": None, "description": "Model of the galvanometer-based scanning head"},
        "galvo_scan_head_interface": {"type": model.datatypes.String, "unit": None, "description": "Type of interface for scan head control"},
        "galvo_scan_head_software": {"type": model.datatypes.String, "unit": None, "description": "Software/firmware version for scan head control"},
        "laser_source_model": {"type": model.datatypes.String, "unit": None, "description": "Model identifier of the laser source"},
        "laser_source_serial_number": {"type": model.datatypes.String, "unit": None, "description": "Serial number of the laser source"},
        "laser_source_software": {"type": model.datatypes.String, "unit": None, "description": "Firmware/software version of the laser source"},
        "laser_source_rated_power": {"type": model.datatypes.Double, "unit": "W", "description": "Maximum rated power output of the laser source"},
        "laser_powers": {"type": model.datatypes.Double, "unit": "W", "description": "List of available laser power settings"},
        "laser_mode": {"type": model.datatypes.String, "unit": None, "description": "Operating mode of the laser (e.g., continuous, pulsed, multimode)"},
        "laser_configuration": {"type": model.datatypes.String, "unit": None, "description": "Configurable laser power settings"},
        "beam_focus_diameter_min": {"type": model.datatypes.Double, "unit": "µm", "description": "Minimum focusable laser beam diameter"},
        "beam_focus_diameter_max": {"type": model.datatypes.Double, "unit": "µm", "description": "Maximum focusable laser beam diameter"}
    },
    "Atmosphere": {
        "filtration_model": {"type": model.datatypes.String, "unit": None, "description": "Type/model of the filtration system used for gas handling"},
        "filtration_serial_number": {"type": model.datatypes.String, "unit": None, "description": "Serial number of the filtration unit"},
        "filtration_safety_software": {"type": model.datatypes.String, "unit": None, "description": "Safety software version controlling filtration"},
        "filtration_software": {"type": model.datatypes.String, "unit": None, "description": "Filtration unit software version"},
        "inert_gas_equipped": {"type": model.datatypes.String, "unit": None, "description": "Type of shielding gas used in the build chamber"}
    },
    "PLC": {
        "model": {"type": model.datatypes.String, "unit": None, "description": "Model/type of the programmable logic controller (PLC)"},
        "serial_number": {"type": model.datatypes.String, "unit": None, "description": "Serial number of the PLC unit"},
        "software_version": {"type": model.datatypes.String, "unit": None, "description": "Version of the PLC software"}
    },
    "MCSW": {
        "print_domain": {"type": model.datatypes.String, "unit": None, "description": "Domain configuration for the printing process"},
        "control_system": {"type": model.datatypes.String, "unit": None, "description": "Supervisory control system of the machine"},
        "scada_system": {"type": model.datatypes.String, "unit": None, "description": "Version of SCADA software used"},
        "db_scheme": {"type": model.datatypes.String, "unit": None, "description": "Database schema version"},
        "db_service": {"type": model.datatypes.String, "unit": None, "description": "Database service version used by the machine"},
        "hcs_service": {"type": model.datatypes.String, "unit": None, "description": "Hardware control system service version"}
    }
}

from basyx.aas import model, adapter


def build_pbf_lbm_aas() -> tuple[model.AssetAdministrationShell, model.Submodel]:
    """Build the AAS and Submodel for a PBF-LB/M machine."""
    asset_information = model.AssetInformation(
        asset_kind=model.AssetKind.INSTANCE,
        global_asset_id="https://acplt.org/PBF-LB-M_AAS",
    )

    aas = model.AssetAdministrationShell(
        id_="https://acplt.org/PBF-LB-M_AAS",
        asset_information=asset_information,
    )

    submodel = model.Submodel(id_="https://acplt.org/PBF-LB-M_Submodel")
    aas.submodel.add(model.ModelReference.from_referable(submodel))

    machine_parameters = _flatten_parameters(machine_parameters_basic)
    for param, datatype in machine_parameters.items():
        submodel.submodel_element.add(
            model.Property(
                id_short=param,
                value_type=datatype,
                value=None,
                semantic_id=model.ExternalReference(
                    (
                        model.Key(
                            type_=model.KeyTypes.GLOBAL_REFERENCE,
                            value=f"https://acplt.org/Properties/{param}",
                        ),
                    )
                ),
            )
        )

    return aas, submodel


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the PBF-LB/M Machine Submodel as JSON"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Write JSON output to this file instead of stdout",
    )
    args = parser.parse_args()

    aas, submodel = build_pbf_lbm_aas()
    print("PBF-LB/M Machine Submodel created successfully!")
    json_string = json.dumps(
        {"the_submodel": submodel, "the_aas": aas},
        cls=aas_json.AASToJsonEncoder,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_string)
    else:
        print(json_string)


if __name__ == "__main__":
    main()
