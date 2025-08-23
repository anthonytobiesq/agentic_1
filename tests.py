from functions.get_files_info import get_files_info

if __name__ == "__main__":
    result = get_files_info("calculator", ".")
    print("Result for current directory:\n" + result)

    result2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:\n" + result2)

    result3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:\n    " + result3)

    result4 = get_files_info("calculator", "../")
    print("Result for '../' directory:\n    " + result4)