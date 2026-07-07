from functions.get_file_content import get_file_content

def test():
    result_1 = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result_1)}")
    print(f"lorem.txt truncated: {'truncated' in result_1}")
    print("")

    result_2 = get_file_content("calculator", "main.py")
    print(f"main.py length: {len(result_2)}")
    print(f"main.py truncated: {'truncated' in result_2}")
    print(result_2)
    print("")

    result_3 = get_file_content("calculator", "pkg/calculator.py")
    print(f"pkg/calculator.py length: {len(result_3)}")
    print(f"pkg/calculator.py truncated: {'truncated' in result_3}")
    print(result_3)
    print("")

    result_4 = get_file_content("calculator", "/bin/cat")
    print(f"/bin/cat length: {len(result_4)}")
    print(f"/bin/cat truncated: {'truncated' in result_4}")
    print("")

    result_5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"pkg/does_not_exist.py length: {len(result_5)}")
    print(f"pkg/does_not_exist.py truncated: {'truncated' in result_5}")
    print("")

if __name__ == "__main__":
    test()