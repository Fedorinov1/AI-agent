from functions.write_file import write_file

def test():
    result_1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result_1)
    print("")

    result_2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result_2)
    print("")

    result_3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result_3)
    print("")

if __name__ == "__main__":
    test()