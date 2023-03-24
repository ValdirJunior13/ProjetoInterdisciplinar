# 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
import openai
import csv

# Substitua "sk-..." pela sua chave de API secreta
openai.api_key = "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"

# Escolha um modelo da open ai (por exemplo, davinci)
model = "text-davinci-002"

# Leia o arquivo CSV usando o módulo csv do python
with open("Data.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    data = []
    links = []
    for i, row in enumerate(reader):
        if i == 0:
            continue  # ignora a primeira linha (cabeçalho)
        parts = row[1].split(',')
        data.append(parts[0])
        links.append(parts[1])

# Crie uma função que recebe uma pergunta do usuário e gera um texto usando o modelo da open ai


def generate_text(question):
    # Construa a entrada para a API da open ai com os dados do CSV e a pergunta do usuário
    input = "Dados:\n"
    for i in range(len(data)):
        input += f"{data[i]} - {links[i]}\n"
    input += f"\nPergunta: {question}\n\nResposta:"

    # Envie uma requisição para a API da open ai com os parâmetros desejados
    response = openai.Completion.create(
        engine=model,
        prompt=input,
        temperature=0.5,
        max_tokens=00,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    # Obtém a resposta gerada pelo modelo
    answer = response["choices"][0]["text"]

    # Procura o link correspondente à linha da coluna que foi usada para a resposta no CSV
    link = ""
    for i in range(len(data)):
        if data[i] in answer:
            link = links[i]
            break

    # Concatena a resposta e o link, se houver
    if link:
        answer += f" (Fonte: {link})"

    return answer


# Testa a função com uma pergunta de exemplo
while True:
    question = input("Digite uma pergunta: ")
    if question == "quit":
        break
    answer = generate_text(question)
    print(answer)
