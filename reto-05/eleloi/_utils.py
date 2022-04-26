import os
import pathlib


def list_jpg_files_in_dir(directory: str) -> None:

    path = pathlib.Path(directory)
    path.mkdir(parents=True, exist_ok=True)

    files_in_dir = [os.path.join(directory, x) for x in os.listdir(directory)]
    files_in_dir = [
        os.path.basename(x) for x in files_in_dir if os.path.isfile(x)
    ]
    jpg_files_in_dir = [
        x
        for x in files_in_dir
        if x.lower().endswith(".jpg") or x.lower().endswith(".jpeg")
    ]

    print("\n".join(jpg_files_in_dir))
