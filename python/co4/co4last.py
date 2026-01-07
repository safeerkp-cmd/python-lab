class book:
    def __init__(self,title,auther):
        self.title=title
        self.auther=auther
class value(book):
    def __init__(self,title,auther,price,pageno):
        super().__init__(title,auther)
        self.price=price
        self.pageno=pageno
    def display(self):
        print("title",self.title)
        print("auther",self.auther)
        print("price",self.price)
        print("pageno",self.pageno)

obj=value("mybook","safeer",100,500)
obj.display()
