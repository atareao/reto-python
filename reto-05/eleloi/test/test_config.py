import os

import _config

SAMPLE_CONFIG_PATH = "test_config.toml"


def clean_sample_data():
    if os.path.isfile(SAMPLE_CONFIG_PATH):
        os.remove(SAMPLE_CONFIG_PATH)
    assert not os.path.isfile(SAMPLE_CONFIG_PATH)


def test_can_create_default_configuration():
    clean_sample_data()
    _config.read(SAMPLE_CONFIG_PATH)
    assert os.path.isfile(SAMPLE_CONFIG_PATH)

