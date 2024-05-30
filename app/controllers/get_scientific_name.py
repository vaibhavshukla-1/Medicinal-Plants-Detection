from flask import Blueprint, jsonify, request
#from db_models.plant import Plant
#from database.database_connection import db
from services.ml_model_service import MLModelService

scientific_name = Blueprint('scientific_name', __name__)


@scientific_name.route('/scientificname', methods=['POST'])
def get_scientific_name():
    if request.method == 'POST':
        try:
            # if 'image' not in request.files:
            #     return jsonify({'error': 'No image provided'}), 400

            # image_file = request.files['image']

            # data = request.get_json()
            # disease = data['image']
            image_file = 'C:/Users/Vaibhav Shukla/Desktop/major project/tulsi.png'
            #res = "plant_name"
            res = MLModelService.find_plant_name(image_file)
            # make a ml model call to get the name of the plant based on its image
            print(res)
            return jsonify({'result': res})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
'''image_file = 'C:/Users/Vaibhav Shukla/Desktop/major project/tulsi.png'
result = "plant_name"
res = MLModelService.find_plant_name(image_file)
# make a ml model call to get the name of the plant based on its image
print(res)'''