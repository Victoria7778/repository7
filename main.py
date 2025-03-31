from app.io.input import input_from_console, input_from_file, input_from_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    console_text = input_from_console()
    filename = "data/file1.txt"
    file_text = input_from_file(filename)
    pandas_filename = "data/file1.csv"
    pandas_text = input_from_file_pandas(pandas_filename)
    print_to_console(console_text)
    print_to_console(file_text)
    print_to_console(pandas_text)

    write_to_file(console_text, "data/console_output.txt")
    write_to_file(file_text, "data/file_output.txt")
    write_to_file(pandas_text, "data/pandas_output.txt")

if __name__ == "__main__":
    main()
