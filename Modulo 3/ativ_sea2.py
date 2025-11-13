import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    "Cliente": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Heitor"],
    "Satisfação": [8.5, 6.0, 9.0, 7.5, 8.0, 5.5, 9.5, 7.0],
    "Categoria": ["Premium", "Básico", "Premium", "Básico", "Premium", "Básico", "Premium", "Básico"]
}


df = pd.DataFrame(dados)

plt.figure(figsize=(4, 5))
sns.violinplot(
    data=df, 
    x="Categoria",
    y="Satisfação",
    inner="quart", 
    palette={"Básico": "grey", "Premium": "green"}
)

plt.title("Satisfação por Categoria")
plt.xlabel("Categoria do Cliente")
plt.ylabel("Nível de Satisfação")
plt.show()