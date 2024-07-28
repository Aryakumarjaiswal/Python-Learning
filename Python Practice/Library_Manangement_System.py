print("\t\t Welcome to library Management System")

class Library:
    def __init__(self,lib,book):
        self.lib=lib
        self.book=book


    def addition(self,book_name):
        # for self.ele in li:
        #     self.book.append(self.ele)
        self.book.append(book_name)

    def info(self):
        print(f'Library Name: {self.lib}\nBooks: {self.book}\nTotal Books: {len(self.book)}')
    

Library1=Library("Roar",["Habit Of Winning","Flying Sikh","MS Dhoni:Captain Cool"])
Library1.info()
ip=input("Want to Add more books(Y/N)")
if(ip!='Y' and ip!='N'):
    print("Enter Valid Letter")
if ip=='Y':

    nbook_sz=input("Total books to add: ")
    for ele in range(int(nbook_sz)):
        val=input("Enter Name: ")
        Library1.addition(val)

Library1.info()
