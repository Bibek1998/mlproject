import sys
'''
The sys module in Python provides various functions 
and variables that are used to manipulate different
parts of the Python runtime environment
'''
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    '''
    exec_tb is a traceback object that contains information 
    about the call stack at the point where an exception occurred.
    '''

    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in the python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exec_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message