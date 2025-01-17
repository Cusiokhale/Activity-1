""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Cordelia Usiokhale"
__version__ = ""

from genre.genre import Genre

class LibraryItem:

    """
    LibraryItem class: Maintains library item data.
    """
    def __init__(self, item_id: int,title: str, 
                 author: str, 
                 genre: Genre, is_borrowed: bool):
                 
        """
        Initializes the LibraryItem with title, author, and genre.
        Args:
            item_id (int): The libary items unique identifier
            name (str): The name of the libray item.
            author (str): The name of the library items author.
            genre (Genre): The genre the library item belongs to.
            is_borrowed (bool): Whether the library item is borrowed or not

        Raises:
            ValueError: When item_id, title, author or is_borrowed is blank
            and when genre is invalid.
        
        """

        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item Id must be numeric.")

        if len(title.strip()) > 0:
            self.__title = title
        else:
            raise ValueError("Title cannot be blank.")

        if len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")

        
        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid genre.")
        
        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value.")
        
    @property
    def item_id(self) -> int:
        """
        Accessor for item_id attribute.

        Returns:
            int: The id of the library item.
        """
        return self.__item_id

    @property
    def title(self) -> str:
        """
        Accessor for title attribute.

        Returns:
            str: The title of the library item.
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        Accessor for author attribute.

        Returns:
            str: The author of the library item.
        """
        return self.__author

    @property
    def genre(self) -> Genre:
        """
        Accessor for genre attribute.

        Returns:
            Genre: The genre of the library item.
        """
        return self.__genre

    @property
    def is_borrowed(self) -> bool:
        """
        Accessor for is_borrowed attribute.

        Returns:
            bool: Whether the library item is borrowed or not.
        """
        return self.__is_borrowed
    
           
