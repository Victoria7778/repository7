def print_to_console(text):
    """Prints text to the console"""
    print(text)

def write_to_file(text, filename="output.txt"):
    """Writes text to a file using Python's built-in capabilities"""
    with open(filename, 'w') as file:
        file.write(text)
