import logging
import sys  # The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_messsage="Error occured in a script [{0}] line number [{1}] error [{2}]".format()
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
        logging.info("Catching the exception for devid eby zero")
        raise CustomeException(e,sys)
    