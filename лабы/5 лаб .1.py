class Book:
    def __init__(self,title, author,year):
        self.title = "Сияние"
        self.author = "Стивин Кинг"
        self.year = 1989
    def get_info(self):
        return f"Title is {self.title},author : {self.author}, year of publication:{self.year}"
book = Book("Сияние" , "Стивин Кинг", 1989)
print(book.get_info())
