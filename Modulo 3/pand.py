import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carla"],
    "Idade": [23, 30, 27],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(dados)
# print(df)
# print("--------------------------------------------------------------")
# print(df.info())
# print("--------------------------------------------------------------")
# print(df.describe())
# print("--------------------------------------------------------------")
# print(df["Idade"])
# print("--------------------------------------------------------------")
# print(df[["Nome", "Cidade"]])
# print("--------------------------------------------------------------")
# print(df[df["Idade"] > 25])
# print("--------------------------------------------------------------")
# df["AnoNascimento"] = 2025 - df["Idade"]
# print(df)
# print("--------------------------------------------------------------")
# df_ordenado = df.sort_values(by="Idade", ascending=False)
# print(df_ordenado)
# print("--------------------------------------------------------------")
# media = df["Idade"].mean()
# print(f"Idade média: {media}")
# print("--------------------------------------------------------------")
# df = df.rename(columns={"Cidade": "Local"})
# print(df)
# print("--------------------------------------------------------------")
# print(df["Local"].value_counts())
# print("--------------------------------------------------------------")
# df = df.drop(columns=["AnoNascimento"])
# print(df)
# print("--------------------------------------------------------------")
# df.to_csv("dados_novos.csv", index=False)
# print("Arquivo salvo com sucesso!")