############### typer ##############
import os
import cmd_styling as style

help_menu_strings = """
-cls  .... clears screen
-quit .... quit the application
-help .... prints this help menu"""

if __name__ == "__main__":
    exit()

def initialise(message, help_cmds=""):
    global MAIN_HELP_MENU
    MAIN_HELP_MENU = help_cmds

    print(message)

# Returns an user input
def get_input(question="", header='>>', cmd_marker='-'):
    user_input = input(f"{header} {question}")

    # Detects command input
    if len(user_input) >= 1 and user_input[0] == '-':
        is_command = execute_sys_cmd(user_input[1:])

        if is_command:
            return '' # if is a system commands returns a blank string
    

    return user_input

def execute_sys_cmd(user_input):
    sys_commands = ('cls', 'quit', 'help')

    if user_input in sys_commands: # If is a system commands executes a True return
        if user_input == 'cls':
            os.system('cls')
        elif user_input == 'quit':
            exit()
        elif user_input == 'help':
            print(style.ansi_fgcolour['yellow'] + help_menu_strings)
            print(f"{MAIN_HELP_MENU}{style.ansi_fgcolour['white']}\n")
        
        return True
    
    return False

def colour_print(text, colour):
    pass
