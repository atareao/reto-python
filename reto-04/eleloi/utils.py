import os


def list_images(directory_name: str) -> None:
    if not os.path.isdir(directory_name):
        os.makedirs(directory_name)
    files_in_dir = [
        os.path.join(directory_name, x) for x in os.listdir(directory_name)
    ]
    files_in_dir = [
        os.path.basename(x) for x in files_in_dir if os.path.isfile(x)
    ]
    print(
        "\n".join(
            [
                x
                for x in files_in_dir
                if x.lower().endswith(".jpg") or x.lower().endswith(".jpeg")
            ]
        )
    )
