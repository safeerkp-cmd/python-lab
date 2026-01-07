class book:
    def __init__(self,auther,title):
        self.auther=auther
        self.title=title
class value(book):
    def __init__(self,auther,title,price,page):
        super().__init__(auther,title)
        self.price=price
        self.title=title
        self.page=page
    def display(self):
        print("title",self.title)
        print("auther",self.auther)
        print("price",self.price)
        print("page",self.page)
obj=value("safeer","python",250,400)
obj.display()
