import pytest
import os
import pydantic

import _config

UNEXISTING_CONFIG_PATH = "test/test_config.toml"
EXISTING_SAMPLE_CONFIG = "test/sample_config.toml"


def _clean_sample_data():
    if os.path.isfile(UNEXISTING_CONFIG_PATH):
        os.remove(UNEXISTING_CONFIG_PATH)
    assert not os.path.isfile(UNEXISTING_CONFIG_PATH)


def test_can_create_a_default_configuration_file():
    _clean_sample_data()
    _config.read(UNEXISTING_CONFIG_PATH)
    assert os.path.isfile(UNEXISTING_CONFIG_PATH)


def test_can_read_sample_config():
    result = _config.read(EXISTING_SAMPLE_CONFIG)
    assert isinstance(result, _config.Configuration)
    assert len(result.directorios) == 2


def test_UserDir_accepts_valid_filter():
    _config.UserDir(
        **{
            "in": f"dir1",
            "out": f"dir1_o",
            "actions": [_config.Action.NONE],
            "filter": "*.jpg",
        }
    )


def test_UserDir_rejects_invalid_filter():
    with pytest.raises(pydantic.ValidationError):
        _config.UserDir(
            **{
                "in": f"dir1",
                "out": f"dir1_o",
                "action": _config.Action.NONE,
                "filter": "blablabla",
            }
        )
