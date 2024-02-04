import logging
import sys  # The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
from src.logger import logging
def error_message_details(error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.terrorb_frame.f_code.co_filename
    script_name=file_name
    line_number=1
    error_message=error
    error_messsage="Error occurred in script [{0}] line number [{1}] error [{2}]".format(script_name, line_number, error_message)

    file_name,exc_tb.tb_lineno,str(error)

    return error_messsage


class CustomeException(Exception):
    def __init__(self,error_messsage,error_detail:sys):
        super().__init__(error_messsage)
        self.error_messsage=error_message_details(error_messsage,error_details=error_detail)

    def __str__(self):
        return self.error_messsage

if __name__=="__main__":
    try:
        1/0
    except Exception as e:
        logging.error("devide by zero erro from exception")
        raise CustomeException(e,sys)
    