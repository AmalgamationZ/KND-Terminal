import os
import time


class TerminalParseError(Exception):
    pass


def check_if_exists(file_name):
    return os.path.exists(file_name)


def check_if_file(file_name):
    return os.path.isfile(file_name)


def check_if_empty(prompt_text):
    if prompt_text == "":
        return True


def validate_file(file_name):
    if not check_if_exists(file_name):
        return False

    if not check_if_file(file_name):
        return False
    
    return True


def check_if_exit(prompt_text):
    prompts = ["quit", "exit"]

    if prompt_text in prompts:
        return True


def check_if_resize(prompt_text):
    if prompt_text == "resize":
        return True


def check_if_clear(prompt_text):
    if prompt_text == "clear":
        return True


def validate_quit(args=None):
    return True


def validate_exit(args=None):
    return True


def validate_access(args=None):
    if args == None:
        return False

    if len(args) != 2:
        return False
    
    return validate_file(args[1])


def validate_status(args=None):
    if args == None:
        return False

    if len(args) != 2:
        return False

    return True

def validate_list(args=None):
    if args == None:
        return False

    if len(args) != 2:
        return False
    
    path = args[1]

    return os.path.isdir(path)


def validate_resize(args=None):
    return True
