import shutil
import sys
import os

from . import texthandler as th
from . import validation as v


def resize(data_dict=None):
    data_dict["cols"], __= shutil.get_terminal_size()


def exit_program(data_dict=None):
    sys.exit(0)


def encode_file(data_dict=None):
    pass


def list_files(data_dict=None):
    path = data_dict["args"][1]
    cols = data_dict["cols"]
    files = os.listdir("./{}".format(path))

    th.print_text("=== LIST OF FILES AND FOLDERS ===", cols)
    
    for f in files:
        th.print_text("-- {} --".format(f), cols)


def access_file(data_dict=None):
    # gets file name from args
    file = data_dict["args"][1]
    cols = data_dict["cols"]

    # prints placeholder loading screen,
    # with short 1-second delay for
    # appearance of loading time
    th.print_text("===== LOADING =====", cols, delay=1)

    if v.validate_file(file):
        # prints instructions on using the file reader
        th.print_text("", cols)
        th.print_text("---------------------------", cols)
        th.print_text("FILE LOADED! PRESS 'ENTER' TO CONTINUE." \
        " ALTERNATIVELY, TYPE 'quit' OR 'exit' TO STOP READING THE FILE", cols)
        th.print_text("OR TYPE 'continue' TO OUTPUT REST OF FILE.", cols)
        th.print_text("---------------------------", cols)
        th.print_text("", cols)
        th.print_from_file(file, cols, enter=True)
    else:
        raise IOError


def view_status(data_dict=None):
    # gets search term from args
    term = data_dict["args"][1]

    # lowercases terms
    term = term.lower()

    status_dict = data_dict["status"]
    cols = data_dict["cols"]

    if term in status_dict:
        th.print_text("== {} ==".format(status_dict[term]), cols)
    else:
        th.print_text("== NO DATA, PLEASE ENTER ANOTHER TERM ==", cols)
