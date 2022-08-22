from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "to_do.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# DB objektas
class Uzduotis(db.Model):
    __tablename__ = "uzduotis"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    atlikta = db.Column("Atlikta", db.Boolean)

    def serialize(self):
        return {"id": self.id, "pavadinimas": self.pavadinimas, "atlikta": self.atlikta}


# Užduoties schema
class UzduotisSchema(ma.Schema):
    class Meta:
        fields = ("id", "pavadinimas", "atlikta")


uzduotis_schema = UzduotisSchema()
uzduotys_schema = UzduotisSchema(many=True)


@app.route("/uzduotis", methods=["POST"])
def prideti_uzduoti():
    db.create_all()
    pavadinimas = request.json["pavadinimas"]
    atlikta = request.json["atlikta"]
    nauja_uzduotis = Uzduotis(pavadinimas=pavadinimas, atlikta=atlikta)
    db.session.add(nauja_uzduotis)
    db.session.commit()
    return jsonify(nauja_uzduotis.serialize())


@app.route("/uzduotis", methods=["GET"])
def gauti_visas_uzduotis():
    visos_uzduotys = Uzduotis.query.all()
    rezultatas = uzduotys_schema.dump(visos_uzduotys)
    return jsonify(rezultatas)


@app.route("/uzduotis/<int:id>", methods=["GET"])
def gauti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    if uzduotis is None:
        return jsonify({"Error": "Not Found"}), 404
    else:
        return uzduotis_schema.jsonify(uzduotis)


@app.route("/uzduotis/<int:id>", methods=["PUT"])
def pakeisti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    uzduotis.pavadinimas = request.json["pavadinimas"]
    uzduotis.atlikta = request.json["atlikta"]
    db.session.commit()
    return uzduotis_schema.jsonify(uzduotis)


@app.route("/uzduotis/<int:id>", methods=["DELETE"])
def istrinti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    db.session.delete(uzduotis)
    db.session.commit()
    return uzduotis_schema.jsonify(uzduotis)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
    db.create_all()
