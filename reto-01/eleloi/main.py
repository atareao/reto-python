from pathlib import Path
import os

DOWNLOAD_FOLDER_NAME = "downloads"


def _get_user_download_directory() -> str:
    home_dir = str(Path.home())
    download_dir = os.path.join(home_dir, DOWNLOAD_FOLDER_NAME)

    if download_dir:
        return download_dir

    raise Exception("Could not find user download directory")


def main():
    download_dir = _get_user_download_directory()
    files_in_download_dir = [
        os.path.join(download_dir, x) for x in os.listdir(download_dir)
    ]
    files_in_download_dir = [
        os.path.basename(x) for x in files_in_download_dir if os.path.isfile(x)
    ]

    print(
        "Directorio: {dir}\n\n{files}".format(
            dir=download_dir, files="\n".join(files_in_download_dir)
        )
    )


if __name__ == "__main__":
    main()
