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

class scholl_book(Book):
    def __init__(self, page_material, text, title, author, page_count, isbn, subject, numb_class, reserved = False):
        super().__init__(page_material, text, title, author, page_count, isbn, reserved)
        self.subject = subject
        self.numb_class = numb_class

    def reserved_book(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, предмет: {self.subject}, "
                  f"класс: {self.numb_class}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, предмет: {self.subject}, "
                  f"класс: {self.numb_class}")

reserved_class_book = scholl_book('sdf','sdfdsf','sdfsdf','sdfds',56, "456",
                                  'математика', 5, reserved=True)
reserved_class_book.reserved_book()

no_reserved_class_book = scholl_book('sdf','sdfdsf','sdfsdf','sdfds',56, "456",
                                     'математика', 5)
no_reserved_class_book.reserved_book()


