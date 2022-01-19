import shutil
import argparse
import os
from sys import stderr

from . import texthandler as th
from . import prompthandler as ph

try:
    parser = argparse.ArgumentParser(description="Interactive text reader")

    parser.add_argument('opening', metavar='opening',
                        help='name of file that contains opening text')
    parser.add_argument('closing', metavar='closing',
                        help='name of file that contains closing text')
    parser.add_argument('prompt', metavar='prompt',
                        help='name of file that contains prompt text')
    parser.add_argument('-pad', metavar='pad', type=int,
                        help='amount of newlines you wish to create' \
                        ' when starting up')
    parser.add_argument('-sec', metavar='sec', type=int,
                        help='seconds in countdown')
    parser.add_argument('-delay', metavar='delay', type=int,
                        help='delay for each text to pop up')

    args = parser.parse_args()

    pad = args.pad
    sec = args.sec
    delay = args.delay
    opening = args.opening
    closing = args.closing
    prompt = args.prompt

    if pad is None:
        pad = 0
    
    if sec is None:
        sec = 0

    if delay is None:
        delay = 0
    
    # gets dimensions of terminal
    cols, rows = shutil.get_terminal_size()

    # prints linebreaks (to hide actual terminal)
    th.print_text("", cols, count=pad)

    # prints warning message to prepare recording device
    th.print_text("WARNING! GET RECORDING DEVICE READY," \
        " COUNTDOWN BEGINNING!", cols)

    # centers countdown
    list_of_nums = []

    # creates countdown numbers
    for i in range(sec, 0, -1):
        list_of_nums.append(str(i))

    th.print_text_list(list_of_nums, cols, delay=1)

    # prints linebreaks (to hide warning)
    th.print_text("", cols, count=pad)

    # prints opening animation
    th.print_from_file(opening, cols, delay=delay)


    # handles output of prompt
    while True:
        th.print_from_file(prompt, cols)

        response = ph.create_prompt("> ")

        if response == "quit" or response == "exit":
            # prints closing animation
            th.print_from_file(closing, cols, delay=delay)
            break
        
        try:
            th.print_text("LOADING...", cols, delay=delay)

            if os.path.isfile(response):
                th.print_text("", cols)
                th.print_text("---------------------------", cols)
                th.print_text("FILE LOADED! PRESS 'ENTER' TO CONTINUE." \
                " ALTERNATIVELY, TYPE 'quit' OR 'exit' TO STOP READING THE FILE", cols)
                th.print_text("OR TYPE 'continue' TO OUTPUT REST OF FILE.", cols)
                th.print_text("---------------------------", cols)
                th.print_text("", cols)
                th.print_from_file(response, cols, enter=True)
            else:
                raise IOError
        except IOError as ex:
            th.print_text("ERROR: FILE NOT FOUND. PLEASE TRY AGAIN.", cols, delay=delay)
        except Exception as e:
            th.print_text("UNKNOWN ERROR. PLEASE TRY AGAIN.", cols, delay=delay)


except Exception as e:
    print(e, file=stderr)