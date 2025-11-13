import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    "Funcionário": ["Alice", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena"],
    "Produtividade": [82, 74, 90, 65, 77, 88, 93, 70],
    "Horas_Semanais": [40, 36, 42, 30, 38, 44, 45, 35]
}

df = pd.DataFrame(dados)

f, ax = plt.subplots(figsize=(6, 5))

sns.set_color_codes("pastel")
sns.barplot(x="Produtividade", y="Funcionário", data=df,
            label="Produtividade", color="b") 

sns.set_color_codes("dark")
sns.barplot(x="Horas_Semanais", y="Funcionário", data=df,
            label="Horas_Semanais", color="b") 

ax.set(xlim=(0, 100), ylabel="",
       xlabel="Produtividade da Equipe (%)")
sns.despine(left=True, bottom=True)
plt.show()