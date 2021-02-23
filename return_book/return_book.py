from database import database
from flask import Flask, request, jsonify


def returnbook():

        error_response = {'error' : "+error_msg+"}
        success_response = {'success' : "+success_msg+"}
        flag = False
        request_data = request.get_json()
        dict_book = database.Database.read_db()
		
        book_id = request_data['book_id']
        sep_id = request_data['separate_id']
        for x in dict_book['user_details']:
            if x['book_id'] == book_id and x['separate_id'] == sep_id:
                flag = True
                dict_book['user_details'].remove(x)
                for x in dict_book['book']:       
                    if (x['book_id'] == book_id):
                        x.update({'copies':x['copies']+1})
                        database.Database.write_db(dict_book)
                        success_response['success'] = "Book returned"
                        return jsonify(success_response) 
        if flag == False:
            error_response['error'] = "Invalid ID"
            return jsonify(error_response)