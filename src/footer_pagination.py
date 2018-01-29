import sys

INPUT_LEN = 5
FIRST_PAGE = 1
FIRST_PAGE_INDEX = 0
LAST_PAGE_INDEX = 1
REMAINING_PAGES = "..."


def init_beginning_pages(total_pages, boundaries):
    """Define the initial status for the set of pages in the beginning: return first and last page

    :param total_pages: total number of pages
    :param boundaries: how many pages we want to link in the beginning, or end
    :return: (first beginning page, last beginning page)
    """
    if boundaries != 0:
        if boundaries < total_pages:
            return FIRST_PAGE, boundaries
        else:
            FIRST_PAGE, total_pages
    else:
        None


def init_end_pages(total_pages, boundaries):
    """Define the initial status for the set of pages in the end: return first and last page

    :param total_pages: total number of pages
    :param boundaries: how many pages we want to link in the beginning, or end
    :return: (first end page, last end page)
    """
    if boundaries != 0:
        if total_pages - boundaries > 0:
            return total_pages - boundaries+1, total_pages
        else:
            return FIRST_PAGE, total_pages
    else:
        return None


def init_around_pages(current_page, around, total_pages):
    """Define the initial status for the set of pages in the around: return first and last page

    :param current_page: current page
    :param around: how many pages we want to link before and after the current page
    :param total_pages: total number of pages
    :return: (first around page, last around page)
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
    """Define the initial status for the sets of pages: return a list with beginning, around and end set of pages

    :param current_page: current page
    :param total_pages: total number of pages
    :param boundaries: how many pages we want to link in the beginning, or end
    :param around: how many pages we want to link before and after the current page
    :return: list with beginning, around and end set of pages
    """
    beginning_pages = init_beginning_pages(total_pages, boundaries)
    around_pages = init_around_pages(current_page, around, total_pages)
    end_pages = init_end_pages(total_pages, boundaries)
    return [beginning_pages, around_pages, end_pages]


def are_overlapping_pages(pages1, pages2):
    """Check if the sets pages1 and pages2 overlap: return True if pages1 and pages2 overlap

    :param pages1: set of pages
    :param pages2: set of pages
    :return: True if pages1 and pages2 overlap
    """
    if pages1 is None or pages2 is None:
        return False
    else:
        return not (pages1[LAST_PAGE_INDEX] < pages2[FIRST_PAGE_INDEX] or
                    pages2[LAST_PAGE_INDEX] < pages1[FIRST_PAGE_INDEX])


def merge_pages(pages1, pages2):
    """Merge overlapping sets of pages1 and pages2: return the merged set of pages

    :param pages1: set of pages
    :param pages2: set of pages
    :return: merged set of pages
    """
    return min(pages1[FIRST_PAGE_INDEX], pages2[FIRST_PAGE_INDEX]), max(pages1[LAST_PAGE_INDEX], pages2[LAST_PAGE_INDEX])


def update_pages(pages1, pages2):
    """Merge two sets of pages if they overlap, otherwise return the initial status of the sets

    :param pages1: set of pages
    :param pages2: set of pages
    :return: (merged set of pages, None) if pages1 and pages2 overlap, otherwise return (pages1, pages2)
    """
    if are_overlapping_pages(pages2, pages1):
        return merge_pages(pages2, pages1), None
    else:
        return pages1, pages2


def update_all_pages(initial_pages_status):
    """Iterate the sets of pages and check if the current set of pages overlap the next sets of pages; unify sets
    that overlap.

    :param initial_pages_status: initial pages status
    :return: final pages status with no overlapping.
    """

    for pages_index, item in enumerate(initial_pages_status):
        for i in range(pages_index, len(initial_pages_status) - 1):
            new_pages_status = update_pages(initial_pages_status[pages_index], initial_pages_status[i+1])
            if new_pages_status is not None:
                if initial_pages_status[pages_index] is not None:
                    initial_pages_status[pages_index] = new_pages_status[0]
                if initial_pages_status[i+1] is not None:
                    initial_pages_status[i+1] = new_pages_status[1]
    return initial_pages_status


def exist_remaining_pages(pages1, pages2):
    """Check if there are remaining pages between the sets of pages pages1 and pages2

    :param pages1: set of pages
    :param pages2: set of pages
    :return: True if exist remaining pages between pages1 and pages2
    """
    if pages1 is not None and pages2 is not None:
        return pages2[FIRST_PAGE_INDEX] - pages1[LAST_PAGE_INDEX] > 1
    else:
        return False


def print_range(pages):
    """Print the range of pages in the set pages

    :param pages: set of pages to print
    """
    if pages is not None:
        print(*range(pages[FIRST_PAGE_INDEX], pages[LAST_PAGE_INDEX]+1), sep=' ', end='')


def find_page(pages_list, page_to_found):
    """Check if page_to_found is in pages_list: return True if exists

    :param pages_list: list with sets of pages
    :param page_to_found: page to found in the list
    :return: True if the page is in the list
    """
    for current_pages in pages_list:
        if current_pages is not None:
            if page_to_found == current_pages[FIRST_PAGE_INDEX] or page_to_found == current_pages[LAST_PAGE_INDEX]:
                return True
    return False


def remove_none(pages_list):
    """Remove None elements from a list

    :param pages_list: list of sets of pages
    :return: list without None elements
    """
    return [pages for pages in pages_list if pages is not None]


def print_output(pages_list, last_page, boundaries):
    """Concatenate and print footer pagination

    :param pages_list: sets of pages
    :param last_page: total pages
    :param boundaries: how many pages we want to link in the beginning, or end
    """
    pages_list_without_none = remove_none(pages_list)
    if boundaries == 0 and not find_page(pages_list_without_none, FIRST_PAGE):
        print(REMAINING_PAGES + " ", end='')
    for pages_index, current_pages in enumerate(pages_list_without_none):
        print_range(current_pages)
        if pages_index + 1 < len(pages_list_without_none):
            if exist_remaining_pages(current_pages, pages_list_without_none[pages_index + 1]):
                print(" " + REMAINING_PAGES + " ", end='')
            else:
                print(" ", end='')
    if boundaries == 0 and not find_page(pages_list_without_none, last_page):
        print(" " + REMAINING_PAGES, end='')


def validate_input(current_page, total_pages, boundaries, around):
    """
    Raises an exception if input is invalid
    :param current_page: current page
    :param total_pages: total number of pages
    :param boundaries: how many pages we want to link in the beginning, or end
    :param around: how many pages we want to link before and after the current page
    """
    if current_page <= 0 or total_pages <= 0:
        raise ValueError("Current page and total pages must be greater than 0")
    if boundaries < 0 or around < 0:
        raise ValueError("Boundaries and around must be greater or equal to 0")
    if current_page > total_pages:
        raise ValueError("Current page must be lower than total pages")


def get_footer_pagination(current_page, total_pages, boundaries, around):
    """Build and print footer pagination according page, total_pages, boundaries and around

    :param current_page: current page
    :param total_pages: total number of pages
    :param boundaries: how many pages we want to link in the beginning, or end
    :param around: how many pages we want to link before and after the current page
    """
    initial_pages_stat = initial_pages_status(current_page, total_pages, boundaries, around)
    final_pages_stat = update_all_pages(initial_pages_stat)
    print_output(final_pages_stat, total_pages, boundaries)


def main():
    """Read arguments current_page, total_page, boundaries and around and build the corresponding footer pagination

    """
    if len(sys.argv) == INPUT_LEN:
        current_page = int(sys.argv[1])
        total_pages = int(sys.argv[2])
        boundaries = int(sys.argv[3])
        around = int(sys.argv[4])
        try:
            validate_input(current_page, total_pages, boundaries, around)
            get_footer_pagination(current_page, total_pages, boundaries, around)
        except ValueError as err:
            print(err)
    else:
        print("Missing arguments")


if __name__ == '__main__':
    main()