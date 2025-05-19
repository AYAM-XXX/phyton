from pathlib import Path
import json
path = Path('numeros.json')
# nome = input("digite seu nome: ")
# contents = json.dumps(nome)

if path.exists():
    nome = path.read_text(encoding='utf-8')
    username = json.loads(nome)
    print(username)
else:
    print("não existe")