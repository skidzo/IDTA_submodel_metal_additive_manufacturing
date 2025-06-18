import pytest
from am_machine import build_lpbf_aas


def test_submodel_contains_basic_properties():
    _, submodel = build_lpbf_aas()
    properties = [element.id_short for element in submodel.submodel_element]
    assert "manufacturer_brand" in properties
    assert "build_volume" in properties

