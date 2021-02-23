import os.path

class Database():
    def create_db():
        if os.path.exists("C:\\Users\\Kochu\\library\\database\\bookdata.txt") == False:
            print("welcome to Library Management System")
            library_name = input("Enter library name: ")
            library_name = "'" +library_name+ "'"
            f = open("C:\\Users\\Kochu\\library\\database\\bookdata.txt",'w')
            f.write("{'Library_name':"+library_name+", 'book':[], 'book_details':[], 'user_details':[]}")
            f.close()
            if os.path.exists("C:\\Users\\Kochu\\library\\database\\bookdata.txt"):
                print("Db created successfully")
            else:
                print("Something went wrong...")

    def write_db(dict_book):
        f = open("C:\\Users\\Kochu\\library\\database\\bookdata.txt",'w')
        f.write(str(dict_book))
        f.close()


    def read_db():
        f = open("C:\\Users\\Kochu\\library\\database\\bookdata.txt",'r')
        for item in f.readlines():
            dict_book = eval(item)
            return dict_book

