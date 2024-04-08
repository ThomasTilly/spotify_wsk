/**
 * Cette action logue les données relatives aux chansons Spotify.
 * Elle peut traiter les résultats de 'filterTracks.py' et 'platformsComparison.py'.
 */

function main(params) {
    // Vérifier si le body est bien formaté en JSON
    if (typeof params.body === 'string') {
        params.body = JSON.parse(params.body);
    }

    // S'assurer que les données sont présentes
    if (!params.body || params.body.length === 0) {
        console.log("Aucune donnée à afficher.");
        return { message: "Aucune donnée à afficher." };
    }

    // Afficher les données
    console.log("Données Spotify :\n");
    params.body.forEach((track, index) => {
        console.log(`Piste ${index + 1}:`);
        console.log(`Nom de la piste : ${track.track_name}`);
        console.log(`Artiste(s) : ${track['artist(s)_name'] || 'Inconnu'}`);
        console.log(`Année de sortie : ${track.released_year || 'Inconnue'}`);
        console.log(`Nombre de streams : ${track.streams || 'Inconnu'}`);
        
        // Pour les données de comparaison de plateformes
        if (track.total_charts !== undefined) {
            console.log(`Présent dans ${track.total_charts} charts de plateformes différentes`);
        }
        console.log('\n'); // Pour espacer les logs des différentes pistes
    });

    return { message: "Données Spotify loguées avec succès." };
}
