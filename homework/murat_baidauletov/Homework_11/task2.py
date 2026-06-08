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


class SchoolBook(Book):
    def __init__(
        self,
        page_material,
        text,
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
            page_material,
            text,
            title,
            author,
            page_count,
            isbn,
            reserved
        )
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def reserved_book(self):
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


reserved_school_book = SchoolBook(
    "бумага",
    True,
    "Алгебра",
    "Иванов",
    200,
    "123",
    "Математика",
    9,
    True,
    reserved=True
)
reserved_school_book.reserved_book()

not_reserved_school_book = SchoolBook(
    "бумага",
    True,
    "История",
    "Петров",
    180,
    "456",
    "История",
    8,
    True
)
not_reserved_school_book.reserved_book()