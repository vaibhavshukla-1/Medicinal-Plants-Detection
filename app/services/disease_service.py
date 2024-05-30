# from db_models.disease import Disease
# from database.database_connection import db
# from  flask import jsonify

# class DiseaseService:

#     @staticmethod
#     def get_all_diseases_by_plant_name(plant_name):
#         diseases = Disease.query.filter_by(common_name=plant_name).all()
#         if diseases is None:
#             return jsonify({'error': 'Plant not found'}), 404
#         disease_names=[disease.disease for disease in diseases]
#         return disease_names
    
#     @staticmethod
#     def add_new_record(disease, scientific_name, common_name):
#         new_disease = Disease(disease=disease, scientific_name=scientific_name, common_name=common_name)
#         db.session.add(new_disease)
#         db.session.commit()