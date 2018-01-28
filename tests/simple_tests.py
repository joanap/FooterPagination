import unittest
from src import footer_pagination


class SimpleTests(unittest.TestCase):

    def test_beginning_pages(self):
        """
        Test the initial status of the beginning pages bin
        """
        self.assertSequenceEqual((1, 1), footer_pagination.init_beginning_pages(5, 1))

    def test_end_pages(self):
        """
        Test the initial status of the end pages bin
        """
        self.assertSequenceEqual((5, 5), footer_pagination.init_end_pages(5, 1))

    def test_around_pages(self):
        """
        Test the initial status of the around pages bin
        """
        self.assertSequenceEqual((4, 4), footer_pagination.init_around_pages(4, 0, 5))

    def test_are_overlapping_pages(self):
        """
        Test overlapping sets of pages
        """
        self.assertTrue(footer_pagination.are_overlapping_pages((1, 3), (2, 4)))

    def test_not_overlapping_pages(self):
        """
        Test not overlapping sets of pages
        """
        self.assertFalse(footer_pagination.are_overlapping_pages((1, 3), (6, 7)))

    def test_unify_pages(self):
        """
        Tests merging of two overlapping sets of pages
        """
        self.assertSequenceEqual((1, 4), footer_pagination.unify_pages((1, 3), (2, 4)))

    def test_update_pages(self):
        """
        Tests the update of two sets of pages that overlap
        """
        self.assertSequenceEqual(((1, 4), None), footer_pagination.update_pages((1, 3), (2, 4)))


def main():
    unittest.main()


if __name__ == '__main__':
    main()