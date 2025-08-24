from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

'''if __name__ == "__main__":
    result = get_files_info("calculator", ".")
    print("Result for current directory:\n" + result)

    result2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:\n" + result2)

    result3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:\n    " + result3)

    result4 = get_files_info("calculator", "../")
    print("Result for '../' directory:\n    " + result4)'''

'''if __name__ == "__main__":
    result = get_file_content("calculator", "main.py")
    print(f"contents of file:\n" + result)
    print(" ")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"contents of file:\n" + result)
    print(" ")
    result = get_file_content("calculator", "/bin/cat")
    print(f"contents of file:\n" + result)
    print(" ")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"contents of file:\n" + result)'''

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print(" ")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print(" ")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test()