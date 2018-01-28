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


def main():
    unittest.main()


if __name__ == '__main__':
    main()