class library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def displayavailablebooks(self):
        print("books present in this library are:")
        for book in self.books:
            print("\t*"+book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print("you have been issued {bookname}.Please keep it safe and return it within 30 days.")
            self.books.remove(bookname)
            return True
        else:
            print("sorry,this book is either not available or  has been already issued to someone else.Please wawit until the book is available.")
            return False
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book! Have a great day.")


class student:
    def requestbook(self):
        self.book=input("enter the name of the book you want to borrow:")
        return self.book
    def returnbook(self):
        self.book=input("enter the name of the book you want to return:")
        return self.book
if __name__=="__main__":
    centrallibrary=library(["algorithms","django","python","data structure"])
    student=student()
    centrallibrary.displayavailablebooks()
    while(True):
        welcomemsg='''
*********welcome to central library********
        please choose an option:
        1.list of all books
        2.request a book
        3.Add/return a book
        4.exit the library
            '''
        print(welcomemsg)
        a=int(input("enter a choice:"))
        if a==1:
              centrallibrary.displayavailablebooks()
        elif a==2:
              centrallibrary.borrowbook(student.requestbook())

        elif a==3:
              centrallibrary.returnbook(student.returnbook())
        elif a==4:
             print("Thanks for choosing central library.Have a great day")
             exit()
        else:
              print("invalid choice")





              
        
