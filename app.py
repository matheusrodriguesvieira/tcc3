from flask import Flask, request, jsonify
from ultralytics import YOLO

# Carrega o modelo YOLO v8
# Para a sua aplicação final, você pode carregar o modelo uma vez para economizar tempo
model = YOLO('yolov8n.pt')

# Inicia a aplicação Flask
app = Flask(__name__)

# Endpoint de teste
@app.route("/")
def home():
    return "API de Reconhecimento de Objetos funcionando!"

# Endpoint para processar a imagem
@app.route("/detectar-objetos", methods=["POST"])
def detectar_objetos():
    # Verifica se a requisição contém um arquivo de imagem
    if 'file' not in request.files:
        return jsonify({"sucesso": False, "mensagem": "Nenhuma imagem enviada."}), 400
    
    file = request.files['file']

    # Se o usuário não selecionar um arquivo, o navegador envia um arquivo vazio
    if file.filename == '':
        return jsonify({"sucesso": False, "mensagem": "Nenhuma imagem selecionada."}), 400

    try:
        # A lógica de processamento da imagem vai aqui.
        # Você usaria o 'model' para fazer a inferência.
        # Exemplo real:
        # results = model.predict(source=file.read())
        
        # Exemplo simulado de resposta para demonstração
        objetos = [
            {"nome": "cachorro", "confianca": 0.95},
            {"nome": "garrafa", "confianca": 0.88}
        ]

        # Retorna o JSON com os dados dos objetos
        return jsonify({
            "sucesso": True,
            "mensagem": "Objetos identificados com sucesso.",
            "objetos_detectados": objetos
        })

    except Exception as e:
        # Caso ocorra algum erro durante o processamento
        return jsonify({
            "sucesso": False,
            "mensagem": f"Erro interno: {e}",
            "objetos_detectados": []
        }), 500

if __name__ == "__main__":
    # Roda o servidor Flask em modo de depuração
    app.run(debug=True)