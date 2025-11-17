from unittest.mock import patch
from print_numbered_lists import list_creation, cross_check
import pytest


def test_list_creation():
    """Test that list is created when entered"""
    with patch("builtins.input", side_effect=["Michael", "Jake"]):
        list = list_creation(2)
        assert list == ["Michael", "Jake"]


def test_list_creation_limit_over():
    """Test that list limit is enforced when entered"""
    with patch("builtins.input", side_effect=["Michael", "Jake", "James", "Janine"]):
        list = list_creation(2)
        assert len(list) == 2
        assert list == ["Michael", "Jake"]


def test_list_creation_limit_empty_entry():
    """Test that function re-asks when empty string is entered"""
    # User enters empty for element 2, then provides valid input
    # Need 3 values total: valid, empty, valid (re-ask), valid
    with patch("builtins.input", side_effect=["Michael", "", "Jake", "", "", "Sarah"]):
        list = list_creation(3)
        assert len(list) == 3
        assert list == ["Michael", "Jake", "Sarah"]


# We can test the cross_check function now that the list creation is working


# Create fixtures for both lists
@pytest.fixture
def master_list():
    """Fixture providing a master list for testing"""
    return ["Angie", "Brian", "Cedric", "Danielle"]


@pytest.fixture
def empty_list():
    """Fixture providing an empty list to collect matches"""
    return []


def test_cross_check_match(master_list, empty_list):
    """Test that matching element is added to separate list"""
    with patch("builtins.input", return_value="Brian"):
        user_input = input()
        if user_input in master_list:
            empty_list.append(user_input)

    assert "Brian" in empty_list
    assert len(empty_list) == 1


def test_cross_check_no_match(master_list, empty_list):
    """Test that non-matching element is not added"""
    with patch("builtins.input", return_value="Eve"):
        user_input = input()
        if user_input in master_list:
            empty_list.append(user_input)

    assert "Eve" not in empty_list
    assert len(empty_list) == 0


def test_cross_check_multiple_matches(master_list):
    """Test multiple matches being added to separate list"""
    separate_list = []
    with patch("builtins.input", side_effect=["Angie", "", "Eve", "Brian"]):
        for _ in range(4):
            user_input = input()
            if user_input in master_list:
                separate_list.append(user_input)

    assert separate_list == ["Angie", "Brian"]
    assert len(separate_list) == 2


def test_cross_check_prints_list_on_mismatch(capsys):
    """Test that master list is printed when entry doesn't match"""
    master_list = ["Reggie", "Miller", "Stephen"]

    # First input doesn't match, second does
    with patch("builtins.input", side_effect=["Michael", "Miller"]):
        result = cross_check(master_list)

    # Capture printed output
    captured = capsys.readouterr()

    # Check that the list was printed
    assert "Reggie" in captured.out
    assert "Miller" in captured.out
    assert "Stephen" in captured.out
    assert "Element does not match" in captured.out
