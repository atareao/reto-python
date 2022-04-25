import os

import _config


def _jpg_files_in_dir(directory_name: str) -> list[str]:
    files_in_dir = [
        os.path.join(directory_name, x) for x in os.listdir(directory_name)
    ]
    files_in_dir = [
        os.path.basename(x) for x in files_in_dir if os.path.isfile(x)
    ]
    return [
        x
        for x in files_in_dir
        if x.lower().endswith(".jpg") or x.lower().endswith(".jpeg")
    ]


def main():
    config = _config.read()
    jpg_files = _jpg_files_in_dir(config.directorio)

    print("\n".join(jpg_files))


if __name__ == "__main__":
    main()
