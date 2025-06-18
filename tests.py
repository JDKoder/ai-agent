from functions.get_files_info import get_file_content, write_file, get_file_content
from functions.run_python import run_python_file


get_files_info_tests = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
    ("calculator", "main.py"),
    ("calculator", "testdir/testdir")
]



def test_get_files_info():
    for test in get_files_info_tests:
        print(f"calling get_files_info({test[0]}, {test[1]})")
        print(get_files_info(test[0], test[1]))

get_file_content_tests = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat")
]

def test_file_content():
    for test in get_file_content_tests:
        print(f'Testing with directory [{test[0]}] and file [{test[1]}].')
        file_content = get_file_content(test[0], test[1])
        print(f"File contents: {file_content}")

write_file_tests = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")
]

def test_write_file():
    for test in write_file_tests:
        print(f'Testing with directory "{test[0]}", file "{test[1]}", and content "{test[2]}"')
        result = write_file(test[0], test[1], test[2])
        print(f"Result: {result}")

run_python_file_tests = [
    ("calculator", "main.py"),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py")
]
def test_run_python_file():
    for test in run_python_file_tests:
        print(f'Testing with directory "{test[0]}", file "{test[1]}"')
        result = run_python_file(test[0], test[1])
        print(f"Result: {result}")



if __name__ == "__main__":
    test_run_python_file()


