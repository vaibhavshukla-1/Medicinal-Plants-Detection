# from flask import Blueprint, jsonify, request
# from ..models.plant import Plant 
# from ..database.database_connection import db

# api=Blueprint('api', __name__)

# # @api.route('/diseases', methods=['POST'])
# # def get_diseases():
# #     if request.method == 'POST':
# #         try:
# #             data = request.get_json()
# #             disease = data['disease']

# #             result = ["headache","common cold"]
# #             # make a db call to get all diseases names based on plant name

# #             return jsonify({'result' : result}) , 200
# #         except Exception as e:
# #             return jsonify({'error': str(e)}), 400
        

# # @api.route('/plants', methods=['POST'])
# # def  find_plants():
# #     if request.method == 'POST':
# #         try:
# #             data = request.get_json()
# #             disease = data['disease']

# #             result = ["tulsi","alovera"]
# #             # make a db call to get all plants names

# #             return jsonify({'result' : result})
# #         except Exception as e:
# #             return jsonify({'error': str(e)}), 400
        
        
# @api.route('/scientificname', methods=['POST'])
# def  get_scientific_name():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             disease = data['image']

#             result = "plant_name"
#             # make a ml model call to get the name of the plant based on its image

#             return jsonify({'result' : result})
#         except Exception as e:
#             return jsonify({'error': str(e)}), 400
        
# @api.route('/insertdata', methods=['POST'])
# def  insert_records_into_db():
#     if request.method == 'POST':
#         data = request.get_json()
#         scientific_name = data.get('scientific_name')
#         common_name = data.get('common_name')
#         disease = data.get('disease')

#         if scientific_name and common_name:
#             new_plant = Plant(scientific_name=scientific_name, common_name=common_name, disease=disease)
#             db.session.add(new_plant)
#             db.session.commit()
#             return jsonify({'message': 'Plant added successfully!'}), 201
#         else:
#             return jsonify({'message': 'Scientific name and common name are required fields!'}), 400
