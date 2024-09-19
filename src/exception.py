import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def error_message_details(error: Exception) -> str:
    _, _, exc_tb = sys.exc_info()  # Get exception details
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"ERROR occurred in script [{file_name}] line number [{line_number}] error message [{error}]"

class CustomException(Exception):
    def __init__(self, error: Exception):
        self.error_message = error_message_details(error)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        logging.info("Divide by zero error")
        raise CustomException(e) from e
