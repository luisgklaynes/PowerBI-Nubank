import pandas as pd
import random

def gerar_dados_ficticios(num_linhas, category, title, valor_min, valor_max):
    """
    Gera um DataFrame com dados fictícios.

    Args:
        num_linhas: Número de linhas a serem geradas.
        category: Lista de category possíveis.
        title: Lista de descrições possíveis.
        valor_min: Valor mínimo para a coluna "amount".
        valor_max: Valor máximo para a coluna "amount".

    Returns:
        Um DataFrame pandas com os dados gerados.
    """
    
    data = {'date': pd.date_range(start='2024-05-01', end='2024-07-31', periods=num_linhas),
            'category': random.choices(category, k=num_linhas),
            'title': random.choices(title, k=num_linhas),
            'amount': [random.uniform(valor_min, valor_max) for _ in range(num_linhas)]}
    
    df = pd.DataFrame(data)
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    return df

# Definindo as category, descrições e valores
category = ['Transporte', 'Alimentação', 'Casa', 'Lazer', 'Saúde']
title = ['Uber', 'Ônibus', 'Restaurante X', 'Aluguel', 'Cinema', 'Consulta médica']
valor_min = 5
valor_max = 200

# Gerando 500 linhas de dados
df = gerar_dados_ficticios(500, category, title, valor_min, valor_max)

# Salvando em um arquivo CSV
df.to_csv('Faturas_nubank/faturas.csv', index=False)