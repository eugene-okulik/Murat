class Book:
    def __init__(self, page_material, text, title, author, page_count, isbn, reserved = False):
        self.page_material = page_material
        self.text = text
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def reserved_book(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count},  материал: "
                  f"{self.page_material}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count},  материал: "
                  f"{self.page_material}")

reserved_book1 = Book('sdf','sdfdsf','sdfsdf','sdfds',56, "456", reserved=True)
reserved_book1.reserved_book()

no_reserved_book2 = Book('sdf','sdfdsf','sdfsdf','sdfds',56, "456")
no_reserved_book2.reserved_book()



