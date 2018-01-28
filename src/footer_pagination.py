import sys

INPUT_LEN = 5
FIRST_PAGE = 1


def init_beginning_pages(total_pages, boundaries):
    """

    :param total_pages:
    :param boundaries:
    :return: first beginning page, last beginning page
    """
    if boundaries != 0:
        if boundaries < total_pages:
            return FIRST_PAGE, boundaries
        else:
            FIRST_PAGE, total_pages
    else:
        None

def main():

    if len(sys.argv) == INPUT_LEN:
        current_page = int(sys.argv[1])
        total_pages = int(sys.argv[2])
        boundaries = int(sys.argv[3])
        around = int(sys.argv[4])
    else:
        current_page = 4
        total_pages = 5
        boundaries = 1
        around = 0

        # print("Missing arguments")


if __name__ == '__main__':
    main()