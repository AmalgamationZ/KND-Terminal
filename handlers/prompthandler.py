import os
import shlex
import shutil
import sys

from . import texthandler as th
from . import validation as v
from . import conversion as c
from . import commands as com


def print_full_help(valid_commands, name=None):
    th.print_text("**************************************", wrap=False)

    if name is not None:
        th.print_text("Unknown command: {}".format(name), wrap=False)
    
    th.print_text("List of Commands:", wrap=False)

    for command in valid_commands:
        descrip = valid_commands[command]["description"]
        usage = valid_commands[command]["usage"]

        th.print_text("> {}".format(command))
        th.print_text("description: {}".format(descrip))
        th.print_text("usage: {}".format(usage))
    
    th.print_text("**************************************", wrap=False) 


def print_command_help(command, valid_commands):
    pre_help = "Please ensure you have entered all arguments correctly."
    help = "{} | usage: {} | description: {}".format(
        command,
        valid_commands[command]["usage"],
        valid_commands[command]["description"]
    )
    th.print_text(pre_help, wrap=False)
    th.print_text(help, wrap=False)


def create_prompt(prompt_text):
    output = input(prompt_text)
    return output


def parse_command(command, data_dict):
    args = shlex.split(command)

    name = args[0]

    # list of valid commands and their associated
    # functions and validation functions
    valid_commands = {
        "quit": {
            "func": com.exit_program,
            "valid_func": v.validate_quit,
            "usage": "quit",
            "description": "Quits the application",
            "needs_args": False},
        "exit": {
            "func": com.exit_program,
            "valid_func": v.validate_exit,
            "usage": "exit",
            "description": "Quits the application",
            "needs_args": False},
        "access": {
            "func": com.access_file,
            "valid_func": v.validate_access,
            "usage": "access [file path in quotes]",
            "description": "Accesses a file, given a file name",
            "needs_args": True},
        "list": {
            "func": com.list_files,
            "valid_func": v.validate_list,
            "usage": "list [folder path in quotes, \".\" for current folder]",
            "description": "Lists all files and folders inside given folder",
            "needs_args": True},
        "resize": {
            "func": com.resize,
            "valid_func": v.validate_resize,
            "usage": "resize",
            "description": "Resizes terminal text so that it matches terminal window's width",
            "needs_args": True},
        "encode": {
            "func": c.encode_file,
            "valid_func": v.validate_access,
            "usage": "encode [file path in quotes]",
            "description": "Encodes a file from UTF-8 text to incomprhensible bytes",
            "needs_args": True},
        "decode": {
            "func": c.decode_file,
            "valid_func": v.validate_access,
            "usage": "decode [file path in quotes]",
            "description": "Decodes a file from incomprhensible bytes to UTF-8 text",
            "needs_args": True},
        "status": {
            "func": com.view_status,
            "valid_func": v.validate_status,
            "usage": "status [search term in quotes]",
            "description": "Returns the status of a search term",
            "needs_args": True}
    }

    if name == "help":
        print_full_help(valid_commands, name=None)
        return

    # if the command doesn't exist, remind user of
    # existing commands and return to main prompt
    if name not in valid_commands:
        print_full_help(valid_commands, name=name)
        return

    if valid_commands[name]["valid_func"](args):
        data_dict["args"] = args
        valid_commands[name]["func"](data_dict)
        data_dict["args"] = None
    else:
        print_command_help(name, valid_commands)
