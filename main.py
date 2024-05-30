# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Sample data
# books = [
#     {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
#     {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho"},
#     {"id": 3, "title": "Clean Code", "author": "Robert C. Martin"}
# ]

# data = []

# # GET endpoint to fetch all books
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)

# # POST endpoint to receive data from the frontend
# @app.route('/receive_data', methods=['POST'])
# def receive_data():
#     # Check if request contains JSON data
#     if request.is_json:
#         try:
#             # Get JSON data from request body
#             req_data = request.get_json()

#             # Append received data to our sample data (simulating storing data)
#             data.append(req_data)

#             return jsonify({"message": "Data received successfully"}), 200
#         except Exception as e:
#             return jsonify({"error": str(e)}), 400
#     else:
#         return jsonify({"error": "Request body must be in JSON format"}), 400


# @app.route('/diseases', methods=['POST'])
# def split_string():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             input_string = data['input_string']
            
#             # Split the input string into an array of strings
#             split_array = input_string.split()
            
#             return jsonify({'result': split_array}), 200
#         except Exception as e:
#             return jsonify({'error': str(e)}), 400


# @app.route('/plants', methods=['POST'])
# def split_string():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             disease = data['disease']
            
#             # # Split the input string into an array of strings
#             # split_array = input_string.split()

#             result = []
#             # make a db call to get 
#             return jsonify({'result' : result})
#             # return jsonify({'result': split_array}), 200
#         except Exception as e:
#             return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
