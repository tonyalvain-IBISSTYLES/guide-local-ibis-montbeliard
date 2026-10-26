# Comment mettre à jour ce guide

## Mettre à jour un établissement

Ouvrez **data.js** sur GitHub, cliquez sur le crayon (Edit), recherchez l'identifiant de la fiche (par ex. `carrefour-express`), puis mettez à jour les champs correspondants :

- `name` : nom officiel et exact ; `category` : `discover`, `food`, `bakery`, `shopping`, `health`, `transport`, `parking`, `services` ou `essentials` ;
- `address` : adresse postale exacte, car elle est utilisée pour l'itinéraire à pied ;
- `description` : quatre variantes obligatoires (`fr`, `en`, `de`, `zh`) ;
- `website` : lien utile pour le client ; `source` : page où la donnée a été vérifiée ; `phone` : numéro au format international, ex. `+33381000000` ;
- `outside` : `true` si le lieu est hors centre / aux alentours, sinon `false` ;
- `hours` : un **type de note**, pas un horaire libre : `check` (à confirmer), `conflict` (sources contradictoires), `tourism` (saisonnier), `realtime` (information temps réel externe), `hotel`, `velotte`, `ev`, `market`… ;
- `verification` : choisissez `review` pour les éléments non revérifiés, `source` quand un lien justificatif existe, `confirmed` uniquement après contrôle solide ;
- `tags` : synonymes de recherche, sans publicité non validée ;
- `checked_on` : renseignez une date **uniquement si vous avez réellement contrôlé les données**.

Chaque objet doit être séparé par une virgule. Ne supprimez pas la déclaration **`window.GUIDE_PLACES =`** ni le point-virgule final. Le site ne nécessite pas d'autres modifications lorsque vous éditez une fiche correctement. Attention : les **50 fiches** de l'édition initiale ne sont pas toutes vérifiées individuellement à cette date.

## Ajouter une nouvelle fiche

Copiez un objet existant dans `data.js`, modifiez `id` (unique et sans espaces), les 4 descriptions, l'adresse et les liens, puis ajoutez-le dans le tableau. Les images affichées correspondent à la catégorie ; elles ne sont pas des photos du lieu.

## Ajouter des photos de lieux

Demandez des photos originales ou sous licence avec autorisation de diffusion sur votre site. Placez-les dans `images/`. Une **intégration technique supplémentaire dans `app.js`** est nécessaire pour afficher des images personnalisées par fiche : ajouter un champ `image`, puis lire ce champ en remplacement de l'illustration de catégorie. N'attribuez jamais une photo d'un établissement à un autre.

## Itinéraires et marche

Les liens créés par le guide utilisent Google Maps, origine `21 avenue des Alliés, 25200 Montbéliard`, mode **walking**. Les parcours, distances, temps et l'accessibilité sont calculés **par Google Maps au moment du clic**, pas par le site. Pour des minutes garanties et un itinéraire contrôlé porte-à-porte, il faudrait une solution cartographique dédiée, une validation sur le terrain et un suivi des modifications de voirie.

## Contrôles mensuels conseillés

- Retester les restaurants et leurs adresses, horaires et contacts ;
- Confirmer parking Velotte / tarif hôtel auprès de la direction ;
- Contrôler les deux pharmacies et laisser 3237 comme source de pharmacie de garde ;
- Actualiser les marchés, musées, transports et supermarchés ;
- Mettre à jour `SOURCES.md` et `VERIFICATIONS.md` et retirer les commerces définitivement fermés ;
- Ouvrir `index.html` et `tv.html` sur ordinateur et téléphone après publication.


## Mise à jour « équipe + photos » — 25 octobre 2026

Pour cette édition, remplacer sur GitHub `index.html`, `data.js`, `app.js`, `styles.css`, `translations.js` et `sources.html`. Les liens vers Wikimedia Commons affichent des photos réelles de 12 lieux ; ils ne sont pas des fichiers JPG stockés localement. Voir `PHOTOS-ET-DROITS.md` pour les crédits et `PHOTOS-A-COMPLETER.csv` pour les 38 lieux restants.
