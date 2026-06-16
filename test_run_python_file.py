from functions.run_python_file import run_python_file


def test() -> None:
    result = run_python_file("calculator", "main.py")
    print("Result for main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for main.py plus math")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for tests.py")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for relative main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for nonexistant.py")
    print(result)
    print("")

    result = run_python_file("calculator", "lorem.txt")
    print("Result for lorem.txt")
    print(result)
    print("")


if __name__ == "__main__":
    test()
