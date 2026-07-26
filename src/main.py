from reviewer import review_code
from utils import read_file


def main():

    file_path = input("Enter Python file path: ")

    code = read_file(file_path)

    feedback = review_code(code)

    print(feedback)


if __name__ == "__main__":
    main()