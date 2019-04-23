from flask import (Blueprint,
                   request,
                   jsonify,
                   current_app)
from .. import models
from datetime import datetime, timedelta

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
        print('get')
    # return jsonify(book.to_dict())
        return jsonify(books)
    return

@module.route('/')
def test():
    return jsonify({
        'status': 'success'
    })