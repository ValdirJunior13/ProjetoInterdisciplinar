import pandas as pd
import openai
import nltk
from nltk.corpus import stopwords

# Lendo os dados do arquivo CSV
df = pd.read_csv("Data.csv")

# Definindo a chave de acesso da API da OpenAI
openai.api_key = "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"

# Definindo a pergunta sobre os dados do CSV
question = input("Digite o que você quer saber sobre a ufrpe: ")


# Tokenizando a pergunta do usuário
tokens = nltk.word_tokenize(question)

# Removendo stopwords (palavras comuns que não carregam muito significado)
stop_words = set(stopwords.words('portuguese'))
tokens = [word for word in tokens if word not in stop_words]

# Marcando cada token com sua respectiva classe gramatical
tagged_tokens = nltk.pos_tag(tokens)

# Selecionando apenas os substantivos e verbos
keywords = [word for word, pos in tagged_tokens if pos.startswith(
    'N') or pos.startswith('V')]

# Filtrando as linhas do dataframe que contêm links relevantes
filtered_df = df[df['links'].apply(lambda x: any(
    keyword.lower() in str(x).lower() for keyword in keywords))]

# Enviando a pergunta e recebendo a resposta usando o modelo davinci3
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question + "\n\nDados:\n" + df.to_string() + "\n\nResposta:",
    temperature=0.8,
    max_tokens=64,
    stop="\n"
)

# Extraindo os links da coluna do CSV filtrada pelo NLTK
filtered_links = filtered_df["links"].tolist()

# Concatenando os links com a resposta
answer = response["choices"][0]["text"] + "\nLinks relacionados:\n"
# Adicione essas linhas após a extração das palavras-chave
print("Palavras-chave extraídas:", keywords)

# Adicione essas linhas após a filtragem dos links relevantes
print("Links filtrados:")
for link in filtered_links:
    print(link)
# Imprimindo a resposta e os links na tela
print(answer)
for link in filtered_links:
    print(link)
