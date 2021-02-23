from database import database
from flask import Flask, request, jsonify


def issuebook():

        error_response = {'error' : "+error_msg+"}
        success_response = {'success' : "+success_msg+"}

        dict_book = database.Database.read_db()
        flag = True
        request_data = request.get_json()
        
        book_id = request_data['book_id']
        sep_id = request_data['separate_id']
        result = {"success":"+success_msg+", "book_id" :[], "title":[], "no.of copies":[]}
        for x in dict_book['book']:
            for z in dict_book['book_details']: 
                if x['book_id'] == book_id and z['separate_id'] == sep_id:
                    #print("book_id : ",x['book_id'],"\nTitle: ",x['title'],"\nAuthor :",x['author'],"\nNo.of copies Available: ",x['copies'])
                    if x['copies'] != 0:
                        for y in dict_book['user_details']:
                                if y['separate_id'] == sep_id:
                                    flag = False
                                    error_response['error'] = "Book already issued"
                                    return jsonify(error_response) 
                        
                        if flag == True:
                            user_name = request_data['user_name']
                            user_phone =  request_data['user_phone']
                            user_place = request_data['user_place']
                            for x in dict_book['book']:       
                                if (x['book_id'] == book_id):
                                    x.update({'copies':x['copies']-1})

                                    dict_book['user_details'].append({'name':user_name, 'phone':user_phone, 'place':user_place, 'book_id':book_id, 'separate_id':sep_id})
                                    database.Database.write_db(dict_book)
                                    success_msg = "Book issued"
                                    result = {
                                    'success' : success_msg,
                                    'book_id': x['book_id'],
                                    'title' : x['title'],
                                    'author' : x['author'],
                                    'No.of copies Available' : x['copies']
                                    }

                                    return jsonify(result)
                                            
        if flag == True:
            error_response['error'] = "Invalid ID"
            return jsonify(error_response) 