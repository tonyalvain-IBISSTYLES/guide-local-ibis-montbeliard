# Rapport de vérification — édition du 25 octobre 2026

## Réalisé et contrôlé

- **50 fiches** structurées, dont **2 pharmacies** et **9 restaurants** ; une description présente dans chacune des quatre langues pour chaque fiche.
- **Recherche** : fonctionne sur les titres, descriptions multilingues, catégories, adresses et mots-clés ; testée avec « pharmacie » (2 résultats).
- **Catégories, secteurs, tri et favoris** : tests des interactions effectués en navigateur Chromium via un HTML de test intégré (les pages locales sont bloquées par les règles réseau de l'environnement). Les favoris sont conservés localement avec gestion des erreurs de stockage.
- **Langues** : FR, EN, DE, chinois simplifié ; bascule du texte d'interface, langue HTML, fiches et page TV.
- **Fiches** : boutons d'itinéraire piéton depuis le `21 avenue des Alliés`, panneau de détail avec horaires prudents, téléphone, source et site.
- **Mode TV** : panneau visuel, séquence automatique toutes les 8 s, pause, suivant / précédent, choix de langue, plein écran facultatif. Fonctionnement interactif testé en Chromium.
- **Mobile** : test Chromium en 390 × 844, **aucun débordement horizontal**.
- **JavaScript** : contrôle de syntaxe Node.js ; **aucune erreur JavaScript** lors des scénarios testés.
- **QR code** : régénéré depuis l'URL GitHub Pages du projet ; enregistré localement dans `images/qr-guide.png`.
- **Assets** : images SVG locales, sans dépendance à `images.unsplash.com`, sites tiers, clés API ou polices externes.
- **Sources** : chacune des fiches conserve un lien de source dans `data.js`, consigné dans `SOURCES.md` et accessible depuis `sources.html`.

## Informations importantes documentées

- Accor : ibis Styles Montbéliard Centre Velotte, `21 avenue des Alliés`, parking public Velotte, **10,50 € par jour**, ouvert **24/7**, hauteur maximale **1,90 m**, selon l'annonce en ligne de l'hôtel. Voir [Accor](https://all.accor.com/hotel/8187/index.fr.shtml). Conditions à revalider auprès de la réception.
- Temple Saint-Martin : **rouvert le 25 avril 2026**, confirmé par le [ministère de la Culture](https://www.culture.gouv.fr/regions/drac-bourgogne-franche-comte/actualite-a-la-une/temple-saint-martin-de-montbeliard-une-renaissance-apres-une-restauration-integrale). Ne signifie pas que les visites sont possibles à toute heure.
- Pharmacie du Carré Piéton : deux pages publient des horaires différents ([site 1](https://www.pharmacieducarrepieton.com/pharmacie), [site 2](https://pharmacieducarrepieton.ceido.com/)) ; ne pas annoncer d'horaire certain sans les joindre.

## Non vérifié / améliorations nécessitant une source ou autorisation externe

- **Exhaustivité absolue de tous les commerces** : non atteinte ; guide documenté avec 50 fiches et liens pour rechercher davantage.
- **Horaires détaillés de chaque commerce**, tarifs des restaurants, accessibilité complète, puissance/tarifs et état en direct des bornes, horaires des pompes à carburant : non validés exhaustivement. Aucun statut « ouvert maintenant » n'est inventé.
- **Distance et temps de marche exacts dans le site** : non calculés ; les liens Google Maps partent bien de l'adresse de l'hôtel. Les résultats exacts dépendent du tracé de l'application et de l'accessibilité réelle.
- **Photographies authentiques distinctes de chaque lieu** : non disponibles avec autorisation explicite. Utilisation transparente d'illustrations de catégories, non de fausses photos.
- **Logo officiel ibis Styles** : à insérer sur validation de la direction ; le site emploie un mot-symbole graphique sans prétendre représenter le fichier de marque officiel.
- **Vérification en navigateur sur le site GitHub Pages déployé** : impossible sans les identifiants et la publication de l'utilisateur ; tests fonctionnels réalisés en environnement local simulé.
- **Contrôle de disponibilité instantanée de chacun des liens externes** : non garanti ; le lecteur doit vérifier lors de l'ouverture.

**Conclusion :** archive complète pour publication GitHub Pages ; le rendu, l'interaction et la structure ont été testés. Ce fichier est un rapport transparent, pas une attestation d'exhaustivité locale.
