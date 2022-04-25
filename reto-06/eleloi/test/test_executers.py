import shutil
import os

import _executers
import _config

SAMPLE_DIR = "sample_data"

none_dir = _config.UserDir(
    **{
        "in": f"{SAMPLE_DIR}/dir1",
        "out": f"{SAMPLE_DIR}/dir1_o",
        "action": _config.Action.NONE,
    }
)
copy_dir = _config.UserDir(
    **{
        "in": f"{SAMPLE_DIR}/dir2",
        "out": f"{SAMPLE_DIR}/dir2_o",
        "action": _config.Action.COPY,
    }
)
move_dir = _config.UserDir(
    **{
        "in": f"{SAMPLE_DIR}/dir3",
        "out": f"{SAMPLE_DIR}/dir3_o",
        "action": _config.Action.MOVE,
    }
)


def _clean_sample_data_dir():
    shutil.rmtree(SAMPLE_DIR)
    assert not os.path.isdir(SAMPLE_DIR)


def _create_folders_if_dont_exist(sample_data: _config.UserDir):
    _executers._create_folders_if_dont_exists(
        [sample_data.in_, sample_data.out]
    )


def _fill_with_sample_files(directory: str, num_files: int) -> None:
    for filename in [f"sample{x}.txt" for x in range(0, num_files)]:
        with open(os.path.join(directory, filename), "w") as f:
            f.write("sample data")


def test_none_executer_creates_directory():
    _clean_sample_data_dir()
    executer = _executers.none
    executer(none_dir.in_, none_dir.out)
    assert os.path.isdir(SAMPLE_DIR)


def test_copy_executer_copy_all_files():
    _clean_sample_data_dir()
    _create_folders_if_dont_exist(copy_dir)
    _fill_with_sample_files(copy_dir.in_, 3)
    assert len(os.listdir(copy_dir.in_)) == 3
    assert len(os.listdir(copy_dir.out)) == 0
    executer = _executers.copy
    executer(copy_dir.in_, copy_dir.out)
    assert len(os.listdir(copy_dir.in_)) == 3
    assert len(os.listdir(copy_dir.out)) == 3


def test_copy_executer_copy_existing_files():
    _clean_sample_data_dir()
    _create_folders_if_dont_exist(copy_dir)
    _fill_with_sample_files(copy_dir.in_, 3)
    _fill_with_sample_files(copy_dir.out, 1)
    assert len(os.listdir(copy_dir.in_)) == 3
    assert len(os.listdir(copy_dir.out)) == 1
    executer = _executers.copy
    executer(copy_dir.in_, copy_dir.out)
    assert len(os.listdir(copy_dir.in_)) == 3
    assert len(os.listdir(copy_dir.out)) == 3


def test_move_executer_all_files():
    _clean_sample_data_dir()
    _create_folders_if_dont_exist(move_dir)
    _fill_with_sample_files(move_dir.in_, 3)
    assert len(os.listdir(move_dir.in_)) == 3
    assert len(os.listdir(move_dir.out)) == 0
    executer = _executers.move
    executer(move_dir.in_, move_dir.out)
    assert len(os.listdir(move_dir.in_)) == 0
    assert len(os.listdir(move_dir.out)) == 3


def test_copy_executer_move_existing_files():
    _clean_sample_data_dir()
    _create_folders_if_dont_exist(move_dir)
    _fill_with_sample_files(move_dir.in_, 3)
    _fill_with_sample_files(move_dir.out, 1)
    assert len(os.listdir(move_dir.in_)) == 3
    assert len(os.listdir(move_dir.out)) == 1
    executer = _executers.move
    executer(move_dir.in_, move_dir.out)
    assert len(os.listdir(move_dir.in_)) == 0
    assert len(os.listdir(move_dir.out)) == 3
