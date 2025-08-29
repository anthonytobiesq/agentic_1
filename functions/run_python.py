import os
import subprocess
from google import genai
from google.genai import types  # <- correct for google-genai



def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(['uv', 'run', file_path, *args], cwd=abs_working_dir, capture_output=True, text=True,  timeout=30)

        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()

        if completed_process.returncode != 0:
            msg = f"Process exited with code {completed_process.returncode}"
            if stderr:
                msg += f"\nSTDERR:\n{stderr}"
            return msg
        if not stdout and not stderr:
            # Case: no output at all
            return "No output produced."
        elif not stdout:
            # Case: only stderr
            return f"STDERR:\n{stderr}"
        elif not stderr:
            # Case: only stdout
            return f"STDOUT:\n{stdout}"
        else:
            # Case: both present
            return (
                f"STDOUT:\n{stdout}\n"
                f"STDERR:\n{stderr}"
            )
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
