from flask import (Blueprint,
                   request,
                   jsonify,
                   current_app)
from .. import models
from datetime import datetime, timedelta
import uuid

module = Blueprint('books', __name__, url_prefix='/api')

@module.route('/books', methods=['GET', 'POST'])
def all_books():
    if request.method == 'POST':
        post_data = request.get_json()
        book = models.Book(title=post_data.get('title'),
                           author=post_data.get('author'),
                           is_read=post_data.get('is_read'))
        
        book.save()
        print('Book added!!')
        return jsonify(book.to_dict())
    else:
        books = models.Book.objects()
        # print('get')
    # return jsonify(book.to_dict())
        return jsonify(books)
    return

@module.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def update_book(book_id):
    book = models.Book.objects.get(id=book_id)
    if request.method == 'PUT':
        put_data = request.get_json()
        book.title = put_data.get('title')
        book.author = put_data.get('author')
        book.is_read = put_data.get('is_read')
        book.save()
        print('Book update!!')
        return jsonify(book.to_dict())

    if request.method == 'DELETE':
        book.delete()
        print('Book delete')
        return jsonify(book.to_dict())
        
