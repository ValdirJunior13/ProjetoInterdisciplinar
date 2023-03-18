import openai
import csv
import pandas as pd
# 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
import openai
import pandas as pd

# Define a chave da API da OpenAI
openai.api_key = "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"

# Define o modelo da OpenAI a ser usado pelo chatbot
model_engine = "text-davinci-002"

# Abre o arquivo CSV com as informações
df = pd.read_csv("dados_uf.csv")

# Função que processa a entrada do usuário e retorna uma resposta baseada nas informações


def processar_entrada(input_text):
    input_text = input_text.lower()

    if "ufrpe" in input_text:
        resposta = df[df["informacao"] == "ufrpe"]["valor"].values[0]
    elif "matriculas" in input_text:
        resposta = "Seu número de matrícula é: {}".format(
            df[df["informacao"] == "matricula"]["valor"].values[0])
    elif "calendario" in input_text:
        resposta = df[df["informacao"] == "calendario"]["valor"].values[0]
    else:
        resposta = "Desculpe, não entendi o que você quis dizer."

    return resposta


# Loop principal do bot
while True:
    # Recebe uma entrada do usuário
    user_input = input("Usuário: ")

    # Processa a entrada do usuário e obtém a resposta baseada nas informações
    bot_response = processar_entrada(user_input)

    # Faz a chamada à API da OpenAI para obter uma resposta mais completa
    response = openai.Completion.create(
        engine=model_engine,
        prompt=bot_response,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Exibe a resposta completa do chatbot
    print("Bot: " + response.choices[0].text.strip())
