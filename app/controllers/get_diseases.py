'''from flask import Blueprint, jsonify, request
from services.disease_service import DiseaseService

diseases=Blueprint('diseases', __name__)

@diseases.route('/diseases', methods=['POST'])
def get_diseases():
    if request.method == 'POST':

        try:
            data = request.get_json()
        
            if 'plant_name' not in data:
                return jsonify({'error': 'Plant name field is missing'}), 400
        
            plant_name = data['plant_name']

            disease_names=DiseaseService.get_all_diseases_by_plant_name(plant_name)
            return jsonify({'result': disease_names}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 400'''