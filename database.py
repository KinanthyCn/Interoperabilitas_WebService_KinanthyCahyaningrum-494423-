from Modela.data_kesehatan import Data_Kesehatan

class KesehatanController:
    def __init__(self, db):
        self.db = db

    def insert(self, name, tgl_lahir, alamat,umur, dokter):
        new_data = Data_Kesehatan(name=name, tgl_lahir=tgl_lahir, alamat=alamat, umur=umur, dokter=dokter)
        self.db.session.add(new_data)
        self.db.session.commit()

    def update(self, id, name, tgl_lahir, alamat,umur, dokter):
        data = Data_Kesehatan.query.get(id)
        data.name = name
        data.tgl_lahir = tgl_lahir
        data.alamat = alamat
        data.umur = umur
        data.dokter = dokter
        self.db.session.commit()

    def delete(self, id):
        data = Data_Kesehatan.query.get(id)
        self.db.session.delete(data)
        self.db.session.commit()

    def get(self, id) -> dict:
        data = Data_Kesehatan.query.get(id)
        return data.to_dict()
