import sys

INPUT_LEN = 5

def main():

    if len(sys.argv) == INPUT_LEN:
        current_page = int(sys.argv[1])
        total_pages = int(sys.argv[2])
        boundaries = int(sys.argv[3])
        around = int(sys.argv[4])
    else:
        print("Missing arguments")


if __name__ == '__main__':
    main()