import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Listas fictícias
tipos_imovel = ["Apartamento", "Casa", "Cobertura", "Studio", "Flat"]
padroes = ["Econômico", "Médio Padrão", "Alto Padrão", "Luxo"]
estados = ["SP", "RJ", "MG", "PR", "RS", "DF", "GO", "PE"]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Brasília", "Goiânia", "Recife"]
bairros = ["Copacabana", "Itaim Bibi", "Moema", "Barra da Tijuca", "Centro", "Jardins", "Boa Viagem"]
nome_predios = ["Edifício Solar", "Residencial Lua", "Condomínio Estrela", "Torre Aurora", "Jardins do Horizonte"]

# Função para gerar preços
def gerar_preco(padrao):
    precos = {"Econômico": (150000, 300000), "Médio Padrão": (300000, 700000), 
              "Alto Padrão": (700000, 1500000), "Luxo": (1500000, 5000000)}
    return np.random.randint(*precos[padrao])

# Base de Imóveis
base_imoveis = pd.DataFrame({
    "ID Imóvel": [f"IM{str(i).zfill(4)}" for i in range(1, 501)],
    "Tipo": np.random.choice(tipos_imovel, 500),
    "Nome do Prédio": np.random.choice(nome_predios, 500),
    "Padrão": np.random.choice(padroes, 500, p=[0.4, 0.3, 0.2, 0.1]),
    "Quartos": np.random.randint(1, 6, 500),
    "Banheiros": np.random.randint(1, 4, 500),
    "Metragem": np.random.randint(50, 201, 500),
    "Garagem": np.random.randint(1, 4, 500),
    "Cidade": np.random.choice(cidades, 500),
    "Bairro": np.random.choice(bairros, 500),
    "Estado": np.random.choice(estados, 500),
    "Preço": [gerar_preco(p) for p in np.random.choice(padroes, 500)]
})

# Clientes fictícios
nomes = ["Carlos Silva", "Mariana Souza", "Pedro Oliveira", "Fernanda Lima", "João Mendes"]
renda_min, renda_max = 3000, 30000

# Vendas detalhadas
datas_vendas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
vendas = pd.DataFrame({
    "ID Venda": [f"V{str(i).zfill(4)}" for i in range(1, 301)],
    "Data da Venda": np.random.choice(datas_vendas, 300),
    "ID Imóvel": np.random.choice(base_imoveis["ID Imóvel"], 300),
    "Cliente": np.random.choice(nomes, 300),
    "Renda Mensal": np.random.randint(renda_min, renda_max, 300),
    "Financiado": np.random.choice(["Sim", "Não"], 300, p=[0.7, 0.3]),
    "Entrada (R$)": np.random.randint(20000, 200000, 300),
    "Parcelas": np.random.randint(12, 360, 300),
    "Taxa de Juros (%)": np.round(np.random.uniform(3, 10, 300), 2),
})

# Índices Financeiros
indices_financeiros = pd.DataFrame({
    "Data": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "Taxa Selic (%)": np.round(np.random.uniform(6, 15, 12), 2),
    "IPCA (%)": np.round(np.random.uniform(2, 10, 12), 2),
    "IGP-M (%)": np.round(np.random.uniform(-1, 8, 12), 2),
})

# Exportar para CSV
base_imoveis.to_csv("base_imoveis.csv", index=False)
vendas.to_csv("tabela_vendas.csv", index=False)
indices_financeiros.to_csv("indices_financeiros.csv", index=False)

print("Arquivos CSV gerados com sucesso!")
