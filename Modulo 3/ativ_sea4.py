import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Lucro": [12000, 15000, 17000, 14000, 16000, 18000, 22000, 21000, 19000, 23000, 25000, 24000]
}

df = pd.DataFrame(dados)

sns.lineplot(x="Lucro", y="Mês", marker="o",
             data=df)
plt.show()