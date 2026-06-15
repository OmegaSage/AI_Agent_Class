import os
import subprocess
from operator import not_
from sys import stderr


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_dir is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_dir]
        if args:
            command.extend(args)
        result = subprocess.run(
            command, text=True, capture_output=True, timeout=30, cwd=working_dir_abs
        )
        output: str = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
            print(output, "TEST1")
        if result.stderr == None:
            if result.stdout == None:
                output += "No output produced"
                print(output, "TEST2")
            elif result.stdout != None:
                output += f"STDOUT: {result.stdout}"
                print(output, "TEST3")
        elif result.stderr != None:
            output += f"STDERR: {result.stderr}"
            print(output, "TEST4")
        return output

    except subprocess.CalledProcessError as t:
        return f"Process exited with code {t.returncode}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
