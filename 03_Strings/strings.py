from ctypes.macholib.dyld import framework_find

tecnologia = "PYTHON"

primeira_letra = tecnologia[0]
quarta_letra = tecnologia[3]

ultima_letra = tecnologia[-1]
penultima_letra = tecnologia[-2]

print(f"primeira: {primeira_letra}, ultima: {ultima_letra}")

frase = "Desenvolvimento de Sistemas"
termo_01 = frase[0:15]
print(termo_01)
termo_02 = frase[16:]
print(termo_02)
codigo = "P1Y2T3H4O5N"
apenas_letras = codigo[0:11:2]
print(apenas_letras)

palavra = "RECURSO"
palavra_invertida = palavra[::-1]
print(palavra_invertida)

divisor = "-" * 30
print(divisor + divisor)
print("       MENU PRINCIPAL DO SISTEMA       ")
print(divisor + divisor)


codigo_id = 484

msg = "erro detectado " + str(codigo_id)

print(msg)

framework = "Django"
print(framework)
framework = "d" + framework[1:]
print(framework)

entrtada_usuario = "uSeR_nAmE@eMaIL.CoM"
email_limpo = entrtada_usuario.lower()
print(email_limpo)


nome = "luiz carlos da silva"
print(nome.capitalize())
print(nome.title())

busca = "     notebook gamer    "
print(busca.lstrip())
print(busca.rstrip())
print(busca.strip())

preco_br = "R$ 1.450,90"
print(preco_br)
preco_EUA = preco_br.replace(".", "").replace(",", ".")
print(preco_EUA)

log_erro = "ERROR: Falha na conexãp. ERROR: Timeout de resposta."

print(log_erro.find("Falha")) # indice onde começa a palavra
print(log_erro.count("ERROR"))

arquivo = "rekatorio_financieiro.csv"

if arquivo.endswith(".csv"):
    print("Iniciando a importação dos dados via planilha. ")
else:
    print("fornmato invalalido . Envie um arquivo .csv")



frase = "Python para Desenvolvimento Web"
palavra = frase.split(" ")
print(palavra)

lista_teclonogia = ["python", "Django", "FastAPI"]
resultado = "->".join(lista_teclonogia)
print(resultado)

token_seguranca = "A55B2"
print(token_seguranca.isdigit())
token_seguranca = "55"
print(token_seguranca.isdigit())
print(token_seguranca.isnumeric())
print(token_seguranca.isalpha())

comentario_suporte = "Prezados, o sistema está muito lento hoje"
if "lento" in comentario_suporte:
    print("Prioridade alta.Direcionar tickect para equipe de infraestrutura")


print("listagem de Erros: \n\t- Banco de dados offline\n\t- Falha de autenticação")

texto_analise = "Engenharia de Software"
contador_vogais = 0
voagais = "aeiouAEIOU"
for charatcter in texto_analise:
    if charatcter in voagais:
        contador_vogais += 1

print(contador_vogais)