import os

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
