import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets


@pytest.mark.parametrize(
    "input,expected_value",
    [
        ("{}{}(ali)[]", True),
        ("{[]([])}", True),
        ("{(])}", False),
        ("{)})[]", False),
    ],
)
def test_validate_brackets(input, expected_value):

    output = validate_brackets(input)
    print(output)
    assert output == expected_value


def test_validate_brackets_empty_input():
    with pytest.raises(Exception, match="The input value is empty"):
        validate_brackets("")
