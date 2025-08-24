import os
from config import MAX_CHARACTERS


def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

        # Containment check
        if os.path.commonpath([abs_working_directory, full_path]) != abs_working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, 'r') as f:
            file_content = f.read(MAX_CHARACTERS + 1)

            # Check if truncation is needed
            if len(file_content) > MAX_CHARACTERS:
                file_content = file_content[
                               :MAX_CHARACTERS] + f"\n[...File '{file_path}' truncated at {MAX_CHARACTERS} characters]"

            return file_content

    except Exception as e:
        return f"Error: {str(e)}"