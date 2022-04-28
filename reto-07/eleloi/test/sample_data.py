import _config

SAMPLE_DIR = "sample_data"

none_dir = _config.UserDir(
    **{
        "in": f"{SAMPLE_DIR}/dir1",
        "out": f"{SAMPLE_DIR}/dir1_o",
        "actions": [_config.Action.NONE],
        "filter": "*.jpg",
    }
)


copy_dir = _config.UserDir(
    **{
        "in": f"{SAMPLE_DIR}/dir2",
        "out": f"{SAMPLE_DIR}/dir2_o",
        "actions": {_config.Action.COPY},
        "filter": "*.jpg",
    }
)
move_dir = _config.UserDir(
    **{
        "in": f"{SAMPLE_DIR}/dir3",
        "out": f"{SAMPLE_DIR}/dir3_o",
        "actions": {_config.Action.MOVE},
        "filter": "*.jpg",
    }
)
