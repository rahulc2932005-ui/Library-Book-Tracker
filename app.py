from flask import Flask, request, jsonify
from flask_cors import CORS
from db_config import get_db_connection

app = Flask(__name__)
CORS(app)

# Add a new book
@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    status = data.get('status', 'available')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, status) VALUES (%s, %s, %s)",
        (title, author, status)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Book added successfully!"}), 201


# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(books)


# Delete a book
@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Book deleted successfully!"})


# Update book status
@app.route('/update_status/<int:book_id>', methods=['PUT'])
def update_status(book_id):
    data = request.json
    new_status = data.get('status')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET status = %s WHERE id = %s", (new_status, book_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Book status updated successfully!"})


if __name__ == '__main__':
    app.run(debug=True)

