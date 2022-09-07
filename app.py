from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask(__name__)

# inisiasi obeject flask restful
api = Api(app)

# inisiasi obeject flask cors
CORS(app)


# variabel kosong
identitas = {}


# class Resource


class ContohResource(Resource):
    # method GET dan POST
    def get(self):
        response = {"msg": "Halo"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg": "data berhasil"}
        return response


# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
