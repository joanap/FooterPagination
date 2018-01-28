import sys

INPUT_LEN = 5
FIRST_PAGE = 1
FIRST_PAGE_INDEX = 0
LAST_PAGE_INDEX = 1


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


def init_end_pages(total_pages, boundaries):
    """

    :param total_pages:
    :param boundaries:
    :return: first end page, last end page
    """
    if boundaries != 0:
        if total_pages - boundaries > 0:
            return total_pages - boundaries+1, total_pages
        else:
            return FIRST_PAGE, total_pages
    else:
        return None


def init_around_pages(current_page, around, total_pages):
    """

    :param current_page:
    :param around:
    :param total_pages:
    :return: first around page, last around page
    """
    around_first_page = around_last_page = current_page
    if around != 0:
        around_first_page = current_page - around
        around_last_page = current_page + around
        if around_first_page < 1:
            around_first_page = FIRST_PAGE
        if around_last_page > total_pages:
            around_last_page = total_pages
    return around_first_page, around_last_page


def initial_pages_status(current_page, total_pages, boundaries, around):
    """

    :param current_page:
    :param total_pages:
    :param boundaries:
    :param around:
    :return:
    """
    beginning_pages = init_beginning_pages(total_pages, boundaries)
    around_pages = init_around_pages(current_page, around, total_pages)
    end_pages = init_end_pages(total_pages, boundaries)
    return [beginning_pages, around_pages, end_pages]


def are_overlapping_pages(pages1, pages2):
    """Does the range (start1, end1) overlap with (start2, end2)?
    :param pages1:
    :param pages2:
    :return:
    """
    if pages1 is None or pages2 is None:
        return False
    else:
        return not (pages1[LAST_PAGE_INDEX] < pages2[FIRST_PAGE_INDEX] or
                    pages2[LAST_PAGE_INDEX] < pages1[FIRST_PAGE_INDEX])


def unify_pages(pages1, pages2):
    """
    Merge two overlapping sets of pages
    :param pages1:
    :param pages2:
    :return:
    """
    return min(pages1[FIRST_PAGE_INDEX], pages2[FIRST_PAGE_INDEX]), max(pages1[LAST_PAGE_INDEX], pages2[LAST_PAGE_INDEX])


def update_pages(pages1, pages2):
    """
    Merge two sets of pages if they overlap, otherwise returns the initial sets
    :param pages1:
    :param pages2:
    :return:
    """
    if are_overlapping_pages(pages2, pages1):
        return unify_pages(pages2, pages1), None
    else:
        pages1, pages2


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