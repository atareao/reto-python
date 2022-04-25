import os
import shutil

import _utils

SAMPLE_DIR = "test_dir"


def _delete_sample_dir():
    if os.path.isdir(SAMPLE_DIR):
        shutil.rmtree(SAMPLE_DIR)
    assert not os.path.isdir(SAMPLE_DIR)


def _create_sample_dir():
    if not os.path.isdir(SAMPLE_DIR):
        os.mkdir(SAMPLE_DIR)
    assert os.path.isdir(SAMPLE_DIR)


def test_can_create_directory_if_not_exists():
    _delete_sample_dir()
    _utils.list_jpg_files_in_dir(SAMPLE_DIR)
    assert os.path.isdir(SAMPLE_DIR)
    _delete_sample_dir()


def test_can_read_existing_directory():
    _create_sample_dir()
    _utils.list_jpg_files_in_dir(SAMPLE_DIR)
    assert os.path.isdir(SAMPLE_DIR)
    _delete_sample_dir()
