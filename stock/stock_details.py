from database import database
from flask import Flask, request, jsonify



def stock():
    request_data = request.get_json()
    dict_book = database.Database.read_db()
    
    #1. Books in Stock
    #2. Issued Books

    choice=request_data['choice']
    if choice==1:
        dataset = dict_book['book']
        return jsonify(dataset)
       
    if choice==2:
        dataset = dict_book['user_details']
        return jsonify(dataset)


