import unittest
from src import footer_pagination


class SimpleTests(unittest.TestCase):

    def test_beginning_pages(self):
        """Test the initial status of the set of pages in the beginning

        """
        self.assertSequenceEqual((1, 1), footer_pagination.init_beginning_pages(5, 1))

    def test_end_pages(self):
        """Test the initial status of the set of pages in the end pages

        """
        self.assertSequenceEqual((5, 5), footer_pagination.init_end_pages(5, 1))

    def test_around_pages(self):
        """Test the initial status of the set of around pages

        """
        self.assertSequenceEqual((4, 4), footer_pagination.init_around_pages(4, 0, 5))

    def test_overlapping_pages(self):
        """Test overlapping sets of pages

        """
        self.assertTrue(footer_pagination.are_overlapping_pages((1, 3), (2, 4)))

    def test_not_overlapping_pages(self):
        """Test not overlapping sets of pages

        """
        self.assertFalse(footer_pagination.are_overlapping_pages((1, 3), (6, 7)))

    def test_merge_pages(self):
        """Tests merging of two overlapping sets of pages

        """
        self.assertSequenceEqual((1, 4), footer_pagination.merge_pages((1, 3), (2, 4)))

    def test_update_overlap_pages(self):
        """Test the update of two sets of pages that overlap

        """
        self.assertSequenceEqual(((1, 4), None), footer_pagination.update_pages((1, 3), (2, 4)))

    def test_update_not_overlap_pages(self):
        """Test the update of two sets of pages that do not overlap

        """
        self.assertSequenceEqual(((1, 3), (6, 7)), footer_pagination.update_pages((1, 3), (6, 7)))

    def test_find_first_page(self):
        """Test if the first page is contained in the sets of pages

        """
        self.assertTrue(footer_pagination.find_page([(1, 2), (3, 5), None], 1))

    def test_not_find_first_page(self):
        """Test if the first page is contained in the sets of pages

        """
        self.assertFalse(footer_pagination.find_page([(2, 3), (4, 5), None], 1))

    def test_exist_remaining_pages(self):
        """Test when two sets of pages have remaining pages between them

        """
        self.assertTrue(footer_pagination.exist_remaining_pages((1, 3), (6, 7)))

    def test_not_exist_remaining_pages(self):
        """Test when two sets of pages do not have remaining pages between them

        """
        self.assertFalse(footer_pagination.exist_remaining_pages((1, 7), (8, 9)))



def main():
    unittest.main()


if __name__ == '__main__':
    main()