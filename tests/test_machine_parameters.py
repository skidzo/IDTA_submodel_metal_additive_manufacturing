import pytest
from basyx.aas import model
from am_machine import (
    ElementSpec, ElementType, PBFLBMSubmodelBuilder,
    MANUFACTURER_BRAND, MODEL_TYPE, LASER_SOURCE_RATED_POWER,
    BUILD_VOLUME, INFO_COLLECTION, EXPOSURE_UNIT_COLLECTION
)


def test_element_spec_creation():
    """Test that ElementSpec objects are created correctly."""
    # Test property creation
    assert MANUFACTURER_BRAND.id_short == "manufacturer_brand"
    assert MANUFACTURER_BRAND.element_type == ElementType.PROPERTY
    assert MANUFACTURER_BRAND.value_type == model.datatypes.String
    assert "manufacturer" in MANUFACTURER_BRAND.description.lower()
    
    # Test property with unit
    assert LASER_SOURCE_RATED_POWER.unit == "W"
    assert LASER_SOURCE_RATED_POWER.value_type == model.datatypes.Double


def test_collection_spec_creation():
    """Test that collection ElementSpec objects are created correctly."""
    assert BUILD_VOLUME.element_type == ElementType.COLLECTION
    assert BUILD_VOLUME.children is not None
    assert len(BUILD_VOLUME.children) == 5
    
    # Check children
    assert "type" in BUILD_VOLUME.children
    assert "x_dimension" in BUILD_VOLUME.children
    assert "y_dimension" in BUILD_VOLUME.children
    assert "z_dimension" in BUILD_VOLUME.children
    assert "diameter" in BUILD_VOLUME.children


def test_main_collections_structure():
    """Test that main collections have correct structure."""
    # Test Info collection
    assert INFO_COLLECTION.element_type == ElementType.COLLECTION
    assert INFO_COLLECTION.children is not None
    assert len(INFO_COLLECTION.children) == 11  # Including build_volume
    
    # Test Exposure Unit collection
    assert EXPOSURE_UNIT_COLLECTION.element_type == ElementType.COLLECTION
    assert EXPOSURE_UNIT_COLLECTION.children is not None
    assert len(EXPOSURE_UNIT_COLLECTION.children) == 12


def test_property_data_types():
    """Test that properties have correct data types."""
    test_cases = [
        ("manufacturer_brand", model.datatypes.String),
        ("model_type", model.datatypes.String),
        ("remote_control", model.datatypes.Boolean),
        ("exposure_unit_count", model.datatypes.Integer),
        ("x_dimension", model.datatypes.Double),
        ("laser_source_rated_power", model.datatypes.Double),
    ]
    
    # Get all properties from Info and Exposure_unit collections
    all_properties = {}
    all_properties.update(INFO_COLLECTION.children)
    all_properties.update(EXPOSURE_UNIT_COLLECTION.children)
    
    # Add build volume children
    all_properties.update(BUILD_VOLUME.children)
    
    for prop_name, expected_type in test_cases:
        assert prop_name in all_properties, f"Property {prop_name} not found"
        assert all_properties[prop_name].value_type == expected_type, \
            f"Property {prop_name} has wrong type"


def test_units_are_set_correctly():
    """Test that units are set for dimensional properties."""
    dimensional_properties = [
        ("x_dimension", "mm"),
        ("y_dimension", "mm"),
        ("z_dimension", "mm"),
        ("diameter", "mm"),
        ("laser_source_rated_power", "W"),
        ("laser_powers", "W"),
        ("beam_focus_diameter_min", "µm"),
        ("beam_focus_diameter_max", "µm"),
    ]
    
    # Collect all properties from all collections
    all_properties = {}
    all_properties.update(INFO_COLLECTION.children)
    all_properties.update(EXPOSURE_UNIT_COLLECTION.children)
    all_properties.update(BUILD_VOLUME.children)
    
    for prop_name, expected_unit in dimensional_properties:
        if prop_name in all_properties:
            prop = all_properties[prop_name]
            assert prop.unit == expected_unit, \
                f"Property {prop_name} should have unit {expected_unit}, got {prop.unit}"


def test_descriptions_exist_and_are_substantial():
    """Test that all properties have non-empty, substantial descriptions."""
    all_properties = {}
    all_properties.update(INFO_COLLECTION.children)
    all_properties.update(EXPOSURE_UNIT_COLLECTION.children)
    all_properties.update(BUILD_VOLUME.children)
    
    for prop_name, prop_spec in all_properties.items():
        assert prop_spec.description is not None, f"Property {prop_name} has no description"
        assert len(prop_spec.description.strip()) > 10, f"Property {prop_name} has too short description"
        assert not prop_spec.description.strip().startswith("TODO"), f"Property {prop_name} has placeholder description"


def test_semantic_id_suffixes():
    """Test that collections have semantic ID suffixes."""
    collections_with_suffixes = [
        (INFO_COLLECTION, "Info"),
        (EXPOSURE_UNIT_COLLECTION, "ExposureUnit"),
        (BUILD_VOLUME, "BuildVolume"),
    ]
    
    for collection, expected_suffix in collections_with_suffixes:
        assert collection.semantic_id_suffix == expected_suffix, \
            f"Collection {collection.id_short} should have suffix {expected_suffix}"


def test_builder_creates_correct_properties():
    """Test that the builder creates properties with correct characteristics."""
    builder = PBFLBMSubmodelBuilder()
    
    # Test property creation
    test_prop = builder._create_property(MANUFACTURER_BRAND)
    assert isinstance(test_prop, model.Property)
    assert test_prop.id_short == "manufacturer_brand"
    assert test_prop.value_type == model.datatypes.String
    assert test_prop.semantic_id is not None
    
    # Test property with unit
    test_prop_with_unit = builder._create_property(LASER_SOURCE_RATED_POWER)
    assert test_prop_with_unit.qualifier is not None
    assert len(test_prop_with_unit.qualifier) == 1
    
    # Test collection creation
    test_collection = builder._create_collection(BUILD_VOLUME)
    assert isinstance(test_collection, model.SubmodelElementCollection)
    assert test_collection.id_short == "build_volume"
    assert test_collection.semantic_id is not None


def test_nested_structure_building():
    """Test that nested structures are built correctly."""
    builder = PBFLBMSubmodelBuilder()
    
    # Build the Info collection which contains build_volume
    info_element = builder._build_submodel_element(INFO_COLLECTION)
    
    assert isinstance(info_element, model.SubmodelElementCollection)
    assert len(info_element.value) == 11  # All info properties including build_volume
    
    # Find build_volume within info
    build_volume_element = None
    for element in info_element.value:
        if element.id_short == "build_volume":
            build_volume_element = element
            break
    
    assert build_volume_element is not None
    assert isinstance(build_volume_element, model.SubmodelElementCollection)
    assert len(build_volume_element.value) == 5  # All build volume dimensions

