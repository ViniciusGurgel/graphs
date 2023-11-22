from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
'''
engine = create_engine("mysql+mysqlconnector://root:Gatitcha1!@localhost/teste?charset=utf8mb4")

DB = automap_base()
DB.prepare(autoload_with=engine)
Ocorrencias = DB.classes.tb_ocorrencia
TipoOcorrencia = DB.classes.tb_tipo_ocorrencia

session_factory = sessionmaker(bind=engine)
ses = session_factory() 
'''

@app.route("/")
def home():
    '''
    result = ses.query(TipoOcorrencia.tipo_ocorrencia_nome, func.count(Ocorrencias.id_ocorrencia).label('total')).\
        join(Ocorrencias, Ocorrencias.id_tipo_ocorrencia_fk == TipoOcorrencia.id_tipo_ocorrencia).\
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
