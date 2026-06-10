class Book:
    page_material = 'Бумага'
    text = True

    def __init__(
        self,
        title,
        author,
        page_count,
        isbn,
        reserved=False
    ):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def show_book_info(self):
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


class SchoolBook(Book):
    def __init__(
        self,
        title,
        author,
        page_count,
        isbn,
        subject,
        school_class,
        tasks,
        reserved=False
    ):
        super().__init__(
            title,
            author,
            page_count,
            isbn,
            reserved
        )
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def show_book_info(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.page_count}, предмет: {self.subject}, "
                f"класс: {self.school_class}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.page_count}, предмет: {self.subject}, "
                f"класс: {self.school_class}"
            )


# add book1
book1 = Book(
    "Тест",
    "тест123",
    200,
    "458"
)

# reserved book1
book1.reserved = True
book1.show_book_info()

# add book2
book2 = Book(
    "Война и мир",
    "Мурат murat",
    "200",
    1200,

)
book2.show_book_info()

school_book1 = SchoolBook(
    "Алгебра",
    "Иванов",
    200,
    "123",
    "Математика",
    9,
    True,
    reserved=True
)
school_book1.show_book_info()

school_book2 = SchoolBook(
    "История Казахстана",
    "Ақтөре",
    180,
    "456",
    "История",
    7,
    True
)
school_book2.show_book_info()
