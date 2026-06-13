import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        file_info = []
        for name in os.listdir(target_dir):
            path = os.path.join(target_dir, name)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            file_info.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(file_info)
    except Exception as e:
        return f"Error listing files: {e}"
