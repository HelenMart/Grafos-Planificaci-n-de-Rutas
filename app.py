from flask import Flask, render_template, request, jsonify
from dijkstra import dijkstra, build_graph

app = Flask(__name__)
graph = build_graph("routes.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/planificar", methods=["POST"])
def planificar():
    data = request.json
    origen = data["origen"]
    destino = data["destino"]
    ruta, distancia = dijkstra(graph, origen, destino)
    return jsonify({"ruta": ruta, "distancia": distancia})

if __name__ == "__main__":
    app.run(debug=True)