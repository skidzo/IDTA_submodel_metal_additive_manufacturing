import pytest
from am_machine import build_pbf_lbm_aas


def test_submodel_contains_basic_properties():
    _, submodel = build_pbf_lbm_aas()
    properties = [element.id_short for element in submodel.submodel_element]
    assert "manufacturer_brand" in properties
    assert "x_dimension" in properties


