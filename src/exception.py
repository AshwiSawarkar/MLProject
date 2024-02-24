import logging
import sys  # The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
from src.logger import logging
# def error_message_details(error_details:sys):
#     _,_,exc_tb=error_details.exc_info()
#     file_name=exc_tb.terrorb_frame.f_code.co_filename
#     script_name=file_name
#     line_number=1
#     error_message=error
#     error_messsage="Error occurred in script [{0}] line number [{1}] error [{2}]".format(script_name, line_number, error_message)

#     file_name,exc_tb.tb_lineno,str(error)

#     return error_messsage

def error_message_details(exception):
    # Extract traceback details
    exc_type, exc_value, exc_traceback = traceback.exc_info()
    # Get the last traceback object
    tb = traceback.extract_tb(exc_traceback)[-1]
    file_name = tb.filename
    line_number = tb.lineno
    error_message = str(exc_value)
    formatted_error_message = "Error occurred in script [{}] line number [{}] error [{}]".format(file_name, line_number, error_message)
    
    return formatted_error_message

class CustomException(Exception):
    def __init__(self,error_messsage,error_detail:None):
        super().__init__(error_messsage)
        if error_detail is not None and not isinstance(error_detail, list):
            error_detail = [error_detail]
        self.error_messsage=error_message_details(error_messsage,error_details=error_detail)

    def __str__(self):
        return self.error_messsage

if __name__=="__main__":
    try:
        1/0
    except Exception as e:
        raise CustomException(e,sys)
    