class Book:
    """Represents a book with title, author, and publication year."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self) -> int:
        """Return the age of the book based on the year 2025."""
        current_year = 2025
        return current_year - self.year

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author} ({self.year})"


class EBook(Book):
    """Represents an electronic book."""

    def __init__(self, title: str, author: str, year: int, file_size: float):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"{super().__str__()} - File size: {self.file_size}MB"
