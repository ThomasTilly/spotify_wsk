import pandas as pd

def main(dict):
    csv_path = '../spotify-2023.csv'

    try:
        # Charger le CSV
        df = pd.read_csv(csv_path)

        # Sélectionner les colonnes requises
        columns_of_interest = ['track_name', 'artist(s)_name', 'released_year', 'streams']
        filtered_df = df[columns_of_interest]

        # Trier les données par nombre de streams en ordre décroissant
        sorted_df = filtered_df.sort_values(by='streams', ascending=False)

        # Convertir le DataFrame trié en JSON
        result_json = sorted_df.to_json(orient='records')

        return {'body': result_json}
    except Exception as e:
        return {'error': str(e)}
