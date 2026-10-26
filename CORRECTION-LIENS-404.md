# Correctif liens commerçants — 26 octobre 2026

## Signalement client
Des utilisateurs obtenaient des erreurs 404 / pages inaccessibles après avoir cliqué sur « Site / détails » depuis des fiches de commerçants.

## Cause identifiée
Certains liens externes fournis par le guide ne sont plus les sites valides des établissements, ou ne sont pas accessibles avec leur forme `www`. Le guide n’est pas lui-même en erreur 404. Le comportement des services tiers peut varier selon le navigateur.

## Corrections apportées

- Le Châtel : ancien `restaurant-lechatel.fr` remplacé par `https://le-chatel.eu/` (site identifié).
- La Pause Gourmande : ancien `lapausegourmande.net` inaccessible ; remplacé par la **fiche de l’Office de tourisme**, identifiée comme telle (pas comme le site officiel du restaurant).
- Ho’Plats Gourmands : lien rectifié en `https://hoplats-gourmands.com/` (sans www).
- Signorizza : lien générique remplacé par la fiche spécifique de l’Office de tourisme, avec libellé adapté ; le site de marque était inaccessible lors de la vérification.
- La Tentation : ajout du site officiel `https://restaurant-latentation.fr/`.
- Chez Witt : ajout de la page d'établissement `https://chez-witt-montbeliard.metro.bar/?lang=fr`.
- La Mie Câline : lien remplacé par la page du magasin Montbéliard.
- E.Leclerc : lien remplacé par la page précise du magasin Montbéliard.

## Améliorations pour éviter les confusions

1. Le bouton de la carte s’appelle maintenant **« Voir la fiche »** : il ouvre un panneau **dans notre propre guide**, sans lien extérieur.
2. Les liens externes sont explicitement nommés **« Site officiel »** ou **« Fiche du commerce (Tourisme) »** selon leur nature.
3. Chaque restaurant, pâtisserie et commerce possède un bouton **« Retrouver ce commerce sur Google Maps »** indépendant du site du commerçant.
4. Les quatre langues sont mises à jour.
5. Le numéro de version des scripts a changé pour éviter que le navigateur conserve l’ancien `data.js`.
6. Les fichiers images et les 50 fiches sont conservés.

## Limite
Il n’est pas possible de garantir à vie l’accès à un site tiers. Des sites peuvent changer d’adresse, bloquer certains visiteurs ou fermer. Les nouvelles URL ci-dessus ont été identifiées dans les résultats de sites éditeurs et de l’Office de tourisme au 26/10/2026. Pour un lien externe en panne, l’utilisateur peut toujours ouvrir la fiche du lieu dans notre guide et son bouton Google Maps.

## Publication GitHub Pages

1. Décompresser `Mise_A_Jour_Liens_Commercants_404.zip`.
2. Importer **tous les fichiers contenus** (`index.html`, `data.js`, `app.js`, `translations.js`, `sources.html`, et documents éventuels) via `Add file > Upload files` à la racine du dépôt, branche `main`.
3. Cliquer sur `Commit changes`.
4. Vérifier `Actions` pour le déploiement réussi, puis actualiser avec `Ctrl+F5` ou en navigation privée.
5. Tester au minimum Le Châtel, La Pause Gourmande, Ho’Plats Gourmands, La Tentation, Chez Witt, Signorizza, La Mie Câline et E.Leclerc.

Le dossier `images` n’a pas besoin d’être rechargé pour **cette seule correction**.
