import argparse
import json
from typing import Dict, Any, Union, List, Optional, Type
from dataclasses import dataclass
from enum import Enum

from basyx.aas import model, adapter
from basyx.aas.adapter import json as aas_json


class ElementType(Enum):
    """Types of submodel elements."""
    PROPERTY = "property"
    COLLECTION = "collection"


@dataclass
class ElementSpec:
    """Specification for a submodel element."""
    id_short: str
    element_type: ElementType
    value_type: Optional[Type] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    children: Optional[Dict[str, 'ElementSpec']] = None
    semantic_id_suffix: Optional[str] = None


# ============================================================================
# MACHINE SPECIFICATION DEFINITIONS
# ============================================================================

# Info Section Elements
MANUFACTURER_BRAND = ElementSpec(
    id_short="manufacturer_brand",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Name of the AM machine manufacturer (e.g., SLM, TRUMPF, EOS)"
)

MODEL_TYPE = ElementSpec(
    id_short="model_type",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Type of machine, specifying whether it's for metal or polymer"
)

MODEL_NUMBER = ElementSpec(
    id_short="model_number",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Product model number of the machine"
)

MODEL_NUMBER_TECHNICAL = ElementSpec(
    id_short="model_number_technical",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Technical designation of the machine model"
)

SERIAL_NUMBER = ElementSpec(
    id_short="serial_number",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Unique serial number assigned to the machine"
)

HOST_NAME = ElementSpec(
    id_short="host_name",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Network hostname for machine connectivity"
)

FEED_MODEL = ElementSpec(
    id_short="feed_model",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Variant of the material feed system"
)

FEEDSTOCK_EQUIPPED = ElementSpec(
    id_short="feedstock_equipped",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Type of material currently loaded into the machine"
)

REMOTE_CONTROL = ElementSpec(
    id_short="remote_control",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Boolean,
    description="Boolean flag indicating if remote operation is enabled"
)

EXPOSURE_UNIT_COUNT = ElementSpec(
    id_short="exposure_unit_count",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Integer,
    description="Number of exposure units (e.g., laser sources)"
)

# Build Volume Elements
BUILD_VOLUME_TYPE = ElementSpec(
    id_short="type",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Specifies whether the build volume is rectangular or cylindrical"
)

BUILD_VOLUME_X = ElementSpec(
    id_short="x_dimension",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="mm",
    description="Build plate width (X-axis)"
)

BUILD_VOLUME_Y = ElementSpec(
    id_short="y_dimension",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="mm",
    description="Build plate depth (Y-axis)"
)

BUILD_VOLUME_Z = ElementSpec(
    id_short="z_dimension",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="mm",
    description="Maximum build height (Z-axis)"
)

BUILD_VOLUME_DIAMETER = ElementSpec(
    id_short="diameter",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="mm",
    description="Diameter of the build volume (if cylindrical)"
)

BUILD_VOLUME = ElementSpec(
    id_short="build_volume",
    element_type=ElementType.COLLECTION,
    description="Build volume specifications",
    semantic_id_suffix="BuildVolume",
    children={
        "type": BUILD_VOLUME_TYPE,
        "x_dimension": BUILD_VOLUME_X,
        "y_dimension": BUILD_VOLUME_Y,
        "z_dimension": BUILD_VOLUME_Z,
        "diameter": BUILD_VOLUME_DIAMETER
    }
)

# Exposure Unit Elements
GALVO_SCAN_HEAD_MODEL = ElementSpec(
    id_short="galvo_scan_head_model",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Model of the galvanometer-based scanning head"
)

GALVO_SCAN_HEAD_INTERFACE = ElementSpec(
    id_short="galvo_scan_head_interface",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Type of interface for scan head control"
)

GALVO_SCAN_HEAD_SOFTWARE = ElementSpec(
    id_short="galvo_scan_head_software",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Software/firmware version for scan head control"
)

LASER_SOURCE_MODEL = ElementSpec(
    id_short="laser_source_model",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Model identifier of the laser source"
)

LASER_SOURCE_SERIAL_NUMBER = ElementSpec(
    id_short="laser_source_serial_number",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Serial number of the laser source"
)

LASER_SOURCE_SOFTWARE = ElementSpec(
    id_short="laser_source_software",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Firmware/software version of the laser source"
)

LASER_SOURCE_RATED_POWER = ElementSpec(
    id_short="laser_source_rated_power",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="W",
    description="Maximum rated power output of the laser source"
)

LASER_POWERS = ElementSpec(
    id_short="laser_powers",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="W",
    description="Available laser power settings"
)

LASER_MODE = ElementSpec(
    id_short="laser_mode",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Operating mode of the laser (e.g., continuous, pulsed, multimode)"
)

LASER_CONFIGURATION = ElementSpec(
    id_short="laser_configuration",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Configurable laser power settings"
)

BEAM_FOCUS_DIAMETER_MIN = ElementSpec(
    id_short="beam_focus_diameter_min",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="µm",
    description="Minimum focusable laser beam diameter"
)

BEAM_FOCUS_DIAMETER_MAX = ElementSpec(
    id_short="beam_focus_diameter_max",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.Double,
    unit="µm",
    description="Maximum focusable laser beam diameter"
)

# Atmosphere Elements
FILTRATION_MODEL = ElementSpec(
    id_short="filtration_model",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Type/model of the filtration system used for gas handling"
)

FILTRATION_SERIAL_NUMBER = ElementSpec(
    id_short="filtration_serial_number",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Serial number of the filtration unit"
)

FILTRATION_SAFETY_SOFTWARE = ElementSpec(
    id_short="filtration_safety_software",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Safety software version controlling filtration"
)

FILTRATION_SOFTWARE = ElementSpec(
    id_short="filtration_software",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Filtration unit software version"
)

INERT_GAS_EQUIPPED = ElementSpec(
    id_short="inert_gas_equipped",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Type of shielding gas used in the build chamber"
)

# PLC Elements
PLC_MODEL = ElementSpec(
    id_short="model",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Model/type of the programmable logic controller (PLC)"
)

PLC_SERIAL_NUMBER = ElementSpec(
    id_short="serial_number",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Serial number of the PLC unit"
)

PLC_SOFTWARE_VERSION = ElementSpec(
    id_short="software_version",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Version of the PLC software"
)

# MCSW Elements
MCSW_PRINT_DOMAIN = ElementSpec(
    id_short="print_domain",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Domain configuration for the printing process"
)

MCSW_CONTROL_SYSTEM = ElementSpec(
    id_short="control_system",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Supervisory control system of the machine"
)

MCSW_SCADA_SYSTEM = ElementSpec(
    id_short="scada_system",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Version of SCADA software used"
)

MCSW_DB_SCHEME = ElementSpec(
    id_short="db_scheme",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Database schema version"
)

MCSW_DB_SERVICE = ElementSpec(
    id_short="db_service",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Database service version used by the machine"
)

MCSW_HCS_SERVICE = ElementSpec(
    id_short="hcs_service",
    element_type=ElementType.PROPERTY,
    value_type=model.datatypes.String,
    description="Hardware control system service version"
)

# ============================================================================
# MAIN COLLECTIONS
# ============================================================================

INFO_COLLECTION = ElementSpec(
    id_short="Info",
    element_type=ElementType.COLLECTION,
    description="General information about the PBF-LB/M machine",
    semantic_id_suffix="Info",
    children={
        "manufacturer_brand": MANUFACTURER_BRAND,
        "model_type": MODEL_TYPE,
        "model_number": MODEL_NUMBER,
        "model_number_technical": MODEL_NUMBER_TECHNICAL,
        "serial_number": SERIAL_NUMBER,
        "host_name": HOST_NAME,
        "feed_model": FEED_MODEL,
        "feedstock_equipped": FEEDSTOCK_EQUIPPED,
        "remote_control": REMOTE_CONTROL,
        "exposure_unit_count": EXPOSURE_UNIT_COUNT,
        "build_volume": BUILD_VOLUME
    }
)

EXPOSURE_UNIT_COLLECTION = ElementSpec(
    id_short="Exposure_unit",
    element_type=ElementType.COLLECTION,
    description="Laser and galvanometer system specifications",
    semantic_id_suffix="ExposureUnit",
    children={
        "galvo_scan_head_model": GALVO_SCAN_HEAD_MODEL,
        "galvo_scan_head_interface": GALVO_SCAN_HEAD_INTERFACE,
        "galvo_scan_head_software": GALVO_SCAN_HEAD_SOFTWARE,
        "laser_source_model": LASER_SOURCE_MODEL,
        "laser_source_serial_number": LASER_SOURCE_SERIAL_NUMBER,
        "laser_source_software": LASER_SOURCE_SOFTWARE,
        "laser_source_rated_power": LASER_SOURCE_RATED_POWER,
        "laser_powers": LASER_POWERS,
        "laser_mode": LASER_MODE,
        "laser_configuration": LASER_CONFIGURATION,
        "beam_focus_diameter_min": BEAM_FOCUS_DIAMETER_MIN,
        "beam_focus_diameter_max": BEAM_FOCUS_DIAMETER_MAX
    }
)

ATMOSPHERE_COLLECTION = ElementSpec(
    id_short="Atmosphere",
    element_type=ElementType.COLLECTION,
    description="Gas handling and filtration system specifications",
    semantic_id_suffix="Atmosphere",
    children={
        "filtration_model": FILTRATION_MODEL,
        "filtration_serial_number": FILTRATION_SERIAL_NUMBER,
        "filtration_safety_software": FILTRATION_SAFETY_SOFTWARE,
        "filtration_software": FILTRATION_SOFTWARE,
        "inert_gas_equipped": INERT_GAS_EQUIPPED
    }
)

PLC_COLLECTION = ElementSpec(
    id_short="PLC",
    element_type=ElementType.COLLECTION,
    description="Programmable Logic Controller specifications",
    semantic_id_suffix="PLC",
    children={
        "model": PLC_MODEL,
        "serial_number": PLC_SERIAL_NUMBER,
        "software_version": PLC_SOFTWARE_VERSION
    }
)

MCSW_COLLECTION = ElementSpec(
    id_short="MCSW",
    element_type=ElementType.COLLECTION,
    description="Machine Control Software specifications",
    semantic_id_suffix="MCSW",
    children={
        "print_domain": MCSW_PRINT_DOMAIN,
        "control_system": MCSW_CONTROL_SYSTEM,
        "scada_system": MCSW_SCADA_SYSTEM,
        "db_scheme": MCSW_DB_SCHEME,
        "db_service": MCSW_DB_SERVICE,
        "hcs_service": MCSW_HCS_SERVICE
    }
)

# ============================================================================
# ROOT MACHINE SPECIFICATION
# ============================================================================

MACHINE_SPECIFICATION = {
    "Info": INFO_COLLECTION,
    "Exposure_unit": EXPOSURE_UNIT_COLLECTION,
    "Atmosphere": ATMOSPHERE_COLLECTION,
    "PLC": PLC_COLLECTION,
    "MCSW": MCSW_COLLECTION
}


class PBFLBMSubmodelBuilder:
    """Robust builder for PBF-LB/M machine submodels."""
    
    def __init__(self, base_semantic_uri: str = "https://admin-shell.io/IDTA/PBF-LB-M/1/0"):
        self.base_semantic_uri = base_semantic_uri
        self.property_base_uri = "https://acplt.org/Properties"
        
    def _create_semantic_reference(self, suffix: str) -> model.ExternalReference:
        """Create a semantic reference for an element."""
        return model.ExternalReference(
            (
                model.Key(
                    type_=model.KeyTypes.GLOBAL_REFERENCE,
                    value=f"{self.base_semantic_uri}/{suffix}",
                ),
            )
        )

    def _create_property_semantic_reference(self, property_name: str) -> model.ExternalReference:
        """Create a semantic reference for a property."""
        return model.ExternalReference(
            (
                model.Key(
                    type_=model.KeyTypes.GLOBAL_REFERENCE,
                    value=f"{self.property_base_uri}/{property_name}",
                ),
            )
        )

    def _create_property(self, spec: ElementSpec) -> model.Property:
        """Create a property from specification."""
        prop = model.Property(
            id_short=spec.id_short,
            value_type=spec.value_type,
            value=None,
            semantic_id=self._create_property_semantic_reference(spec.id_short)
        )
        
        if spec.description:
            prop.description = model.MultiLanguageTextType({"en": spec.description})
        
        if spec.unit:
            prop.qualifier = {
                model.Qualifier(
                    type_="unit",
                    value=spec.unit,
                    value_type=model.datatypes.String
                )
            }
        
        return prop

    def _create_collection(self, spec: ElementSpec) -> model.SubmodelElementCollection:
        """Create a collection from specification."""
        collection = model.SubmodelElementCollection(id_short=spec.id_short)
        
        if spec.description:
            collection.description = model.MultiLanguageTextType({"en": spec.description})
        
        if spec.semantic_id_suffix:
            collection.semantic_id = self._create_semantic_reference(spec.semantic_id_suffix)
        
        return collection

    def _build_submodel_element(self, spec: ElementSpec) -> model.SubmodelElement:
        """Recursively build submodel elements from specification."""
        if spec.element_type == ElementType.PROPERTY:
            return self._create_property(spec)
        
        elif spec.element_type == ElementType.COLLECTION:
            collection = self._create_collection(spec)
            
            if spec.children:
                for child_spec in spec.children.values():
                    child_element = self._build_submodel_element(child_spec)
                    collection.value.add(child_element)
            
            return collection
        
        else:
            raise ValueError(f"Unknown element type: {spec.element_type}")

    def build_aas_and_submodel(self, 
                              aas_id: str = "https://acplt.org/PBF-LB-M_AAS",
                              submodel_id: str = "https://acplt.org/PBF-LB-M_Submodel") -> tuple[model.AssetAdministrationShell, model.Submodel]:
        """Build complete AAS and Submodel from specification."""
        
        # Create Asset Information
        asset_information = model.AssetInformation(
            asset_kind=model.AssetKind.INSTANCE,
            global_asset_id=aas_id,
        )

        # Create AAS
        aas = model.AssetAdministrationShell(
            id_=aas_id,
            asset_information=asset_information,
        )

        # Create Submodel
        submodel = model.Submodel(
            id_=submodel_id,
            semantic_id=self._create_semantic_reference("Submodel")
        )
        
        # Add submodel reference to AAS
        aas.submodel.add(model.ModelReference.from_referable(submodel))

        # Build all submodel elements from specification
        for element_spec in MACHINE_SPECIFICATION.values():
            element = self._build_submodel_element(element_spec)
            submodel.submodel_element.add(element)

        return aas, submodel

    def get_statistics(self, submodel: model.Submodel) -> Dict[str, int]:
        """Get statistics about the generated submodel."""
        stats = {
            "total_collections": 0,
            "total_properties": 0,
            "max_depth": 0
        }
        
        def count_elements(elements, depth=0):
            stats["max_depth"] = max(stats["max_depth"], depth)
            
            for element in elements:
                if isinstance(element, model.SubmodelElementCollection):
                    stats["total_collections"] += 1
                    count_elements(element.value, depth + 1)
                elif isinstance(element, model.Property):
                    stats["total_properties"] += 1
        
        count_elements(submodel.submodel_element)
        return stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the PBF-LB/M Machine Submodel as JSON using maintainable variable definitions"
    )
    parser.add_argument(
        "-o", "--output",
        help="Write JSON output to this file",
        default="pbf_lbm_submodel.json"
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty print JSON output"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics about the generated submodel"
    )
    args = parser.parse_args()

    try:
        # Build submodel using maintainable variable definitions
        builder = PBFLBMSubmodelBuilder()
        aas, submodel = builder.build_aas_and_submodel()
        
        print("✓ PBF-LB/M Machine Submodel created successfully using maintainable definitions!")
        
        # Show statistics if requested
        if args.stats:
            stats = builder.get_statistics(submodel)
            print(f"✓ Statistics:")
            print(f"  - Total Collections: {stats['total_collections']}")
            print(f"  - Total Properties: {stats['total_properties']}")
            print(f"  - Maximum Depth: {stats['max_depth']}")
        
        # Create object store for proper serialization
        object_store = model.DictObjectStore()
        object_store.add(aas)
        object_store.add(submodel)
        
        # Serialize to JSON
        json_data = aas_json.object_store_to_json(object_store)
        
        if args.pretty:
            json_string = json.dumps(json_data, indent=2, ensure_ascii=False)
        else:
            json_string = json.dumps(json_data, ensure_ascii=False)

        # Write output
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_string)
        print(f"✓ JSON output written to: {args.output}")
            
    except Exception as e:
        print(f"✗ Error creating submodel: {e}")
        raise


if __name__ == "__main__":
    main()
