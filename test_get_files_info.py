from functions.get_files_info import get_files_info


# Truthfully the way I did this page was way different
# but still worked. After passing the lessons I looked at the
# solution files and thought this was so much better. The other two pages were grammar fixes.
def test() -> None:
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "main.py")
    print("Result for 'main.py':")
    print(result)


if __name__ == "__main__":
    test()
