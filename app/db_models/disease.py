'''from database.database_connection import db

class Disease(db.Model):
    __tablename__ = 'diseases'

    id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100), nullable=False)
    common_name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Disease(id={self.id}, scientific_name='{self.scientific_name}', disease='{self.disease}', common_name='{self.common_name}')"
'''