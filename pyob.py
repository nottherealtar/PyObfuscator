import os
import sys
import random
import string

ERROR = "\x1b[38;5;255m[\x1b[31m-\x1b[38;5;255m]"
SUCCESS = "\x1b[38;5;255m[\x1b[32m+\x1b[38;5;255m]"

def set_terminal_properties():
    os.system("mode 80,18 & title goinggone & powershell $H=get-host;$W=$H.ui.rawui;$B=$W.buffersize;$B.width=80;$B.height=9999;$W.buffersize=$B;")

def exit_program():
    input("Press any key to continue...")
    sys.exit()

def generate_dummy_code():
    func_name = "".join(random.choices(string.ascii_lowercase, k=5))
    var_name = "".join(random.choices(string.ascii_lowercase, k=5))
    dummy_code = f'''
import random

class DummyClass_{func_name.capitalize()}:
    def __init__(self, {var_name}):
        self.{var_name} = {var_name}

    def dummy_method(self):
        data = [random.randint(0, 100) for _ in range(10)]
        return sum(data) / len(data)

def dummy_function_{func_name}({var_name}):
    dummy_obj = DummyClass_{func_name.capitalize()}({var_name})
    result = dummy_obj.dummy_method()
    print(f'Dummy result: {{result}}')

dummy_variable_{var_name} = dummy_function_{func_name}(random.randint(0, 100))
'''
    return dummy_code

def intersperse_dummy_code(original_code):
    dummy_code_start = '\n'.join([generate_dummy_code() for _ in range(15)])  # Generating 15 dummy code blocks
    dummy_code_end = '\n'.join([generate_dummy_code() for _ in range(15)])  # Generating 15 dummy code blocks
    obfuscated_code = f"{dummy_code_start}\n{original_code}\n{dummy_code_end}"
    return obfuscated_code

def main():
    set_terminal_properties()

    if not os.path.exists("main.py"):
        print(f"{ERROR} Please locate file main.py\n")
        exit_program()

    with open("main.py", "r") as file:
        original_code = file.read()

    obfuscated_code = intersperse_dummy_code(original_code)

    with open("final.py", "w") as file:
        file.write(obfuscated_code)

    print(f"{SUCCESS} Obfuscation complete. Obfuscated code saved as final.py\n")
    exit_program()

if __name__ == "__main__":
    main()
