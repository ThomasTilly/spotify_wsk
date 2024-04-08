import pandas as pd

def main(dict):
    csv_path = '../spotify-2023.csv'

    try:
        # Charger le CSV
        df = pd.read_csv(csv_path)

        # Convertir les valeurs booléennes en entiers (1 pour True, 0 pour False)
        # pour les colonnes représentant la présence dans les charts de chaque plateforme
        chart_columns = ['in_apple_charts', 'in_deezer_charts', 'in_shazam_charts', 'in_spotify_charts']
        for col in chart_columns:
            df[col] = df[col].astype(int)

        # Ajouter une colonne pour le total des présences dans les charts
        df['total_charts'] = df[chart_columns].sum(axis=1)

        # Sélectionner et trier les données
        columns_of_interest = ['track_name', 'artist(s)_name', 'total_charts', 'streams']
        filtered_sorted_df = df[columns_of_interest].sort_values(by=['total_charts', 'streams'], ascending=[False, False])

        # Convertir en JSON
        result_json = filtered_sorted_df.to_json(orient='records')

        return {'body': result_json}
    except Exception as e:
        return {'error': str(e)}
