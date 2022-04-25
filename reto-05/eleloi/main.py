import _config
import _utils


CONFIG_PATH = "config.toml"


def main():
    config = _config.read(CONFIG_PATH)
    for path_name in [x.in_ for x in config.directorios]:
        _utils.list_jpg_files_in_dir(path_name)


if __name__ == "__main__":
    main()
