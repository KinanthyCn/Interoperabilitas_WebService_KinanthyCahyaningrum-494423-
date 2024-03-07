from mysql_setup import db

class Data_Kesehatan(db.Model):
    __tablename__ = 'data_kesehatan'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tgl_lahir = db.Column(db.String(50))
    alamat = db.Column(db.String(50))
    umur = db.Column(db.String(50))
    dokter = db.Column(db.String(50))

    def __repr__(self):
        return f'<Data_Kesehatan {self.id}>'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'tgl_lahir': self.tgl_lahir,
            'alamat': self.alamat,
            'umur': self.umur,
            'dokter': self.dokter
        }


