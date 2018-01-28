import unittest
from src import footer_pagination


class SimpleTests(unittest.TestCase):

    def test_beginning_pages(self):
        """
        Test the initial status of the beginning pages bin
        """
        self.assertSequenceEqual((1, 1), footer_pagination.init_beginning_pages(5, 1))


def main():
    unittest.main()


if __name__ == '__main__':
    main()