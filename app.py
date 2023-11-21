from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def home():
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
        return render_template("graph_line.html", labels=labels, values=values)
    else:
        return "No data available."