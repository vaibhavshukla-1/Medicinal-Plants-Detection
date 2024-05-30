# '''from database.database_connection import db

# class Plant(db.Model):
#     __tablename__ = 'plants'

#     id = db.Column(db.Integer, primary_key=True)
#     scientific_name = db.Column(db.String(100), nullable=False)
#     common_name = db.Column(db.String(100), nullable=False)
#     disease = db.Column(db.String(100), nullable=True)

#     def __repr__(self):
#         return f"Plant(id={self.id}, scientific_name='{self.scientific_name}', common_name='{self.common_name}', disease='{self.disease}')"
