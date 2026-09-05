import os

# Example of insecure code (Command Injection risk)
def run_user_command(user_input):
    # DANGER: Executing unsanitized user input directly in shell
    os.system("echo " + user_input)

user_data = "hello"
run_user_command(user_data)