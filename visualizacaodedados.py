import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuração inicial
plt.style.use('ggplot')
sns.set_palette("pastel")
os.makedirs('graficos', exist_ok=True)

# Query 1: Gênero dos leads
def plot_genero_leads():
    data = {
        "gênero": ["homens", "mulheres"],
        "leads (#)": [3500, 4200]  # Valores exemplos - substituir pelos reais
    }
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x='gênero', y='leads (#)', data=df)
    plt.title('Distribuição de Leads por Gênero')
    plt.savefig('graficos/genero_leads.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

# Query 2: Status profissional dos leads
def plot_status_profissional():
    data = {
        "status profissional": [
            "clt", "autônomo(a)", "estudante", "empresário(a)", 
            "funcionário(a) público(a)", "freelancer", "aposentado(a)", "outro"
        ],
        "leads (%)": [0.35, 0.25, 0.15, 0.08, 0.07, 0.05, 0.03, 0.02]  # Valores exemplos
    }
    df = pd.DataFrame(data).sort_values('leads (%)', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='leads (%)', y='status profissional', data=df)
    plt.title('Status Profissional dos Leads (%)')
    plt.savefig('graficos/status_profissional.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

# Query 3: Faixa etária dos leads
def plot_faixa_etaria():
    data = {
        "faixa etária": ["0-20", "20-40", "40-60", "60-80", "80+"],
        "leads (%)": [0.15, 0.35, 0.30, 0.15, 0.05]  # Valores exemplos
    }
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='faixa etária', y='leads (%)', data=df, order=df['faixa etária'])
    plt.title('Distribuição de Leads por Faixa Etária (%)')
    plt.savefig('graficos/faixa_etaria.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

# Query 4: Faixa salarial dos leads
def plot_faixa_salarial():
    data = {
        "faixa salarial": ["0-5000", "5000-10000", "10000-15000", "15000-20000", "20000+"],
        "leads (%)": [0.40, 0.30, 0.15, 0.10, 0.05],  # Valores exemplos
        "ordem": [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data).sort_values('ordem', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='faixa salarial', y='leads (%)', data=df, order=df['faixa salarial'])
    plt.title('Distribuição de Leads por Faixa Salarial (%)')
    plt.xticks(rotation=45)
    plt.savefig('graficos/faixa_salarial.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

# Query 5: Classificação dos veículos visitados
def plot_classificacao_veiculos():
    data = {
        "classificação do veículo": ["novo", "seminovo"],
        "veículos visitados (#)": [6000, 4000]  # Valores exemplos
    }
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x='classificação do veículo', y='veículos visitados (#)', data=df)
    plt.title('Veículos Visitados por Classificação')
    plt.savefig('graficos/classificacao_veiculos.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

# Query 6: Idade dos veículos visitados
def plot_idade_veiculos():
    data = {
        "idade do veículo": [
            "até 2 anos", "de 2 à 4 anos", "de 4 à 6 anos", 
            "de 6 à 8 anos", "de 8 à 10 anos", "acima de 10 anos"
        ],
        "veículos visitados (%)": [0.35, 0.25, 0.15, 0.10, 0.08, 0.07],  # Valores exemplos
        "ordem": [1, 2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data).sort_values('ordem')
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='idade do veículo', y='veículos visitados (%)', data=df)
    plt.title('Distribuição de Veículos Visitados por Idade (%)')
    plt.xticks(rotation=45)
    plt.savefig('graficos/idade_veiculos.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

# Query 7: Veículos mais visitados por marca
def plot_veiculos_mais_visitados():
    data = {
        "brand": ["Ford", "Ford", "Chevrolet", "Chevrolet", "Volkswagen", "Volkswagen", "Toyota"],
        "model": ["Fiesta", "Focus", "Onix", "Cruze", "Gol", "Polo", "Corolla"],
        "visitas (#)": [1500, 1200, 1800, 900, 2000, 1300, 1100]  # Valores exemplos
    }
    df = pd.DataFrame(data).sort_values(['brand', 'visitas (#)'], ascending=[True, False])
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x='visitas (#)', y='model', hue='brand', data=df, dodge=False)
    plt.title('Modelos Mais Visitados por Marca')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig('graficos/veiculos_visitados.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

def main():
    # Gerar todos os gráficos
    df1 = plot_genero_leads()
    df2 = plot_status_profissional()
    df3 = plot_faixa_etaria()
    df4 = plot_faixa_salarial()
    df5 = plot_classificacao_veiculos()
    df6 = plot_idade_veiculos()
    df7 = plot_veiculos_mais_visitados()
    
    # Salvar dados em CSV para referência
    df1.to_csv('graficos/dados_genero_leads.csv', index=False)
    df2.to_csv('graficos/dados_status_profissional.csv', index=False)
    df3.to_csv('graficos/dados_faixa_etaria.csv', index=False)
    df4.to_csv('graficos/dados_faixa_salarial.csv', index=False)
    df5.to_csv('graficos/dados_classificacao_veiculos.csv', index=False)
    df6.to_csv('graficos/dados_idade_veiculos.csv', index=False)
    df7.to_csv('graficos/dados_veiculos_visitados.csv', index=False)
    
    print("Análise concluída! Gráficos e dados salvos na pasta 'graficos'.")

if __name__ == "__main__":
    main()