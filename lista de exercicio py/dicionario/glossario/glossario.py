# Glossário: Um dicionário Python pode ser usado para modelar
# um dicionário real. Contudo,
# para evitar confusão, vamos chamá-lo de glossário.
# • Pense em cinco palavras do mundo de programação que você
# aprendeu nos capítulos
# anteriores. Use essas palavras como chaves em seu glossário e
# armazene seus significados
# como valores.
# • Exiba cada palavra e seu significado como uma saída elegantemente
# formatada. É possível até
# mesmo exibir a palavra seguida por dois-pontos e depois seu significado
# ou a palavra em uma
# linha e, em seguida, exibir seu significado indentado em uma segunda
# linha. Use o caractere
# quebra de linha(\n) para inserir uma linha em branco entre cada par
# palavra-significado em sua saída.

termos_programacao = {
    "Variável": "Espaço na memória que armazena um valor que pode mudar durante a execução do programa.",
    "Função": "Bloco de código reutilizável que executa uma tarefa específica.",
    "Loop": "Estrutura que repete um bloco de código várias vezes, como o 'for' ou 'while'.",
    "Condicional": "Estrutura que permite executar diferentes blocos de código dependendo de uma condição (ex: if/else).",
    "Classe": "Estrutura que define um tipo de objeto, contendo atributos (dados) e métodos (funções)."
}

for nome, sign in termos_programacao.items():
    print(f"{nome.upper()}: {sign}\n")
