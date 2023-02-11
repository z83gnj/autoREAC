# To install module use:                                           #
#       pip install keyboard                                       #


DEV = True
# Import section
import os, #keyboard
#######

# Global Variable
# Current working directory
CWD = os.getcwd()

def main_autoREACToExcel():
    
    # Inform the user about the working dir. If is not correct the sript will be broken.
    print(f"\nThe current work directory is {CWD}\n")
    print("If the working directory is not correct please press q, navigate to the correct location and restart the script!!!")
    print("To continue press any other key!")
    
    if waiting_press_key("q", "The script is finished!"): return -1
    

    # TODO: Get the .post filename form the directory

    # TODO: Collect data from .post file

    # TODO: Write data to excel table
    # TODO: Check the permissions to using the file
    # TODO: Check the existing of the file, if it exist rename to *.bak.xlsx

    pass

def waiting_press_key(key, text : str = ""):
    '''Wainting a key press and check is it the given key or not.\n
    If the key is match the the given text will be shown!
    '''
    if (keyboard.read_key() == str(key)) | (keyboard.read_key() == str(key).upper()):
        print(text)
        return True
    else: return False

main_autoREACToExcel()

if DEV:
    print("develop mode")
    print(type(keyboard.read_key()))
    
