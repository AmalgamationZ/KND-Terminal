import shutil
import os
import time
from sys import stderr

from . import texthandler as th
from . import prompthandler as ph
from . import validation as v
from . import commands as c


def start():
    open_prompt = """
    --------------------------------------------
    Type opening text file name and press ENTER.
    If you press ENTER without text, the
    program will automatically assume
    it will use the file "o.txt" as the opening
    text.

    Alternatively, type "quit" or "exit" (case-
    sensitive) to stop the program.
    --------------------------------------------
    > """

    close_prompt = """
    --------------------------------------------
    Type closing text file name and press ENTER.
    If you press ENTER without text, the
    program will automatically assume
    it will use the file "c.txt" as the opening
    text.

    Alternatively, type "quit" or "exit" (case-
    sensitive) to stop the program.
    --------------------------------------------
    > """

    prompt_prompt = """
    --------------------------------------------
    Type prompt text file name and press ENTER.
    If you press ENTER without text, the
    program will automatically assume
    it will use the file "p.txt" as the opening
    text.

    Alternatively, type "quit" or "exit" (case-
    sensitive) to stop the program.
    --------------------------------------------
    > """

    status_prompt = """
    --------------------------------------------
    Type status text file name and press ENTER.
    If you press ENTER without text, the
    program will automatically assume
    it will use the file "s.txt" as the opening
    text.

    Alternatively, type "quit" or "exit" (case-
    sensitive) to stop the program.
    --------------------------------------------
    > """

    file_error_msg = """
    ERROR! File not found or is not a singular file.
    Please ensure that the file exists, is inside
    the same directory as the main application,
    or is a singular file (i.e. not a folder).

    If you left the input empty, then ensure the
    default "o.txt", "p.txt", and/or "c.txt" files
    are in the same diretory as the application
    and type again.

    Press ENTER to confirm that you have read this.
    """

    file_success_msg = """
    --------------------------------------------
    SUCCESS!

    NOW LOADING FULL PROMPT...
    --------------------------------------------
    """

    try:
        # first prompt for files (loops
        # until existing files are found)
        while True:
            # prompts user for opening text file,
            # handles default inputs, or exits
            # if prompt is "quit" or "exit"
            opening = ph.create_prompt(open_prompt)

            if not opening:
                opening = "defaults/o.txt"
            
            if v.check_if_exit(opening):
                c.exit_program(None)

            # prompts user for closing text file,
            # handles default inputs, or exits
            # if prompt is "quit" or "exit"
            closing = ph.create_prompt(close_prompt)

            if not closing:
                closing = "defaults/c.txt"

            if v.check_if_exit(closing):
                c.exit_program(None)

            # prompts user for prompt text file,
            # handles default inputs, or exits
            # if prompt is "quit" or "exit"
            prompt = ph.create_prompt(prompt_prompt)

            if not prompt:
                prompt = "defaults/p.txt"

            if v.check_if_exit(prompt):
                c.exit_program(None)
            
            # prompts user for status text file,
            # handles default inputs, or exits
            # if prompt is "quit" or "exit"
            status = ph.create_prompt(status_prompt)

            if not status:
                status = "defaults/s.txt"

            if v.check_if_exit(status):
                c.exit_program(None)
            
            # if file does not exist, is not in the same folder,
            # or is not a file (i.e. is a folder), then the program
            # will insist the user try again.
            if not v.validate_file(opening):
                ph.create_prompt(file_error_msg)
                continue

            if not v.validate_file(closing):
                ph.create_prompt(file_error_msg)
                continue
            
            if not v.validate_file(prompt):
                ph.create_prompt(file_error_msg)
                continue
            
            if not v.validate_file(status):
                ph.create_prompt(file_error_msg)
                continue
            
            if not os.path.exists("saves") or not os.path.isdir("saves"):
                os.mkdir("saves")
            
            print(file_success_msg)

            break

        # initially gets dimensions of terminal
        cols, __ = shutil.get_terminal_size()

        # places "cols" key inside dictionary
        # for reference, as well as an "args"
        # key for use in functions
        data_dict = {"cols": cols, "args": None}

        # generates status dict and saves it
        # to data_dict
        data_dict["status"] = th.make_status_dict(status)

        # prints opening crawl
        th.print_from_file(opening, data_dict["cols"], delay=0.1)

        # enters user prompt for reading a file
        while True:
            # prints the prompt text
            th.print_from_file(prompt, data_dict["cols"])
        
            try:
                # prints the prompt cursor and
                # obtains file name
                response = ph.create_prompt("> ")

                # handles empty commands
                if v.check_if_empty(response):
                    continue
                
                # parses command
                ph.parse_command(response, data_dict)
            
            # catches any errors related to invalid arguments
            except IOError as ex:
                # notifies user of file error
                th.print_text("", cols)
                th.print_text("*** ERROR: FILE NOT FOUND. PLEASE TRY AGAIN. ***", cols)
                th.print_text("", cols)
    except Exception as e:
        print(e, file=stderr)
        ph.create_prompt("Press ENTER to confirm you read this error.")
