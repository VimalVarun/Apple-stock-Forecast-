import sys
import logging

def error_message_detail(error, error_details: sys):
    """Function to extract error details including filename and line number."""
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}] at line [{1}] with message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """Custom exception class to capture detailed error messages."""
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("error.log"), logging.StreamHandler()]
    )

    try:
        a = 1 / 0
    except Exception as e:
        error_msg = CustomException(e, sys)
        logging.error(error_msg)  # Logs the error without traceback clutter
