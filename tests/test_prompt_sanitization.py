# tests/test_prompt_sanitization.py
import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from scripts.generate_image import validate_prompt, MAX_PROMPT_LENGTH


def test_normal_prompt_passes():
    result = validate_prompt("A cute robot mascot")
    assert result == "A cute robot mascot"


def test_prompt_at_limit_passes():
    result = validate_prompt("x" * MAX_PROMPT_LENGTH)
    assert len(result) == MAX_PROMPT_LENGTH


def test_prompt_over_limit_exits():
    with pytest.raises(SystemExit) as exc_info:
        validate_prompt("x" * (MAX_PROMPT_LENGTH + 1))
    assert exc_info.value.code == 1


def test_empty_prompt_exits():
    with pytest.raises(SystemExit) as exc_info:
        validate_prompt("")
    assert exc_info.value.code == 1


def test_whitespace_only_prompt_exits():
    with pytest.raises(SystemExit) as exc_info:
        validate_prompt("   ")
    assert exc_info.value.code == 1
