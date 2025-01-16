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
    def __init__(self, title: str, 
                 author: str, 
                 genre: Genre):
                 
        """
        Initializes the LibraryItem with title, author, and genre.
        Args: 
            name (str): The name of the libray item.
            genre (Genre): The genre to which the 
            library item applies.
            credit_hours (int): The number of credit hours 
            assigned to the library item.

        Raises:
            ValueError: When title or author is blank.
            TypeError: When genre is not of type Genre.
        
        """
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
            raise ValueError("Invalid genre. .")
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

    
           
