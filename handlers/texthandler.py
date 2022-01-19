import time
import textwrap
import csv

from . import prompthandler as ph
from . import validation as v


def print_text(message, cols=0, count=1, delay=0, wrap=True):
    for _ in range(0, count):
        if message == "":
            print()

            time.sleep(delay)

            continue

        if wrap == True:
            lines = textwrap.wrap(message, replace_whitespace=False)

            for line in lines:
                print(line.center(cols))
                
        else:
            print(message)
        
        time.sleep(delay)


def print_text_list(messages, cols, text_count=1, count=1, text_delay=0, delay=0,
print_newline=False, enter=False, wrap=True):
    for _ in range(0, count):
        for message in messages:
            print_text(message, cols,
            count=text_count,
            delay=text_delay,
            wrap=wrap)

            if print_newline:
                print()
            
            if enter == True and message != "":
                response = ph.create_prompt("> ")

                if v.check_if_exit(response):
                    break
                
                if response == 'continue':
                    enter = False

            time.sleep(delay)


def print_from_file(input_file, cols, delay=0, enter=False, wrap=True):
    with open(input_file, encoding='utf8') as file:
        contents = file.read()

        messages = contents.split("\n")
        
        print_text_list(messages, cols, delay=delay, enter=enter, wrap=wrap)


def make_status_dict(file):
    status = {}

    # look for directory "defaults/s.txt"
    with open(file, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue

            reader = csv.reader([line], skipinitialspace=True)

            data = list(reader)[0]

            # if the split doesn't result in a two-item list,
            # then skip
            if len(data) != 2:
                continue

            status[data[0]] = data[1]
    

    return status