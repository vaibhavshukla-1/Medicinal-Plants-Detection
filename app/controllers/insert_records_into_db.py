'''from flask import Blueprint, jsonify, request
from services.disease_service import DiseaseService
from services.plant_service import PlantService

insert_records=Blueprint('insert_records', __name__)

@insert_records.route('/insertdata', methods=['POST'])
def  insert_records_into_db():
    if request.method == 'POST':
        data = request.get_json()
        scientific_name = data.get('scientific_name')
        common_name = data.get('common_name')
        disease = data.get('disease')

        if scientific_name and common_name and disease:
            PlantService.add_new_record(scientific_name,common_name,disease)
            DiseaseService.add_new_record(disease,scientific_name,common_name)
            return jsonify({'message': 'Plant and Disease added successfully!'}), 201
        else:
            return jsonify({'message': 'Scientific name and common name and disease are required fields!'}), 400'''
