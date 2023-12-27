from pathlib import Path

def write_file(file_name, file_content):
    file_name = Path(file_name).with_suffix('.txt')  # Convert to Path object and add .txt extension
    with open(file_name, "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = Path(file_name).with_suffix('.txt')  # Convert to Path object and add .txt extension
    with open(file_name, "a") as file:
        file.write("\n" + append_content)

def read_file(file_name):
    file_name = Path(file_name).with_suffix('.txt')  # Convert to Path object and add .txt extension
    with open(file_name, "r") as file:
        content = file.read()
    return content
