from google.genai import types
from google.genai.types import FunctionCall
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if isinstance(function_call_part, FunctionCall):
        func_name = function_call_part.name
        args = function_call_part.args or {}
        args["working_directory"] = "./calculator"
        if verbose:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(f" - Calling function: {function_call_part.name}")


    if func_name in function_map:
        function_to_run = function_map[func_name]
        result = function_to_run(**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"result": result},
                )
            ],
        )
    elif func_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )



