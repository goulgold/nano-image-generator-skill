import os
import sys
import importlib
import pytest

# Patch env before importing module
def load_module(env_vars):
    """Load generate_image with specific env vars set."""
    for k, v in env_vars.items():
        os.environ[k] = v
    import scripts.generate_image as m
    importlib.reload(m)
    return m

def test_api_key_reads_from_env(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key-abc123")
    import importlib
    import scripts.generate_image as m
    importlib.reload(m)
    assert m.get_api_key() == "test-key-abc123"

def test_api_key_missing_exits(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    import importlib
    import scripts.generate_image as m
    importlib.reload(m)
    with pytest.raises(SystemExit):
        m.get_api_key()
