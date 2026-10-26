# CORRECTIF PHOTOS — 26 octobre 2026

## Ce qui a été corrigé

Le précédent petit ZIP « audit 50 liens » ne contenait **aucune** image. Les photos du guide étaient pourtant stockées dans le dossier `images/` du ZIP complet.

Cette mise à jour contient `photo-cache.js` : une copie optimisée et intégrée des **43 médias locaux** (dont 32 images WebP/PNG et les pictogrammes et documents graphiques). Les images fonctionnent même si `images/` n’a pas été transféré sur GitHub, à condition de charger `photo-cache.js` avec le nouvel `index.html` et `app.js`.

- 34 fiches pointent vers une image locale.
- 12 fiches utilisent une photographie Wikimedia Commons chargée depuis Internet : elles disposent désormais d’un fallback visuel local en cas d’échec, mais il reste préférable de télécharger ces photographies lorsque les licences le permettent.
- 4 fiches n’ont pas encore de photo identifiée (Carrefour Montbéliard, E.Leclerc Montbéliard, Info Jeunes, Marché du mardi) : elles utilisent un visuel de catégorie clair, et non une fausse photographie.

## Installer sur GitHub — méthode la plus sûre

1. Sauvegarde éventuellement ton dépôt actuel.
2. Décompresse **Guide_Ibis_Styles_Montbeliard_CORRECTIF_RAPIDE_PHOTOS_2026-10-26.zip**.
3. Dans ton dépôt GitHub, ouvre `Add file` puis `Upload files` à la RACINE de la branche `main`.
4. Dépose TOUS les fichiers du ZIP décompressé, et non le ZIP lui-même. Ils sont tous à la racine ; aucun dossier n’est nécessaire.
5. Clique `Commit changes`.
6. Vérifie que GitHub Actions a terminé le déploiement.
7. Ouvre `/photos-test.html` pour voir les images locales réellement publiées, puis `Ctrl + F5` sur la page du guide.

## IMPORTANT

L’archive COMPLETE inclut **en plus** le dossier `images/` (à conserver pour les modifications futures), mais pour une correction rapide de l’affichage le ZIP rapide suffit.

Photos transmises de sources tierces : autorisations de republication à confirmer avant diffusion publique, particulièrement les photos de presse et les images avec filigrane. Voir `PHOTOS-ET-DROITS.md` dans le ZIP complet.
