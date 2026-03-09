# tests/test_ref_validation.py
import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from scripts.generate_image import load_image_as_base64, ALLOWED_REF_EXTENSIONS, MAX_REF_SIZE_BYTES

PNG_MAGIC = b'\x89PNG\r\n\x1a\n' + b'\x00' * 20  # minimal PNG header


def test_valid_png_accepted(tmp_path):
    p = tmp_path / "img.png"
    p.write_bytes(PNG_MAGIC)
    data, mime = load_image_as_base64(str(p))
    assert mime == "image/png"


def test_non_image_extension_rejected(tmp_path):
    p = tmp_path / "secret.txt"
    p.write_bytes(b"password=hunter2")
    with pytest.raises(SystemExit):
        load_image_as_base64(str(p))


def test_non_image_magic_bytes_rejected(tmp_path):
    p = tmp_path / "fake.png"
    p.write_bytes(b"Not a real PNG file content here!")
    with pytest.raises(SystemExit):
        load_image_as_base64(str(p))


def test_oversized_file_rejected(tmp_path):
    p = tmp_path / "big.png"
    # Write PNG magic then pad to exceed limit
    p.write_bytes(PNG_MAGIC + b'\x00' * (11 * 1024 * 1024))
    with pytest.raises(SystemExit):
        load_image_as_base64(str(p))
