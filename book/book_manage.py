from database import database
from flask import Flask, request, jsonify


error_response = {'error' : "+error_msg+"}
success_response = {'success' : "+success_msg+"}
#Add book

def addbook():
    
    flag = False
    request_data = request.get_json()

    dict_book = database.Database.read_db()
    if request_data:
        book_id = request_data['book_id']
        for x in dict_book['book']:
            if book_id == x['book_id']:
                flag = True
                error_response['error'] = "Book already exists"
                return jsonify(error_response)

        if flag == False:
            title = request_data['title']
            author = request_data['author']
            try:
                copies = int(request_data['copies'])
                dict_book['book'].append({'book_id':book_id, 'title':title, 'author':author, 'copies':copies, 'permanent_count':copies})
                #print("Book added successfully")
            except:
                error_response['error'] = "Enter a Number"
                return jsonify(error_response)
            
        #generate separate id for each book
        try:
            i = 1
            while i<=copies:
                separate_id = book_id + str(i)
                dict_book['book_details'].append({'book_id':book_id, 'separate_id':separate_id})
                i+=1
        except:
            error_response['error'] = "Invalid input"
            return jsonify(error_response)

        database.Database.write_db(dict_book)
        success_response['success'] = "Book added successfully"
        return jsonify(success_response)
            

#Delete book using separate ID

def deletebook():
    flag = False
    request_data = request.get_json()
    dict_book = database.Database.read_db()

    del_bid = request_data['del_bid']
    del_id = request_data['del_id']
    for x in dict_book['book_details']:
        if x['separate_id'] == del_id:
            flag = True
            dict_book['book_details'].remove(x)
            for x in dict_book['book']:       
                if (x['book_id'] == del_bid):
                    x.update({'copies':x['copies']-1, 'permanent_count':x['permanent_count']-1})
                    database.Database.write_db(dict_book)
                    
                    success_response['success'] = "Book removed successfully"
                    return jsonify(success_response)       
    if flag == False:
        error_response['error'] = "Invalid ID"
        return jsonify(error_response)

#Search book using ID, Title, Author

def searchbook():
    dict_book = database.Database.read_db()
    flag = False
    request_data = request.get_json()

    choice=request_data['choice']
    if choice==1:
                s_title = request_data['s_title']
                for x in dict_book['book']:
                    if x['title'] == s_title:
                        flag = True
                        return jsonify(x)
                if flag == False:
                    error_response['error'] = "Invalid title"
                    return jsonify(error_response) 
            
    if choice==2:
                s_author = request_data['s_author']
                list = []
                for x in dict_book['book']:
                    if x['author'] == s_author:
                        flag = True
                        list.append(x.copy())
                return jsonify(list)

                if flag == False:
                    error_response['error'] = "Invalid author name"
                    return jsonify(error_response) 

    if choice==3:
                s_id = request_data['s_id']
                for x in dict_book['book']:
                    if x['book_id'] == s_id:
                        flag = True
                        return jsonify(x)
                if flag == False:
                    error_response['error'] = "Invalid ID"
                    return jsonify(error_response) 
                
#Update book details such as author and title

def updatebook():
        dict_book = database.Database.read_db()
        flag = False
        request_data = request.get_json()

        update_id = request_data['update_id']
        for x in dict_book['book']:
            if x['book_id'] == update_id:
                flag = True
                new_title = request_data['new_title']
                new_author = request_data['new_author']
                x.update({'book_id':update_id, 'title':new_title, 'author':new_author})
                database.Database.write_db(dict_book)
                success_response['success'] = "Book updated successfully"
                return jsonify(success_response)
        if flag == False:
            error_response['error'] = "Invalid ID"
            return jsonify(error_response)

#Update count of books

def updatecount():
        dict_book = database.Database.read_db()
        flag = False
        request_data = request.get_json()

        book_id = request_data['book_id']
        try:
            new_copies = request_data['new_copies']
            for x in dict_book['book']:
                if x['book_id'] == book_id:
                    cp = x['permanent_count'] +1
                    x.update({'copies':x['copies']+new_copies, 'permanent_count':x['permanent_count']+new_copies})
        except :
            error_response['error'] = "Invalid count"
            return jsonify(error_response) 
        
        #generate separate id for each book
        try:
            i = 1
            while i<=new_copies:
                separate_id = book_id + str(cp)
                dict_book['book_details'].append({'book_id':book_id, 'separate_id':separate_id})
                i+=1
                cp+=1
            database.Database.write_db(dict_book)  
            success_response['success'] = "Book count updated successfully"
            return jsonify(success_response) 
        except:
            error_response['error'] = "Invalid ID"
            return jsonify(error_response) 