from functions.run_python_file import run_python_file

def test():
    result_1 = run_python_file("calculator", "main.py")
    print(result_1)
    print("")

    result_2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result_2)
    print("")

    result_3 = run_python_file("calculator", "tests.py")
    print(result_3)
    print("")

    result_4 = run_python_file("calculator", "../main.py")
    print(result_4)
    print("")

    result_5 = run_python_file("calculator", "nonexistent.py")
    print(result_5)
    print("")

    result_6 = run_python_file("calculator", "lorem.txt")
    print(result_6)
    print("")

if __name__ == "__main__":
    test()