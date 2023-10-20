import json

class CustomCliException(Exception):
    '''
    A class to represent a custom exception raised by the CLI app

    This class defines a custom exception with an error code and corresponding error message

    Args
        error_code (int): The error code of the exception
        error_message (str): The error message which describes the exception
    '''

    def __init__(self, error_code: int, error_message: str):
        self.error_code = error_code
        self.error_message = error_message

# A dictionary tp map cli return codes to description
cli_return_codes = {
    0: "SUCCESS",
    1: "INTERNAL ERROR",
    2: "INVALID JSON FORMAT",
    3: "MISSING OPTION"
}

# Convert any exception to CustomCliException for further error handling
def error_converter(exception):
    if not isinstance(exception, CustomCliException):
        # Centralized error handling 
        if isinstance(exception, json.JSONDecodeError):
            exception = CustomCliException(2, "Please make sure your JSON input is correctly formatted and all braces and quotes are balanced.")
        # elif: Add all known exceptions here
        else:
            exception = CustomCliException(1, "An unknown issue occurred while executing your command.")
    return exception

def error_logger(exception):
    custom_cli_exception: CustomCliException = error_converter(exception)
    return f"Command Error {custom_cli_exception.error_code} - {cli_return_codes[custom_cli_exception.error_code]}\n{custom_cli_exception.error_message}"
        
    