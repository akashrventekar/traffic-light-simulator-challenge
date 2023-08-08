import pytest
from app import valid_input,get_traffic_light
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
    actual_bool_value = valid_input(input_duration)
    assert actual_bool_value == expected_bool_value


def test_exit():
    with pytest.raises(SystemExit):
        valid_input("exit")

@pytest.mark.parametrize(
    "red, yellow, green, expected_traffic_lights",
    [
        (
                True,
                False,
                False,
f"""
     ##
    _[]_
  [______]
.----''----.
|   .==.   |
\033[31m|  /####\  |
|  \####/  |\033[0m
|   .==.   |
|   .==.   |
|    /\    |
|    \/    |
|   .==.   |
|   .==.   |
|    /\    |
|    \/    |
|   .==.   |
'-.______.-'
    """

        ),
        (
                False,
                True,
                False,
f"""
     ##
    _[]_
  [______]
.----''----.
|   .==.   |
|    /\    |
|    \/    |
|   .==.   |
|   .==.   |
\033[33m|  /####\  |
|  \####/  |\033[0m
|   .==.   |
|   .==.   |
|    /\    |
|    \/    |
|   .==.   |
'-.______.-'
    """
        ),
        (
                False,
                False,
                True,
f"""
     ##
    _[]_
  [______]
.----''----.
|   .==.   |
|    /\    |
|    \/    |
|   .==.   |
|   .==.   |
|    /\    |
|    \/    |
|   .==.   |
|   .==.   |
\033[32m|  /####\  |
|  \####/  |\033[0m
|   .==.   |
'-.______.-'
    """
        ),
    ]
)
def test_set_traffic_light(red, yellow, green, expected_traffic_lights):
    actual_traffic_lights = get_traffic_light(red=red, yellow=yellow, green=green)
    assert actual_traffic_lights == expected_traffic_lights


