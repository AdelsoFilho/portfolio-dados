import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuração inicial
np.random.seed(42)  # Para reproducibilidade

# Listas de valores fictícios
regioes = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Brasília"]
canais_venda = ["Online", "Presencial", "Corretor Parceiro"]
tipos_campanha = ["Google Ads", "Facebook Ads", "Feirão Presencial", "Corretores Parceiros"]
nomes_predios = ["Edifício Solar", "Residencial Lua", "Condomínio Estrela", "Torre Aurora", "Jardins do Horizonte"]

# Função para gerar preços com base no padrão
def gerar_preco(padrao):
    if padrao == "Econômico":
        return np.random.randint(150000, 300001)
    elif padrao == "Médio Padrão":
        return np.random.randint(300000, 700001)
    elif padrao == "Alto Padrão":
        return np.random.randint(700000, 1500001)
    elif padrao == "Luxo":
        return np.random.randint(1500000, 5000001)

# Função para gerar descontos com base no canal de venda
def gerar_desconto(canal):
    if canal == "Corretor Parceiro":
        return np.random.uniform(0.1, 0.15)  # Descontos maiores para corretores
    else:
        return np.random.uniform(0, 0.1)  # Descontos menores para outros canais

# 1. Tabela de Vendas
datas_vendas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
vendas = pd.DataFrame({
    "Data da Venda": np.random.choice(datas_vendas, size=500),  # 500 vendas ao longo do ano
    "Apartamento": ["AP" + str(i).zfill(3) for i in range(1, 501)],
    "Nome do Prédio": np.random.choice(nomes_predios, size=500),
    "Padrão": np.random.choice(["Econômico", "Médio Padrão", "Alto Padrão", "Luxo"], size=500, p=[0.4, 0.3, 0.2, 0.1]),
    "Número de Quartos": np.random.randint(1, 6, size=500),
    "Número de Banheiros": np.random.randint(1, 4, size=500),
    "Metragem (m²)": np.random.randint(50, 201, size=500),
    "Vagas de Garagem": np.random.randint(1, 4, size=500),
    "Canal de Venda": np.random.choice(canais_venda, size=500),
    "Região": np.random.choice(regioes, size=500)
})

# Aplicar preços e descontos
vendas["Preço Unitário"] = vendas["Padrão"].apply(gerar_preco)
vendas["Desconto Aplicado"] = vendas["Canal de Venda"].apply(gerar_desconto)
vendas["Total da Venda"] = vendas["Preço Unitário"] * (1 - vendas["Desconto Aplicado"])

# 2. Tabela de Marketing
campanhas = pd.DataFrame({
    "Campanha": ["Campanha " + str(i) for i in range(1, 11)],
    "Tipo de Campanha": np.random.choice(tipos_campanha, size=10),
    "Data Início": pd.date_range(start="2023-01-01", periods=10, freq="M"),
    "Data Fim": pd.date_range(start="2023-02-01", periods=10, freq="M") + timedelta(days=np.random.randint(30, 90)),
    "Investimento Total": np.random.randint(10000, 500001, size=10),
    "Custo por Clique (CPC)": np.round(np.random.uniform(1, 10, size=10), 2),
    "Cliques": np.random.randint(1000, 50001, size=10),
    "Conversões": np.random.randint(10, 501, size=10)
})
campanhas["ROI"] = np.round((campanhas["Conversões"] * 100000) / campanhas["Investimento Total"], 2)  # ROI fictício

# 3. Tabela de Estoque
estoque = pd.DataFrame({
    "Apartamento": ["AP" + str(i).zfill(3) for i in range(1, 101)],
    "Nome do Prédio": np.random.choice(nomes_predios, size=100),
    "Padrão": np.random.choice(["Econômico", "Médio Padrão", "Alto Padrão", "Luxo"], size=100, p=[0.4, 0.3, 0.2, 0.1]),
    "Número de Quartos": np.random.randint(1, 6, size=100),
    "Número de Banheiros": np.random.randint(1, 4, size=100),
    "Metragem (m²)": np.random.randint(50, 201, size=100),
    "Vagas de Garagem": np.random.randint(1, 4, size=100),
    "Quantidade Disponível": np.random.randint(5, 51, size=100),
    "Preço de Custo": [gerar_preco(padrao) * 0.7 for padrao in np.random.choice(["Econômico", "Médio Padrão", "Alto Padrão", "Luxo"], size=100)],  # 70% do preço de venda
    "Quantidade Vendida": np.random.randint(0, 20, size=100),
    "Quantidade Reabastecida": np.random.randint(0, 10, size=100)
})

# Exportar para CSV
vendas.to_csv("tabela_vendas.csv", index=False)
campanhas.to_csv("tabela_marketing.csv", index=False)
estoque.to_csv("tabela_estoque.csv", index=False)

print("Arquivos CSV gerados com sucesso!")