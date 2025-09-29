import sys
import logging

def error_message_detail(error:Exception,error_detail:sys):
    """
    Logs error in a more readable format

    """

    exc_type,exc_value,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno

    error_message=f"Error occured in python Script : [{file_name}] at line [{line_number}] : {str(error)}"

    logging.error(error_message)
    return error_message

class MyException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self)->str:

        """
        Returns the string representation of the error message.
        """
        return self.error_message

