import subprocess
import os.path


def run_python_file(working_directory, file_path):
    cwd_abs_path = os.path.abspath(working_directory)
    file_abs_path = cwd_abs_path
    if file_path:
        file_abs_path = os.path.abspath(os.path.join(cwd_abs_path, file_path))
    if not file_abs_path.startswith(cwd_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside of the permitted working directory'

    is_file = os.path.isfile(file_abs_path)
    if not is_file:
        return f'Error: File "{file_path}" not found.'
    if file_path.split(".")[-1] != "py":
        return f'Error: "{file_path} is not a Python file.'
    try:
        #run the python file
        process_result = subprocess.run(['python3', file_abs_path], cwd=cwd_abs_path, capture_output=True, timeout=30)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    output = [f"STDOUT: {process_result.stdout}\n"]
    output.append(f"STDERR: {process_result.stderr}\n")
    if process_result.returncode != 0:
        output.append(f"Process exited with code {process_result.returncode}")
    if not process_result:
        output.append("No output produced")

    return "".join(output)

