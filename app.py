from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''
app.config['DATABASE'] = ''
db = SQLAlchemy(app)

class TipoOcorrencia(db.Model):
    __tablename__ = 'tb_tipo_ocorrencia'

    id_tipo_ocorrencia = db.Column(db.Integer, primary_key=True)
    tipo_ocorrencia_nome = db.Column(db.String(45), unique=True)
    # Add other columns as needed

class Ocorrencia(db.Model):
    __tablename__ = 'tb_ocorrencia'

    id_ocorrencia = db.Column(db.Integer, primary_key=True)
    id_tipo_ocorrencia_fk = db.Column(db.Integer, db.ForeignKey('tb_tipo_ocorrencia.id_tipo_ocorrencia'))
'''



@app.route("/")
def home():
    '''
    result = db.session.query(TipoOcorrencia.tipo_ocorrencia_nome, db.func.count(Ocorrencia.id_ocorrencia).label('total')).\
        join(Ocorrencia, Ocorrencia.id_tipo_ocorrencia_fk == TipoOcorrencia.id_tipo_ocorrencia).\
        group_by(TipoOcorrencia.tipo_ocorrencia_nome).all()
    labels = [row.tipo_ocorrencia_nome for row in result]
    values = [row.total for row in result]
    '''

    data = [
        ("Acidente de Transito",3),
        ("Assédio",2),
        ("Desaparecimento",1),
        ("Furtos",2),
        ("Lesão Corporal",3),
        ("Extravio/Perda",1),
        ("Fraudes e Apropriacoes",4),
        ("Brigas e ameacas",2),
        ("Manutenção",7),
        ("Danos a instalações",3),
        ("Problemas de infraestrutura",6),
        ("Outros",8),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    if labels and values:
        return render_template("graph_bar.html", labels=labels, values=values)
    else:
        return "No data available."
