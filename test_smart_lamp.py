import pytest

from smart_lamp import should_lamp_turn_on


@pytest.mark.parametrize(
    "motion, light_level, expected",
    [
        ("yes", 20, True),
        ("yes", 49, True),
        ("yes", 50, False),
        ("yes", 51, False),
        ("yes", 80, False),
        ("no", 20, False),
        ("no", 80, False),
        ("yes", 0, True),
        ("yes", 100, False),
	("y", 20, True),
	("y", 80, False),
	("n", 20, False),
	("n", 80, False),
    ],
)
def test_lamp_decision(motion, light_level, expected):
    result = should_lamp_turn_on(motion, light_level)

    assert result is expected


def test_light_level_below_valid_range():
    with pytest.raises(ValueError):
        should_lamp_turn_on("yes", -1)


def test_light_level_above_valid_range():
    with pytest.raises(ValueError):
        should_lamp_turn_on("yes", 101)


def test_invalid_motion():
    with pytest.raises(ValueError):
        should_lamp_turn_on("maybe", 20)
