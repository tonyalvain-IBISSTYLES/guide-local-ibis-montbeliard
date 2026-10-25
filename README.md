# Guide local numérique · ibis Styles Montbéliard Centre Velotte

**Édition du 25 octobre 2026** — Site statique, compatible GitHub Pages. Pas d'installation ni de base de données.

## Mise en ligne GitHub Pages, en français

1. **Décompressez** l'archive ZIP. **N'envoyez pas le ZIP tel quel dans le dépôt**.
2. Ouvrez votre dépôt : **https://github.com/tonyalvain-ibisstyles/guide-local-ibis-montbeliard**.
3. Cliquez sur **Add file** → **Upload files** (ou sur « Ajouter un fichier » → « Téléverser des fichiers » selon l'affichage GitHub).
4. Faites glisser **tout le contenu du dossier décompressé**, y compris `index.html`, `app.js`, `data.js`, `styles.css`, `translations.js`, `tv.html`, les fichiers `.md`, `.nojekyll` et **tout le dossier `images`**. Les fichiers doivent être à la **racine du dépôt** : pas dans un sous-dossier supplémentaire.
5. Validez avec le bouton vert **Commit changes** / « Valider les modifications » en bas de la page. Si GitHub le propose, remplacez les anciens fichiers portant le même nom. **Ne supprimez pas** un éventuel fichier de configuration personnalisé dont vous avez besoin sans avoir vérifié son rôle.
6. Ouvrez **Settings** → **Pages**. Dans **Build and deployment** : choisissez **Deploy from a branch**, branche **main**, répertoire **/(root)**, puis **Save**. Si c'est déjà configuré, ne changez rien.
7. Ouvrez **https://tonyalvain-ibisstyles.github.io/guide-local-ibis-montbeliard/**, puis vérifiez sur un téléphone, idéalement en navigation privée ou après actualisation forcée (`Ctrl+F5`).
8. Pour l'écran TV : **https://tonyalvain-ibisstyles.github.io/guide-local-ibis-montbeliard/tv.html**. Pour passer en plein écran, utilisez le bouton ⛶ de la page ou `F11` dans le navigateur.

**Si GitHub refuse le transfert de dossiers** : depuis Windows, ouvrez le dossier décompressé et sélectionnez **tous les éléments** (fichiers et le dossier `images`) avant de les déposer dans la zone d'envoi GitHub. Ne déposez pas uniquement le dossier parent. Le nom doit être `index.html` exactement, et non `index.htlm` ou `index.html.txt`.

## Structure

```text
index.html                 Page principale, à conserver à la racine
styles.css                 Design responsive
app.js                     Recherche, favoris, filtres, itinéraires, détail
translations.js            Textes FR / EN / DE / 中文
 data.js                   50 fiches de lieux et services
tv.html                    Affichage TV avec défilement de panneaux
images/                    QR code et illustrations SVG locales
.nojekyll                  Désactive le traitement Jekyll sur GitHub Pages
SOURCES.md                 Liste des liens de sources
VERIFICATIONS.md           Bilan des vérifications et points restant à confirmer
MISE-A-JOUR.md             Instructions pour maintenir les fiches
robots.txt, sitemap.xml    Référencement de base
```

## Fonctionnement

- **50 fiches** au lancement, dont exactement **2 pharmacies**.
- **4 langues** : français, anglais, allemand et chinois simplifié.
- Recherche dans les quatre langues, les adresses et les mots-clés ; catégories, filtres par secteur, tri par nom/catégorie.
- **Favoris** conservés dans ce navigateur (sans compte, sans serveur) ; lien direct Google Maps **à pied au départ du 21 avenue des Alliés**.
- Accès téléphone, site et source dans le panneau « Détails » ; encarts pour hôtel, urgence, pharmacie de garde, transports et parking Velotte.
- QR code menant directement à l'URL publique du guide ; version TV autonome (images locales, sans connexion aux réseaux sociaux).

## Limites à connaître

**Ce guide n'est pas un annuaire exhaustif et les horaires ne sont pas suivis en temps réel.** Il ne calcule pas les distances / durées à pied dans la page : **Google Maps les calcule quand le visiteur ouvre l'itinéraire**. Certaines données de commerces doivent être revérifiées avant une communication présentée comme officielle. Les visuels sont des **illustrations de catégories** — pas des photographies des établissements. Le traitement de texte de la marque est une composition graphique **non officielle**, à remplacer uniquement par un logo fourni et autorisé par l'hôtel.

Vous pouvez modifier les fiches dans `data.js` en conservant strictement le format JavaScript/JSON ; voir [MISE-A-JOUR.md](MISE-A-JOUR.md). Les auteurs du guide restent responsables de la validation locale des tarifs et des recommandations dites « coups de cœur de l'équipe ».
