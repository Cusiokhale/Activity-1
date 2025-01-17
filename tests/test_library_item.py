"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = ""
__version__ = ""

import unittest

from genre.genre import Genre

from library_item.library_item import LibraryItem

class TestLibraryItem (unittest.TestCase):
    def setUp(self):
        self.libraryitem = LibraryItem(1, "commanding the day","Paul Eneche", Genre.NON_FICTION, False)
 
    def test_init_valid_input_attribute_set(self):
        book= LibraryItem(1, "commanding the day","Paul Eneche", Genre.NON_FICTION, False)

        self.assertEqual(1, 
                         book._LibraryItem__item_id )
        self.assertEqual("commanding the day", 
                         book._LibraryItem__title )
        self.assertEqual("Paul Eneche", 
                         book._LibraryItem__author )
        self.assertEqual(Genre.NON_FICTION, 
                         book._LibraryItem__genre )
        self.assertEqual(False, 
                         book._LibraryItem__is_borrowed )

    def test_init_blank_item_id_raises_value_error(self):

        with self.assertRaises(ValueError):
            LibraryItem("", "commanding the day","Paul Eneche", Genre.NON_FICTION, False)
     
    def test_init_blank_title_raises_value_error(self):

        with self.assertRaises(ValueError):
            LibraryItem(1, "", "Paul Eneche", Genre.NON_FICTION, False)
    
    def test_init_blank_author_raises_value_error(self):

        with self.assertRaises(ValueError):
            LibraryItem(1, "commanding the day", "", Genre.NON_FICTION, False)

    def test_init_invalid_genre_raises_exception(self):

        with self.assertRaises(ValueError):
            LibraryItem(1, "commanding the day", "", "Drama", False)

    def test_init_invalid_is_borrowed_raises_exception(self):

        with self.assertRaises(ValueError):
            LibraryItem(1, "commanding the day", "", "Drama", "")
    
    def test_title_accessor_valid_libraryitem_title_returned(self):

        self.assertEqual("commanding the day", self.libraryitem.title)

    def test_author_accessor_valid_libraryitem_author_returned(self):

        self.assertEqual("Paul Eneche", self.libraryitem.author)

    def test_genre_accessor_valid_libraryitem_genre_returned(self):

        self.assertEqual(Genre.NON_FICTION, self.libraryitem.genre)


    

