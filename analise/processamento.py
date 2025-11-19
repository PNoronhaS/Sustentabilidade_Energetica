import pandas as pd
from utils.simulador import aplicar_ajuste

def carregar_dados(caminho_csv: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_csv)
    df['Dia'] = pd.to_datetime(df['Dia'])
    return df

def analisar_consumo(df: pd.DataFrame) -> dict:
    total = df['Consumo_kWh'].sum()
    media = df['Consumo_kWh'].mean()
    pico = df['Consumo_kWh'].max()
    dia_pico = df.loc[df['Consumo_kWh'].idxmax(), 'Dia']
    return {
        'total_kwh': total,
        'media_kwh': media,
        'pico_kwh': pico,
        'dia_pico': dia_pico.date(),
    }

def simular_economia(df: pd.DataFrame, reducao_percentual=10, fator_emissao_kg_por_kwh=0.10) -> dict:
    df['Consumo_Ajustado'] = df['Consumo_kWh'].apply(
        lambda x: aplicar_ajuste(x, reducao_percentual)
    )
    economia_kwh = (df['Consumo_kWh'] - df['Consumo_Ajustado']).sum()
    economia_percent = economia_kwh / df['Consumo_kWh'].sum() * 100

    # Impacto ambiental
    co2_evitable_kg = economia_kwh * fator_emissao_kg_por_kwh
    co2_evitable_ton = co2_evitable_kg / 1000

    return {
        'economia_kwh': economia_kwh,
        'economia_percent': economia_percent,
        'co2_evitable_kg': co2_evitable_kg,
        'co2_evitable_ton': co2_evitable_ton,
        'fator_emissao_kg_por_kwh': fator_emissao_kg_por_kwh,
        'df_ajustado': df,
    }
