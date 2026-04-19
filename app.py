from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/comparador")
def comparador():
    servicios = [
        {"nombre": "Internet", "precio": 50000},
        {"nombre": "Agua", "precio": 30000},
        {"nombre": "Energía", "precio": 45000}
    ]
    return render_template("comparador.html", servicios=servicios)

@app.route("/anomalias")
def anomalias():
    precios = [50000, 30000, 45000, 150000]  # ejemplo con un valor anómalo
    promedio = sum(precios) / len(precios)
    alertas = [p for p in precios if p > promedio * 1.5]
    return render_template("anomalias.html", promedio=promedio, alertas=alertas)

if __name__ == "__main__":
    app.run(debug=True)

