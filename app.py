from flask import Flask, request, jsonify
from database import db
from datetime import datetime
from models.snack import Snack

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3307/data-base"

db.init_app(app)

@app.route("/snack", methods=['POST'])
def create_snack():
    data = request.json
    dateTime_str = data.get('dateTime')

    if not data.get('name') or data.get('check') is None:
        return jsonify({"message": "Campos obrigatórios ausentes: nome, check."})

    try:
        if dateTime_str:
            dateTime = datetime.strptime(dateTime_str, "%d/%m/%Y-%H:%M")
        else:
            dateTime = datetime.now()
    except ValueError:
        return jsonify({"message": "Formato de data hora inválido, esperado 'dd/mm/yyyy-hh:mm'"})

    
    new_snack = Snack(name=data['name'], description=data.get('description', ""), dateTime=dateTime, check=data['check'])
    db.session.add(new_snack)
    db.session.commit()

    return jsonify({"message": "Refeição cadastrada com sucesso!"})

@app.route("/snack", methods=['GET'])
def get_snacks():
    snacks = Snack.query.all()
    snacks_list = []

    for snack in snacks:
        snacks_list.append({
            'id': snack.id,
            'name': snack.name,
            'description': snack.description,
            'dateTime': snack.dateTime.strftime("%d/%m/%Y-%H:%M"),
            'check': snack.check
        })
    
    output = {
        "snacks": snacks_list,
        "total_snacks": len(snacks_list)
    }

    return jsonify(output)

@app.route("/snack/<int:id_snack>", methods=['GET'])
def get_snack(id_snack):
    snack = Snack.query.get(id_snack)

    if snack:
        output = ({
            "nome": snack.name,
            "description": snack.description,
            "dataTime": snack.dateTime.strftime("%d/%m/%Y-%H:%M"),
            "check": snack.check
        })
        return jsonify (output)

    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/snack/<int:id_snack>", methods=['PUT'])
def update_snack(id_snack):
    snack = Snack.query.get(id_snack)

    if snack:
        data = request.json
        dateTime_str = data.get('dateTime')

        try:
            if dateTime_str:
                dateTime = datetime.strptime(dateTime_str, "%d/%m/%Y-%H:%M")
            else:
                dateTime = datetime.now()
        except ValueError:
            return jsonify({"message": "Formato de data hora inválido, esperado 'dd/mm/yyyy-hh:mm'"})
        
        snack.name = data.get("name")
        snack.description = data.get("description")
        snack.dateTime = dateTime
        snack.check = data.get("check")
        db.session.commit()

        return jsonify({"message": f"Refeição {id_snack} atualizada com sucesso"})

    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/snack/<int:id_snack>", methods=['DELETE'])
def delete_scank(id_snack):
    snack = Snack.query.get(id_snack)

    if snack:
        db.session.delete(snack)
        db.session.commit()

        return jsonify ({'message': f"Refeição {id_snack} deletada com sucesso"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)