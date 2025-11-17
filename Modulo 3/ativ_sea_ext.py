import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
"Áreas": [
    "Programação básico", "Inglês básico", "Conhec. gerais", "Comun. Profissional", "Criatividade", "Adaptabilidade", "Pensamento Lógico", "Res. de Problemas", "Org. de Tarefas", "Aprendizado Contínuo"
],
    "Nível de Proficiência": [72, 55, 67, 50, 87, 65, 84, 73, 75, 89]
}

df = pd.DataFrame(dados)

sns.barplot(x="Áreas", y="Nível de Proficiência", data=df, palette="crest")

plt.title("Comparação Profissional da Nan")
plt.show()