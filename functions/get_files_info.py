import os
from google import genai
from google.genai import types  # <- correct for google-genai


        # working_directory is the pwd
        # directory is relative path within the working_directory
        # create full path
        #if the absolute path to the directory is outside the working_directory, return a string error message:
        #if the directory argument is not a directory, again, return an error string: f'Error: "{directory}" is not a directory'
        #Build and return a string representing the contents of the directory. It should use this format:
        #if any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix error strings with "Error:".
        #create tests to debug function


def get_files_info(working_directory, directory="."):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(abs_working_directory, directory))

        # Containment check
        if os.path.commonpath([abs_working_directory, full_path]) != abs_working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        lines = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)
            lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

    except Exception as e:
        return f"Error: {str(e)}"

    return "\n".join(lines)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
