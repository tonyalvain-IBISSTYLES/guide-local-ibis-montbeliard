# AUDIT COMPLET DES LIENS – Guide local ibis Styles Montbéliard

**Date : 26 octobre 2026**  
**Périmètre : 50 fiches du guide, 56 URL externes distinctes**, avec les liens `website` / `source` et les principaux liens fixes des pages HTML.

## Méthode

- Lecture des 50 fiches du fichier `data.js` et inventaire des champs `website` et `source`.
- Consultation directe des pages d'éditeur (sites officiels), de l'Office de tourisme et des institutions avec un outil de navigation web.
- Lorsqu'une page renvoyait à une page trop générique, remplacement par une page identifiée relative au lieu.
- Analyse des boutons dans `app.js` : une fiche s'ouvre localement; les itinéraires Google Maps et les liens téléphone restent des actions distinctes.
- Tests locaux de chargement du site et vérification des liens enregistrés dans les données (voir rapports de tests).

## Évolutions incluses

1. **Chocolaterie Vergne** : la variante sans `www` était inaccessible au contrôleur; lien désormais vers `https://www.patisserie-vergne.fr/notre-maison/` et source contact dédiée.
2. **Gare TGV Belfort-Montbéliard** : remplacement de la page d'accueil SNCF par la page **précise de la gare**.
3. **Biscuiterie Billiotte** : lien vers la page de l'enseigne présentant ses magasins (dont celui de Montbéliard).
4. **Café Central, Librairie Littéra** : pages descriptives exactes au lieu de liens absents / pages génériques.
5. **Base de loisirs de Brognard, EuroVelo 6, Stade Bonal, Info Jeunes** : pages ciblées plutôt que sites d'accueil généralistes.
6. **Le Châtel, Sakura Sushi, Chez Cass’Graine, Maison Debrie, La Mie Câline, Ragot** : remplacement des références génériques par des pages précises confirmées.
7. `sources.html` synchronisé avec les liens réellement fournis par le guide.
8. Tous les itinéraires Google Maps restent disponibles depuis les fiches, même si le site d'un commerce devient indisponible.

## Ce qui est vérifié – et ce qui ne l'est pas

- **50 fiches inventoriées**; 46 ont un lien de consultation (`website`) et les autres ont une source ou une recherche cartographique.
- Les liens ont été rapprochés des pages trouvées à la date d'audit. **Ce n'est pas un contrôle en temps réel garanti sur tous les appareils** : certains hébergeurs bloquent les vérificateurs, des pages redirigent différemment, et des liens peuvent casser après notre intervention.
- Page `https://www.3237.fr/` : le contrôleur web n'a pas pu confirmer la page d'accueil (délai dépassé), mais des pages internes du service existent. Le **3237 par téléphone** reste le conseil principal pour la garde.
- Les photos externes sur Wikimedia Commons, les horaires/tarifs, les changements de gérance et les droits des images **ne font pas partie de la validation de disponibilité des sites**.
- Cette version est fondée sur le **dernier ZIP généré** du projet. L'état actuel du dépôt privé ou public GitHub n'a pas pu être lu de manière fiable pendant ce contrôle. Les nouvelles modifications devront être publiées pour être visibles aux clients.

## Conservation et entretien

Le fichier `AUDIT-LIENS-2026-10-26.csv` liste chaque fiche et ses URL. Pour vérifier régulièrement les pages depuis un ordinateur disposant d'Internet, lancer :

```
python scripts/verifier_liens.py
```

Ce programme est **un outil de prédiagnostic** : il tente d'ouvrir les URL, détecte des erreurs 404/500 et les pages d'indexation de répertoire, et marque séparément les accès bloqués ou indéterminés. Les résultats douteux doivent être ouverts manuellement dans un navigateur. Le fichier de sortie `RAPPORT-AUTO-LIENS.csv` est créé localement. En plus, le fichier `.github/workflows/verification-liens.yml` permet de lancer **un contrôle automatique chaque lundi** via GitHub Actions (onglet **Actions**). En cas de liens manifestement cassés, la tâche échoue et un CSV peut être téléchargé. Cela n'empêche pas physiquement une panne; les contrôles bloqués ou incertains restent à examiner dans un navigateur. GitHub Pages n’exécute pas ce script au moment où un client visite le guide.

Pour les prochaines mises à jour, n'éditer que `data.js` (pour les URL) puis adapter `sources.html` si le lien est exposé dans la page documentaire. Actualiser la version des scripts (`?v=`) si nécessaire.
