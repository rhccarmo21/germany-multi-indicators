# Projeto: Múltiplos Indicadores – Alemanha

## 📌 Sobre o Projeto
Este projeto tem como objetivo analisar múltiplos aspectos da sociedade alemã entre 1990 e 2017, utilizando indicadores compostos de **meio ambiente, economia, desigualdade e capital humano**. O estudo busca revelar tendências históricas, padrões de desenvolvimento sustentável e insights sobre coesão social e inovação.

O projeto faz parte de um portfólio de análises estruturadas com dados públicos e APIs, seguindo boas práticas de organização e reprodutibilidade.

---

## 🎯 Objetivos

1. Avaliar o **desacoplamento entre crescimento econômico e impacto ambiental**.
2. Investigar a **desigualdade social** e a coesão econômica da população alemã.
3. Explorar o papel do **capital humano e da inovação** na sustentação do bem-estar social.
4. Estruturar os dados de forma consistente para análises futuras e comparações internacionais.

---

## 📊 Estrutura de Diretórios

```
README.md
comparacao_tendencias_alemanha.png
dados_alemanha_1990_2017.csv
dados_ambientais_alemanha.csv
dados_completos_alemanha.csv
economia_populacao_alemanha.png
emissoes_ghg_alemanha.png
intensidade_carbono_alemanha.png
pm25_alemanha.png
---

## 📂 Indicadores Utilizados

### 1️⃣ Meio Ambiente
- PM2.5 – Exposição média (μg/m³)
- População exposta a PM2.5 (%)
- Emissões de gases de efeito estufa per capita (t CO2e)
- Intensidade de carbono do PIB (kg CO2e/PPP$)
- PIB per capita (US$)

### 2️⃣ Desigualdade e Coesão Social
- Índice de Gini
- Taxa de pobreza relativa
- Desemprego de longo prazo
- Participação no mercado de trabalho por gênero
- Distribuição de renda regional (Leste vs Oeste)

### 3️⃣ Capital Humano e Inovação
- Expectativa de vida ao nascer
- Anos médios de escolaridade
- Investimento em P&D (% do PIB)
- Exportações de alta tecnologia (% do total)
- Taxa de emprego qualificado (% da força de trabalho)

---

## 💻 Scripts

Todos os scripts foram estruturados para:

1. Consultar dados via API do Banco Mundial (`wbdata`)
2. Transformar e limpar os datasets para análise
3. Gerar gráficos e visualizações em alta qualidade
4. Salvar resultados em pastas específicas por estudo

> Exemplo de uso do script Python:
```bash
python scripts/download_indicadores.py --pais DEU --estudo ambiente
```

---

## 📊 Resultados e Visualizações

- Gráficos de séries temporais
- Correlações entre PIB, emissões e desigualdade
- Tabelas com variações percentuais e tendências históricas
- PDFs de resumo com insights estratégicos

Todos os resultados estão organizados na pasta `resultados/` de cada estudo.

---

## 📎 Download de Dados

Os arquivos CSV e gráficos podem ser baixados diretamente da pasta `dados/` e `visualizacoes/` de cada estudo, ou consultados via scripts Python com API.

---

## 📝 Observações Finais

Este projeto demonstra que é possível integrar múltiplos indicadores de diferentes dimensões (econômica, social e ambiental) em um **framework analítico unificado**, permitindo gerar insights estratégicos e comparações históricas confiáveis.

