import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )
    if valid_target_dir is False:
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
    elif os.path.isdir(directory) is False:
        print(f'Error: "{directory}" is not a directory')
    elif os.path.isdir(directory):
        print(f'Success: "{directory}" is within the working directory')
