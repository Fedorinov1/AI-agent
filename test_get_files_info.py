from functions.get_files_info import get_files_info

def test():
    print("Result for current directory:")
    result_1 = get_files_info("calculator", ".")
    print(result_1)
    print("")

    print("Result for 'pkg' directory:")
    result_2 = get_files_info("calculator", "pkg")
    print(result_2)
    print("")

    print("Result for '/bin' directory:")
    result_3 = get_files_info("calculator", "/bin")
    print(result_3)
    print("")

    print("Result for '../' directory:")
    result_4 = get_files_info("calculator", "../")
    print(result_4)
    print("")

if __name__ == "__main__":
    test()