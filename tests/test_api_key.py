import os
import importlib
import pytest

def test_api_key_reads_from_env(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key-abc123")
    import scripts.generate_image as m
    importlib.reload(m)
    assert m.get_api_key() == "test-key-abc123"

def test_api_key_missing_exits(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    import scripts.generate_image as m
    importlib.reload(m)
    with pytest.raises(SystemExit) as exc_info:
        m.get_api_key()
    assert exc_info.value.code == 1
