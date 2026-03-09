from datetime import datetime


class Note:
    def __init__(self, text: str, page:int, date:datetime):
        self.text: str = text
        self.page: int = page
        self.date = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED : int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int ):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes : list[Note] = [ ]


    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False

        nueva_nota = Note(text, page, date)
        self.notes.append(nueva_nota)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in [Book.EXCELLENT, Book.GOOD, Book.BAD]:
            return False

        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        return [nota for nota in self.notes if nota.page == page]

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        conteo_paginas = {}
        for nota in self.notes:
            conteo_paginas[nota.page] = conteo_paginas.get(nota.page, 0) + 1


















