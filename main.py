from flask import Flask, request, jsonify

from mysql_setup import db
from database import KesehatanController

def setup_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/data_kesehatan'

    db.init_app(app)

    return app


app = setup_app()


@app.route('/data_kesehatan', methods=['POST'])
def insert_data_kesehatan():
    nama = request.form.get('nama')
    tgl_lahir = request.form.get('tgl_lahir')
    alamat = request.form.get('alamat')
    umur = request.form.get('umur')
    dokter = request.form.get('dokter')

    api.insert(nama, tgl_lahir, alamat, umur, dokter)

    return jsonify({'status': 'success'})


@app.route('/data_kesehatan', methods=['PUT'])
def update_data_kesehatan():
    id = request.form.get('id')
    nama = request.form.get('nama')
    tgl_lahir = request.form.get('tgl_lahir')
    alamat = request.form.get('alamat')
    umur = request.form.get('umur')
    dokter = request.form.get('dokter')

    api.update(id, nama, tgl_lahir, alamat, umur, dokter)

    return jsonify({'status': 'success'})


@app.route('/data_kesehatan/<int:id>', methods=['DELETE'])
def delete_data_kesehatan(id):
    api.delete(id)

    return jsonify({'status': 'success'})


@app.route('/data_kesehatan/<int:id>', methods=['GET'])
def get_data_kesehatan(id):
    data = api.get(id)

    return jsonify(data)


if __name__ == '__main__':
    with app.app_context():
        api = KesehatanController(db)

        app.run(debug=True)






