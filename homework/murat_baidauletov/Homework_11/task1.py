class Book:
    def __init__(
        self,
        page_material,
        text,
        title,
        author,
        page_count,
        isbn,
        reserved=False
    ):
        self.page_material = page_material
        self.text = text
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def reserved_book(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.page_count}, материал: {self.page_material}, "
                f"зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.page_count}, материал: {self.page_material}"
            )


reserved_book1 = Book(
    "бумага",
    True,
    "Идиот",
    "Достоевский",
    500,
    "456",
    reserved=True
)
reserved_book1.reserved_book()

not_reserved_book2 = Book(
    "бумага",
    True,
    "Война и мир",
    "Толстой",
    1200,
    "789"
)
not_reserved_book2.reserved_book()