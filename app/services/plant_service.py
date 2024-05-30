# from database.database_connection import db
# from db_models.plant import Plant

# class PlantService:
#     @staticmethod
#     def get_plants_by_disease(disease):
#         """
#         Retrieve plants by disease.

#         Args:
#             disease (str): The disease to filter plants by.

#         Returns:
#             list: A list of plant objects matching the disease criteria.
#         """
#         plants = Plant.query.filter_by(disease=disease).all()
#         plant_names = [plant.common_name for plant in plants]
#         return plant_names

#     @staticmethod
#     def add_new_record(scientific_name, common_name, disease):
#         """
#         Add a new plant to the database.

#         Args:
#             scientific_name (str): The scientific name of the plant.
#             common_name (str): The common name of the plant.
#             disease (str): The disease that can be treated with that plant.

#         Returns:
#             Plant: The newly created plant object.
#         """
#         plant = Plant(scientific_name=scientific_name, common_name=common_name, disease=disease)
#         db.session.add(plant)
#         db.session.commit()
#         return plant

#     # @staticmethod
#     # def update_plant(plant_id, scientific_name=None, common_name=None, disease=None):
#     #     """
#     #     Update an existing plant in the database.

#     #     Args:
#     #         plant_id (int): The ID of the plant to update.
#     #         scientific_name (str, optional): The new scientific name of the plant.
#     #         common_name (str, optional): The new common name of the plant.
#     #         disease (str, optional): The new disease associated with the plant.

#     #     Returns:
#     #         Plant: The updated plant object.
#     #     """
#     #     plant = Plant.query.get(plant_id)
#     #     if scientific_name:
#     #         plant.scientific_name = scientific_name
#     #     if common_name:
#     #         plant.common_name = common_name
#     #     if disease:
#     #         plant.disease = disease
#     #     db.session.commit()
#     #     return plant

#     # @staticmethod
#     # def delete_plant(plant_id):
#     #     """
#     #     Delete a plant from the database.

#     #     Args:
#     #         plant_id (int): The ID of the plant to delete.
#     #     """
#     #     plant = Plant.query.get(plant_id)
#     #     db.session.delete(plant)
#     #     db.session.commit()
