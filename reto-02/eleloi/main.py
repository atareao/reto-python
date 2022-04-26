from pathlib import Path
import os

DOWNLOAD_FOLDER_NAME = "downloads"


def _get_user_download_directory() -> str:
    home_dir = str(Path.home())
    download_dir = os.path.join(home_dir, DOWNLOAD_FOLDER_NAME)

    if download_dir:
        return download_dir

    raise Exception("Could not find user download directory")


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


def _str_list_formatter(items: list[str]) -> list[str]:
    _has_numbers = lambda x: any(char in x for char in "0123456789")

    formatted_items: list[str] = []
    for idx, item in enumerate(items):
        if _has_numbers(item):
            item = item.lower()
        else:
            item = item.upper()
        if idx % 2 == 0:
            item = f"=> {item}"

        item = f"{idx} {item}"
        formatted_items.append(item)

    return formatted_items


def main():
    user_download_dir = _get_user_download_directory()
    jpeg_files_in_dir = _jpg_files_in_dir(user_download_dir)
    file_list_formatted = _str_list_formatter(jpeg_files_in_dir)
    print(
        "{dirname}\n\n{files}".format(
            dirname=user_download_dir, files="\n".join(file_list_formatted)
        )
    )


if __name__ == "__main__":
    main()
