# Daily Diet Api

API Flask para controle de dieta diária desenvolvido com Flask-SQLAlchemy, MySQL e pytest para testes automatizados.

 ## Tecnologias Utilizadas
- Flask
- Flask-SQLAlchemy
- MySQL
- Docker
- Pytest

 ## Como executar a aplicação
1. Certifique-se de ter o Python e o Docker instalados corretamente.

2. Clone este repositório:
````bash
git clone https://github.com/devnatanaelsantos/daily-diet-api.git
````

3. Instale as dependências:
````bash
pip install -r requirements.txt
````

4. Antes de iniciar o contêiner altere o caminho antes de `:/var/lib/mysql` no arquivo docker-compose.yml para uma pasta local.

5. Inicie o contêiner Docker:
````bash
docker-compose up -d
````

6. Utilize a extensão MySQL do VS Code ou outro cliente MySQL para conectar-se ao banco de dados.

7. No terminal, execute os comandos abaixo para criar as tabelas do banco de dados:
````bash
flask shell
db.create_all()
db.session.commit()
exit()
````

8. Inicie a aplicação:
````bash
python app.py
````

## Como Executar os Testes Automatizados
1. Com a aplicação em execução, abra um novo terminal, acesse o diretório do projeto e execute o comando:
```bash
pytest tests.py -v
```

## Endpoints
### Adicionar refeição
Método: POST

URL: http://127.0.0.1:5000/snack

Corpo da Requisição (JSON):

````json
{
    "name": "Almoço",
    "description": "Arroz, feijão, salada e frango",
    "dateTime": "17/05/2024-13:30",
    "check": true
}
````

Retorno esperado:
````json
{
    "message": "Refeição cadastrada com sucesso",
    "id": 1,
}
````

### Consultar todas refeições
Método: GET

URL: http://127.0.0.1:5000/snack

Retorno esperado:
````json
{
    "snacks": [
        {
            "check": true,
            "dateTime": "17/05/2024-13:30",
            "description": "Arroz, feijão, salada e frango",
            "id": 1,
            "name": "Almoço"
        }
    ],
    "total_snacks": 1
}
````

### Consultar refeição por ID
Método: GET

URL: http://127.0.0.1:5000/snack/{id}

Retorno esperado:
````json
{
    "check": true,
    "dateTime": "17/05/2024-13:30",
    "description": "Arroz, feijão, salada e frango",
    "id": 1,
    "name": "Almoço"
}
````

### Atualizar refeição
Método: PUT

URL: http://127.0.0.1:5000/snack/{id}

Corpo da Requisição (JSON):
````json
{
    "name": "Jantar",
    "description": "Arroz, batata e carne moída",
    "dateTime": "17/05/2024-19:30",
    "check": true
}
````

Retorno esperado:
````json
{
    "message": "Refeição 1 atualizada com sucesso"
}
````

### Deletar refeição
Método: DELETE

URL: http://127.0.0.1:5000/snack/{id}

Retorno esperado:
````json
{
    "message": "Refeição 1 deletada com sucesso"
}
````





