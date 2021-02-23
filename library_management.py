from book import book_manage
from database import database
from issue_book import issue_book
from return_book import return_book
from stock import stock_details
from flask import Flask, request, jsonify

app = Flask(__name__)
database.Database.create_db()

@app.route("/", methods=['GET'])
def home():
    return "Welcome to Library Management Server"

#Add book
@app.route("/addbook", methods=['POST'])
def addbook():
    return book_manage.addbook()


#Delete book using separate ID        
@app.route('/deletebook', methods=['POST'])
def deletebook():
    return book_manage.deletebook()


#Search book using ID, Title, Author
@app.route('/searchbook',methods=['POST'])
def searchbook():
    return book_manage.searchbook() 


@app.route('/updatebook',methods=['POST'])
def updatebook():
    return book_manage.updatebook() 

        
#Update count of books
@app.route('/updatecount',methods=['POST'])
def updatecount():
    return book_manage.updatecount() 

            
#Issue Book
@app.route('/issuebook', methods=['POST'])
def issuebook():
    return issue_book.issuebook()


#Return Book
@app.route('/returnbook', methods=['POST'])
def returnbook():
    return return_book.returnbook() 


#Stock details
@app.route('/stock',methods=['POST'])
def stock():
    return stock_details.stock()

		
if __name__ == "__main__":
    app.run(debug=True)
