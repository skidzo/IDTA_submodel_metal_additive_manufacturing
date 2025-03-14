import json

from basyx.aas import model
from basyx.aas.adapter import json as aas_json



# Improved structured dictionary for LPBF machine parameters aligned with Eclipse BaSyx SDK
machine_parameters = {
    "Info": {
        "manufacturer_brand": model.datatypes.String,
        "model_type": model.datatypes.String,
        "model_number": model.datatypes.String,
        "model_number_technical": model.datatypes.String,
        "serial_number": model.datatypes.String,
        "host_name": model.datatypes.String,
        "feed_model": model.datatypes.String,
        "feedstock_equipped": model.datatypes.String,
        "remote_control": model.datatypes.Boolean,
        "build_plate_dimensions": {
            "x_dimension": model.datatypes.Double,
            "y_dimension": model.datatypes.Double,
            "z_dimension": model.datatypes.Double
        },
        "exposure_unit_count": model.datatypes.Integer
    },
    "Exposure_unit": {
        "galvo_scan_head_model": model.datatypes.String,
        "galvo_scan_head_interface": model.datatypes.String,
        "galvo_scan_head_software": model.datatypes.String,
        "laser_source_model": model.datatypes.String,
        "laser_source_serial_number": model.datatypes.String,
        "laser_source_software": model.datatypes.String,
        "laser_source_rated_power": model.datatypes.Double,
        "laser_powers": model.datatypes.Double,
        "laser_mode": model.datatypes.String,
        "laser_configuration": model.datatypes.String,
        "laser_configuration_mode": model.datatypes.String,
        "beam_focus_diameter_min": model.datatypes.Double,
        "beam_focus_diameter_max": model.datatypes.Double
    },
    "Atmosphere": {
        "filtration_model": model.datatypes.String,
        "filtration_serial_number": model.datatypes.String,
        "filtration_safety_software": model.datatypes.String,
        "filtration_software": model.datatypes.String,
        "inert_gas_equipped": model.datatypes.String
    },
    "PLC": {
        "model": model.datatypes.String,
        "serial_number": model.datatypes.String,
        "software_version": model.datatypes.String
    },
    "MCSW": {
        "print_domain": model.datatypes.String,
        "control_system": model.datatypes.String,
        "scada_system": model.datatypes.String,
        "db_scheme": model.datatypes.String,
        "db_service": model.datatypes.String,
        "hcs_service": model.datatypes.String
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
