import pandas as pd
import json

def ler_csv_bruto(nome):
    df = pd.read_csv(nome, encoding="latin1", header=None)

    # remove linhas completamente vazias
    df = df.dropna(how="all")

    # remove colunas vazias
    df = df.dropna(axis=1, how="all")

    # reset index
    df = df.reset_index(drop=True)

    return df

# =========================
# LEITURA (SEM DEPENDER DE CABEÇALHO)
# =========================
dashboard = ler_csv_bruto("dashboard.csv")
grafico = ler_csv_bruto("grafico.csv")
fluxo = ler_csv_bruto("fluxo.csv")
compromissos = ler_csv_bruto("compromissos.csv")
alertas = ler_csv_bruto("alertas.csv")

print("OK - arquivos carregados")

# =========================
# KPI
# =========================
kpis = {}
for i in range(len(dashboard)):
    if len(dashboard.columns) >= 2:
        chave = str(dashboard.iloc[i, 0]).strip()
        valor = dashboard.iloc[i, 1]
        kpis[chave] = valor

# =========================
# GRAFICO
# =========================
labels = grafico.iloc[:, 0].tolist() if grafico.shape[1] > 0 else []
receita = grafico.iloc[:, 1].tolist() if grafico.shape[1] > 1 else []
despesas = grafico.iloc[:, 2].tolist() if grafico.shape[1] > 2 else []
lucro = grafico.iloc[:, 3].tolist() if grafico.shape[1] > 3 else []

# =========================
# FLUXO
# =========================
fluxo_dict = {}
for i in range(len(fluxo)):
    if fluxo.shape[1] >= 2:
        chave = str(fluxo.iloc[i, 0]).strip()
        valor = fluxo.iloc[i, 1]
        fluxo_dict[chave] = valor

# =========================
# COMPROMISSOS
# =========================
comp = []
for i in range(len(compromissos)):
    linha = {}
    for j in range(compromissos.shape[1]):
        linha[f"col{j}"] = compromissos.iloc[i, j]
    comp.append(linha)

# =========================
# ALERTAS
# =========================
alert = alertas.iloc[:, 0].dropna().tolist() if alertas.shape[1] > 0 else []

# =========================
# JSON FINAL
# =========================
dados = {
    "kpis": kpis,
    "grafico": {
        "labels": labels,
        "receita": receita,
        "despesas": despesas,
        "lucro": lucro
    },
    "fluxo": fluxo_dict,
    "compromissos": comp,
    "alertas": alert
}

# =========================
# SALVAR
# =========================
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("✅ FUNCIONOU - JSON GERADO SEM DEPENDER DO EXCEL")