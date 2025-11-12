import pandas as pd

dados = {
    "Produto": ["Lápis", "Caneta", "Caderno"],
    "Preço": [2.50, 3.00, 15.00],
    "Quantidade": [10, 7, 3]
}

df = pd.DataFrame(dados)
df['Valor Total'] = df['Preço'] * df['Quantidade']
produto_mais_caro = df.loc[df['Preço'].idxmax(), 'Produto']
valor_total_estoque = df['Valor Total'].sum()

print(df)
print(f"\nProduto mais caro: {produto_mais_caro}")
print(f"Valor total em estoque: R$ {valor_total_estoque:.2f}")