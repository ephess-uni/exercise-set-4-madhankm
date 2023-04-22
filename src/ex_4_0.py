""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    with open(logfile, 'r') as fp:
    listval=[]
        lines = fp.readlines()
        for row in lines:   
         if "Shutdown initiated" in row:
            listval.append(row.replace("\n",""))
    return listval

# >>>> The code below will call your function and print the results
if _name_ == "_main_":
    print(f"{get_shutdown_events(FILENAME)=}")
