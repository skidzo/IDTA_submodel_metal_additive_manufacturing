import pytest
from am_machine import _flatten_parameters, machine_parameters_basic
from basyx.aas import model


def test_flatten_parameters_basic_subset():
    expected = {
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
        "beam_focus_diameter_max": model.datatypes.Double,
    }
    flattened = _flatten_parameters(machine_parameters_basic)
    for key, datatype in expected.items():
        assert key in flattened, f"Missing parameter: {key}"
        assert flattened[key] == datatype


