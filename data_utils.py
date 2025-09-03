import wbdata
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações de visualização
plt.style.use('default')
sns.set_palette("husl")

def get_wb_data(country_code, indicators):
    try:
        data = wbdata.get_dataframe(indicators, country=country_code)
        data = data.reset_index()
        return data
    except Exception as e:
        print(f"❌ Erro: {e}")
        return pd.DataFrame()

# Indicadores ambientais da Alemanha
indicators_germany = {
    "EN.ATM.PM25.MC.M3": "PM2.5 - Exposição média (μg/m³)",
    "EN.ATM.PM25.MC.ZS": "PM2.5 - População exposta (%)",
    "EN.GHG.ALL.PC.CE.AR5": "Emissões GHG per capita (t CO2e)",
    "EN.GHG.CO2.RT.GDP.PP.KD": "Intensidade carbono PIB (kg CO2e/PPP$)",
    "NY.GDP.MKTP.CD": "PIB (US$)",
    "SP.POP.TOTL": "População total",
    "NY.GDP.PCAP.CD": "PIB per capita (US$)"
}

if __name__ == "__main__":
    print("🔎 Analisando dados ambientais da Alemanha...")
    df = get_wb_data("DEU", indicators_germany)
    
    # Converter ano para numérico
    df['date'] = pd.to_numeric(df['date'], errors='coerce')
    df = df.sort_values('date')
    
    # Focar no período com mais dados (1990-2017)
    df_recent = df[(df['date'] >= 1990) & (df['date'] <= 2017)].copy()
    
    # --------------------------------------------------
    # GRÁFICO 1: POLUIÇÃO PM2.5
    # --------------------------------------------------
    plt.figure(figsize=(12, 5))
    
    # PM2.5 - Exposição média
    pm25_data = df_recent.dropna(subset=['PM2.5 - Exposição média (μg/m³)'])
    plt.plot(pm25_data['date'], pm25_data['PM2.5 - Exposição média (μg/m³)'], 
             marker='o', linewidth=2.5, color='red', label='Exposição média (μg/m³)')
    
    # PM2.5 - População exposta (eixo secundário)
    ax2 = plt.gca().twinx()
    pop_data = df_recent.dropna(subset=['PM2.5 - População exposta (%)'])
    ax2.plot(pop_data['date'], pop_data['PM2.5 - População exposta (%)'], 
             marker='s', linewidth=2.5, color='orange', linestyle='--', 
             label='População exposta (%)')
    
    plt.title('Poluição por PM2.5 na Alemanha (1990-2017)\nExposição média e população acima do guideline da OMS', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Ano', fontweight='bold')
    plt.gca().set_ylabel('Exposição média (μg/m³)', fontweight='bold', color='red')
    ax2.set_ylabel('População exposta (%)', fontweight='bold', color='orange')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig('pm25_alemanha.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --------------------------------------------------
    # GRÁFICO 2: EMISSÕES DE GASES DE EFEITO ESTUFA
    # --------------------------------------------------
    plt.figure(figsize=(12, 5))
    
    # Emissões GHG per capita
    ghg_data = df_recent.dropna(subset=['Emissões GHG per capita (t CO2e)'])
    plt.plot(ghg_data['date'], ghg_data['Emissões GHG per capita (t CO2e)'], 
             marker='^', linewidth=2.5, color='green', label='Emissões GHG per capita')
    
    plt.title('Emissões de Gases de Efeito Estufa na Alemanha (1990-2017)\nEmissões per capita em toneladas de CO2 equivalente', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Ano', fontweight='bold')
    plt.ylabel('Emissões GHG per capita (t CO2e)', fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('emissoes_ghg_alemanha.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --------------------------------------------------
    # GRÁFICO 3: INTENSIDADE DE CARBONO DA ECONOMIA
    # --------------------------------------------------
    plt.figure(figsize=(12, 5))
    
    # Intensidade de carbono do PIB
    carbon_data = df_recent.dropna(subset=['Intensidade carbono PIB (kg CO2e/PPP$)'])
    plt.plot(carbon_data['date'], carbon_data['Intensidade carbono PIB (kg CO2e/PPP$)'], 
             marker='d', linewidth=2.5, color='purple', label='Intensidade de carbono')
    
    plt.title('Intensidade de Carbono da Economia Alemã (1990-2017)\nEmissões de CO2 por unidade de PIB (PPC)', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Ano', fontweight='bold')
    plt.ylabel('Intensidade de carbono (kg CO2e/PPP$)', fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('intensidade_carbono_alemanha.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --------------------------------------------------
    # GRÁFICO 4: CRESCIMENTO ECONÔMICO E DEMOGRÁFICO
    # --------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # PIB per capita
    gdp_data = df_recent.dropna(subset=['PIB per capita (US$)'])
    ax1.plot(gdp_data['date'], gdp_data['PIB per capita (US$)']/1000, 
             marker='o', linewidth=2.5, color='blue', label='PIB per capita')
    ax1.set_title('Crescimento Econômico da Alemanha (1990-2017)', fontweight='bold')
    ax1.set_ylabel('PIB per capita (mil US$)', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # População
    pop_data = df_recent.dropna(subset=['População total'])
    ax2.plot(pop_data['date'], pop_data['População total']/1e6, 
             marker='s', linewidth=2.5, color='brown', label='População')
    ax2.set_title('Evolução Demográfica da Alemanha (1990-2017)', fontweight='bold')
    ax2.set_xlabel('Ano', fontweight='bold')
    ax2.set_ylabel('População (milhões)', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.suptitle('Desempenho Econômico e Demográfico da Alemanha\n(1990-2017)', 
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('economia_populacao_alemanha.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --------------------------------------------------
    # GRÁFICO 5: COMPARAÇÃO DE TENDÊNCIAS (NORMALIZADO)
    # --------------------------------------------------
    plt.figure(figsize=(12, 6))
    
    # Normalizar dados para comparar tendências (1990 = 100)
    for col in ['PM2.5 - Exposição média (μg/m³)', 'Emissões GHG per capita (t CO2e)',
                'Intensidade carbono PIB (kg CO2e/PPP$)']:
        col_data = df_recent.dropna(subset=[col]).copy()
        if len(col_data) > 0:
            base_value = col_data[col].iloc[0]
            col_data[f'{col}_norm'] = (col_data[col] / base_value) * 100
            plt.plot(col_data['date'], col_data[f'{col}_norm'], 
                     marker='o', linewidth=2.5, label=col.split(' - ')[0] if ' - ' in col else col)
    
    plt.title('Evolução Comparada dos Indicadores Ambientais da Alemanha (1990-2017)\nValores normalizados (1990 = 100)', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Ano', fontweight='bold')
    plt.ylabel('Índice (1990 = 100)', fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('comparacao_tendencias_alemanha.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --------------------------------------------------
    # ANÁLISE ESTATÍSTICA
    # --------------------------------------------------
    print("\n📊 ANÁLISE ESTATÍSTICA - ALEMANHA (1990-2017)")
    print("=" * 50)
    
    # Calcular variação percentual para cada indicador
    trends = {}
    for col in ['PM2.5 - Exposição média (μg/m³)', 'PM2.5 - População exposta (%)',
                'Emissões GHG per capita (t CO2e)', 'Intensidade carbono PIB (kg CO2e/PPP$)',
                'PIB per capita (US$)']:
        col_data = df_recent.dropna(subset=[col])
        if len(col_data) > 1:
            initial = col_data[col].iloc[0]
            final = col_data[col].iloc[-1]
            change = ((final - initial) / initial) * 100
            trends[col] = change
            print(f"{col:40s}: {initial:6.1f} → {final:6.1f} ({change:+.1f}%)")
    
    # Salvar dados
    df_recent.to_csv('dados_alemanha_1990_2017.csv', index=False)
    print(f"\n💾 Dados salvos em 'dados_alemanha_1990_2017.csv'")
    
    print("\n🎯 PRINCIPAIS CONCLUSÕES:")
    print("   • Gráficos individuais gerados para cada categoria")
    print("   • Período de análise: 1990-2017 (dados mais completos)")
    print("   • Tendências calculadas com variações percentuais")
    print("   • Visualizações salvas em arquivos PNG de alta qualidade")
