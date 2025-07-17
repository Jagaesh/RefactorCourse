# HOKLA CODE QUALITY TEST

## Instructions

Ce test est une mise en situation, tu arrives sur un nouveau projet avec un code de mauvaise qualité et ton client te demande de rajouter une fonctionnalité pour demain. Tu es conscient que tu ne seras plus sur ce projet après-demain, tu dois donc aussi faire en sorte que le prochain développeur puisse reprendre la main sur ce projet très facilement. A toi de jouer pour ajouter la fonctionnalité et rendre le code plus compréhensible.

Tu es totalement libre sur la manière de faire, tu devras justifier tes choix lors du débrief.

Note: Attention ce code est actuellement en production et fonctionne correctement selon les attentes actuelles du client.

Bon courage!

---

## Enoncé

Bonjour et bienvenue dans l'équipe de l'AP-HP, l'assistance publique des Hoklaniens practiciens.

A l'AP-HP, nous tentons chaque jour de soigner nos patients avec les meilleurs médicaments afin de favoriser leur guérison rapide. C'est pour cela que nous ne délivrons que des médicaments que nous avons nous mêmes validés.

Malheureusement, l'efficacité des médicaments de base se dégrade à l'approche de leur date de péremption. Tous? non, car nous avons déniché quelques médicaments dont nous sommes très fiers.

Notre équipe informatique dont vous faites partie a mis en place un système pour suivre notre inventaire. Il a été développé par Bernardos, une personne pleine de bon sens qui est partie pour de nouvelles aventures.

Votre objectif est d'ajouter un nouveau médicament que nous venons d'acquérir pour que nous puissions soigner rapidement une nouvelle épidémie qui se développe vite en France.

Mais d'abord, laissez-moi vous présenter notre système:

- Tous les médicaments ont une valeur `use_before` qui désigne le nombre de jours restants avant leurs dates de péremption.
- Tous les médicaments ont une `efficiency` en pourcentage qui dénote combien le médicament est efficace.
- A la fin de chaque journée, notre système diminue ces deux valeurs pour chaque médicament (de 1 jour et 1%)

Plutôt simple, non ?

Attendez, ça devient intéressant:

- Une fois que la date de péremption est passée, l'efficacité se dégrade deux fois plus rapidement.
- Les "fioles d'insuline", diminuent aussi de 1 en efficacité au cours du temps. Néanmoins, l'efficacité diminue de 2 quand il reste 30 jours ou moins, puis de 3 quand il reste 7 jours ou moins. Enfin, l'efficacité tombe à 0 après la date de péremption car ces fioles deviennent toxiques pour l'organisme.
- Nos "Recettes de grand-mère", perdurent à travers le temps, donc n'ont pas de date de péremption et ne perdent jamais en efficacité (on nous dit même que certains recettes seraient d'une efficacité hors-norme).
- Enfin, certains de nos pharmaciens privilégient la médécine de campagne. Leur "bouteille de vin" augmente son efficacité plus le temps passe et est très appréciée des patients.

Comme dit en préambule de notre présentation, pour contrer les diverses pandémies, Nous avons récemment signé un partenariat avec un fournisseur de vaccins à ARN messager. Cela nécessite une mise à jour de notre système:

- Les "Vaccin ARN" voient leur efficacité se dégrader de deux fois plus vite que les médicaments normaux, ce qui est normal car ils n'ont pas le même historique que nos autres médicaments. En temps normal, nous ne le délivrerions pas, mais l'urgence nous impose de le faire.

## Informations pratiques

Pour installer le projet, dans un nouveau terminal, lancez la commande

```bash
poetry install
```

Si `poetry` n'est pas déjà installé, vous pouvez l'installer avec la commande

```bash
pip install poetry
```

Pour exécuter le fichier de test, lancez la commande

```bash
python main.py
```
