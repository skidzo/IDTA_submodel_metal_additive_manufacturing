import pytest
from basyx.aas import model
from am_machine import PBFLBMSubmodelBuilder, MACHINE_SPECIFICATION


def test_submodel_builder_creates_valid_aas_and_submodel():
    """Test that the builder creates valid AAS and Submodel objects."""
    builder = PBFLBMSubmodelBuilder()
    aas, submodel = builder.build_aas_and_submodel()
    
    # Check AAS is valid
    assert isinstance(aas, model.AssetAdministrationShell)
    assert aas.id == "https://acplt.org/PBF-LB-M_AAS"  # Fixed: use 'id' instead of 'id_'
    assert len(aas.submodel) == 1
    
    # Check Submodel is valid
    assert isinstance(submodel, model.Submodel)
    assert submodel.id == "https://acplt.org/PBF-LB-M_Submodel"  # Fixed: use 'id' instead of 'id_'


def test_submodel_contains_required_collections():
    """Test that the submodel contains all required main collections."""
    builder = PBFLBMSubmodelBuilder()
    _, submodel = builder.build_aas_and_submodel()
    
    collection_names = [element.id_short for element in submodel.submodel_element]
    
    # Check main collections exist
    assert "Info" in collection_names
    assert "Exposure_unit" in collection_names
    assert "Atmosphere" in collection_names
    assert "PLC" in collection_names
    assert "MCSW" in collection_names
    
    # Check we have the expected number of main collections
    assert len(collection_names) == 5


def test_info_collection_contains_basic_properties():
    """Test that the Info collection contains expected properties."""
    builder = PBFLBMSubmodelBuilder()
    _, submodel = builder.build_aas_and_submodel()
    
    info_collection = None
    for element in submodel.submodel_element:
        if element.id_short == "Info":
            info_collection = element
            break
    
    assert info_collection is not None
    assert isinstance(info_collection, model.SubmodelElementCollection)
    
    info_properties = [prop.id_short for prop in info_collection.value]
    
    # Check basic properties exist
    assert "manufacturer_brand" in info_properties
    assert "model_type" in info_properties
    assert "serial_number" in info_properties
    assert "build_volume" in info_properties


def test_build_volume_nested_collection():
    """Test that build_volume is a nested collection with correct properties."""
    builder = PBFLBMSubmodelBuilder()
    _, submodel = builder.build_aas_and_submodel()
    
    # Find Info collection
    info_collection = None
    for element in submodel.submodel_element:
        if element.id_short == "Info":
            info_collection = element
            break
    
    # Find build_volume within Info
    build_volume = None
    for prop in info_collection.value:
        if prop.id_short == "build_volume":
            build_volume = prop
            break
    
    assert build_volume is not None
    assert isinstance(build_volume, model.SubmodelElementCollection)
    
    build_volume_properties = [prop.id_short for prop in build_volume.value]
    assert "type" in build_volume_properties
    assert "x_dimension" in build_volume_properties
    assert "y_dimension" in build_volume_properties
    assert "z_dimension" in build_volume_properties
    assert "diameter" in build_volume_properties


def test_statistics_calculation():
    """Test that statistics are calculated correctly."""
    builder = PBFLBMSubmodelBuilder()
    _, submodel = builder.build_aas_and_submodel()
    
    stats = builder.get_statistics(submodel)
    
    assert "total_collections" in stats
    assert "total_properties" in stats
    assert "max_depth" in stats
    
    # Should have at least the main collections
    assert stats["total_collections"] >= 5
    # Should have many properties
    assert stats["total_properties"] > 20
    # Should have at least depth 2 (main collection -> nested collection)
    assert stats["max_depth"] >= 2


def test_machine_specification_structure():
    """Test that the machine specification has the expected structure."""
    assert isinstance(MACHINE_SPECIFICATION, dict)
    assert len(MACHINE_SPECIFICATION) == 5
    
    required_keys = ["Info", "Exposure_unit", "Atmosphere", "PLC", "MCSW"]
    for key in required_keys:
        assert key in MACHINE_SPECIFICATION
        assert MACHINE_SPECIFICATION[key].id_short == key


def test_semantic_references():
    """Test that semantic references are properly set."""
    builder = PBFLBMSubmodelBuilder()
    _, submodel = builder.build_aas_and_submodel()
    
    # Check submodel has semantic reference
    assert submodel.semantic_id is not None
    assert len(submodel.semantic_id.key) == 1
    assert "PBF-LB-M" in submodel.semantic_id.key[0].value
    
    # Check collections have semantic references
    for element in submodel.submodel_element:
        if isinstance(element, model.SubmodelElementCollection):
            assert element.semantic_id is not None
            assert len(element.semantic_id.key) == 1

