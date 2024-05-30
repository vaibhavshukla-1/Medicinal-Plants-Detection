'''from flask import Blueprint, jsonify, request
from services.plant_service import PlantService

plants=Blueprint('plants', __name__)

@plants.route('/plants', methods=['POST'])
def  find_plants():
    if request.method == 'POST':
        try:
            data = request.get_json()
            disease = data['disease']
            
            # make a db call to get all plants names
            if 'disease' not in data:
                return jsonify({'error': 'Disease field is missing'}), 400
            
            plant_names = PlantService.get_plants_by_disease(disease)

            return jsonify({'result': plant_names})
        
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        '''
