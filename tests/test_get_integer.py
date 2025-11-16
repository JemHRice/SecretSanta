from unittest.mock import patch
from get_integer import get_integer_input
import pytest


def test_valid_integer_input():
    """Test that valid integer input is accepted"""
    with patch("builtins.input", return_value="42"):
        result = get_integer_input("Enter a number: ")
        assert result == 42


def test_negative_integer_input():
    """Test that negative integers are accepted"""
    with patch("builtins.input", return_value="-10"):
        result = get_integer_input("Enter a number: ")
        assert result == -10


def test_invalid_then_valid_input():
    """Test that function retries after invalid input"""
    # Simulate user entering invalid input first, then valid
    with patch("builtins.input", side_effect=["abc", "25"]):
        result = get_integer_input("Enter a number: ")
        assert result == 25


def test_multiple_invalid_then_valid():
    """Test multiple invalid attempts before valid input"""
    with patch("builtins.input", side_effect=["hello", "3.14", "xyz", "100"]):
        result = get_integer_input("Enter a number: ")
        assert result == 100


def test_empty_string_then_valid():
    """Test empty string followed by valid input"""
    with patch("builtins.input", side_effect=["", "15"]):
        result = get_integer_input("Enter a number: ")
        assert result == 15


def test_keyboard_interrupt():
    """Test that KeyboardInterrupt is properly raised"""
    with patch("builtins.input", side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            get_integer_input("Enter a number: ")
