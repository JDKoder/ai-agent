from functions.get_files_info import get_files_info


get_files_info_tests = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
    ("calculator", "main.py"),
    # ("calculator", "testdir/testdir")
]


for test in get_files_info_tests:
    print(f"calling get_files_info({test[0]}, {test[1]})")
    print(get_files_info(test[0], test[1]))
