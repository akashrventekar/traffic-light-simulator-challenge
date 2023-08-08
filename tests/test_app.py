import pytest
from app import valid_duration
@pytest.mark.parametrize(
    "input_duration, expected_bool_value",
    [
        (
                10,
                True
        ),
        (
                None,
                False
        ),
        (
                "string",
                False
        ),
        (
                "",
                False
        ),
        (
                'C',
                False
        ),
        (
                "test",
                False
        ),
        (
                "$",
                False
        ),
    ]
)
def test_valid_duration(input_duration, expected_bool_value):
    actual_bool_value = valid_duration(input_duration)
    assert actual_bool_value == expected_bool_value