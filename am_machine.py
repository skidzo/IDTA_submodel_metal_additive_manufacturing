import json

from basyx.aas import model
from basyx.aas.adapter import json as aas_json

# Improved structured dictionary for LPBF machine parameters aligned with Eclipse BaSyx SDK
machine_parameters = {
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

# Step 1: Create an Asset Administration Shell (AAS) with AssetInformation
asset_information = model.AssetInformation(
    asset_kind=model.AssetKind.INSTANCE,
    global_asset_id='https://acplt.org/LPBF_AAS'
)

# Create the AAS
aas = model.AssetAdministrationShell(
    id_='https://acplt.org/LPBF_AAS',
    asset_information=asset_information
)

# Step 2: Create a Submodel
submodel = model.Submodel(
    id_='https://acplt.org/LPBF_Submodel'
)

# Add the Submodel reference to the AAS
aas.submodel.add(model.ModelReference.from_referable(submodel))

# Step 3: Define machine parameters as Properties and add them to the Submodel
machine_parameters = {
    "manufacturer_brand": model.datatypes.String,
    "model_type": model.datatypes.String,
    "model_number": model.datatypes.String,
    "serial_number": model.datatypes.String,
    "feedstock_equipped": model.datatypes.String,
    "remote_control": model.datatypes.Boolean,
    "x_dimension": model.datatypes.Double,
    "y_dimension": model.datatypes.Double,
    "z_dimension": model.datatypes.Double,
    "laser_source_model": model.datatypes.String,
    "laser_source_rated_power": model.datatypes.Double,
    "beam_focus_diameter_min": model.datatypes.Double,
    "beam_focus_diameter_max": model.datatypes.Double
}

# Create and add properties to the submodel
for param, datatype in machine_parameters.items():
    submodel.submodel_element.add(model.Property(
        id_short=param,
        value_type=datatype,
        value=None,
        semantic_id=model.ExternalReference(
            (model.Key(
                type_=model.KeyTypes.GLOBAL_REFERENCE,
                value=f'https://acplt.org/Properties/{param}'
            ),)
        )
    ))

# Print a confirmation message
print("LPBF Machine Submodel created successfully!")

json_string = json.dumps({'the_submodel': submodel,
                           'the_aas': aas
                           },
                          cls=adapter.json.AASToJsonEncoder)

print(json_string)
