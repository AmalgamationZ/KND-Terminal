# KND-Terminal

Terminal python application inspired by consoles from
the old Cartoon Network show "Codename: KND".

## Setup/Installation
------------------

On the right side of this page, there should be a section titled "Releases". The latest version of the application - currently v00000 - should be there.

### For Windows Users:
1. 

### For Mac OS X and Linux Users:
As of now, there is a Windows download available. Currently, there are no versions for Mac OS X or Linux. This is not due to the fact that doing so is difficult; in fact, the process for making a Mac OS X or Linux executable is actually very simple with the help of PyInstaller. The unfortunate truth is, the owner of this repository (AmalgamationZ) does not have a computer on which Mac OS X is installed. Thus, any Mac users hoping to utilize this app may need to complete a few more steps:

1. Install Python 3.10.1 (the latest version of the Python language), found at this link: [https://www.python.org/downloads/release/python-3101/], following the default installation steps.
2. Install Git

## Usage
--------
### Opening the app

To open the app, simply locate the 

### *list* command

The *list* command will print all the files and directories present inside a given folder, meaning the command requires the user to put in the path to the desired folder. One of the first things that you can do is list all the files and directories (a.k.a. folders) located in the same folder as the knd_terminal.exe file. To view the contents of this folder, which will now be referred to as the current working directory, type:

> list .

It will display a list of all files and directories located inside the current working directory, which should include (by default) the folder "saves", the folder "defaults", and the knd_terminal.exe file.

Now, suppose you structured the current working directory like this, perhaps after creating some new folders:

-some-folder

---knd-terminal.exe

---saves

-----folder-1

-----folder-2

---defaults

-----folder-3

-----folder-4

(in other words, in the current working directory, you have the knd-terminal.exe file, the "saves" folder - which has two subfolders named folder-1 and folder-2 - and the "defaults" folder, which has two subfolders named folder-3 and folder-4)

In order to list the files located in saves, all you would need to do is type the following:

> list saves

However, if you wish to list the files located in folder-1, you must type:

> list saves/folder-1

This is because "folder-1" is one "level", so to say, below the current working directory.

Suppose now, for instance, you had this structure:

-some-folder

---knd-terminal.exe

---saves

-----folder-1

-------folder-2

---defaults

-----folder-3

-----folder-4

If you want to list the files located in folder-2, you must type:

> list saves/folder-1/folder-2

This is because "folder-2" is two "levels", so to say, below the current working directory.

### access command



### encode command

### decode command

### resize command

### status command