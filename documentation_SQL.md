# Documentation SQL

## 1) Qu'est-ce qu'une base de données ?
Une base de données est un espace structuré pour stocker, organiser et interroger des données.

- **Database** : contient les tables.
- **Table** : contient les données sous forme de lignes et colonnes.
- **Row / Record** : une ligne de données.
- **Column / Field** : un attribut de la table.
- **DBMS** : le logiciel qui gère la base (SQLite, PostgreSQL, MySQL...).
- **SQL** : le langage utilisé pour parler au DBMS.

---

## 2) Types de données de base
Les types varient un peu selon le DBMS, mais les plus courants sont :

- `INTEGER` : entier
- `REAL` : nombre décimal
- `TEXT` : texte
- `BLOB` : données binaires
- `NULL` : absence de valeur

Exemple :

```sql
CREATE TABLE books (
    id INTEGER,
    title TEXT,
    year INTEGER
);
```

---

## 3) CREATE TABLE
Créer une table :

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    age INTEGER
);
```

### Points importants
- `PRIMARY KEY` identifie chaque ligne de façon unique.
- `UNIQUE` empêche la duplication des valeurs.
- `NOT NULL` empêche une valeur vide.

---

## 4) PRIMARY KEY
La clé primaire :

- est unique
- ne peut pas être `NULL`
- sert à identifier un enregistrement
- est généralement un `id`

Exemple :

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER
);
```

### Règle pratique
- `id` = identité technique du record
- `username`, `email` = souvent `UNIQUE`, pas forcément `PRIMARY KEY`

---

## 5) INSERT
Ajouter des données :

```sql
INSERT INTO books (title, author, year)
VALUES ('Clean Code', 'Robert Martin', 2008);
```

### Bon réflexe
Toujours préciser les colonnes.

```sql
INSERT INTO books (title, author, year)
VALUES ('Atomic Habits', 'James Clear', 2018);
```

---

## 6) SELECT
Lire les données :

```sql
SELECT * FROM books;
```

### Sélectionner quelques colonnes

```sql
SELECT title, author
FROM books;
```

### Filtrer

```sql
SELECT *
FROM books
WHERE year = 2018;
```

---

## 7) WHERE
Le filtre principal.

### Comparateurs

- `=` égal
- `!=` différent
- `<>` différent (standard SQL)
- `>` supérieur
- `<` inférieur
- `>=` supérieur ou égal
- `<=` inférieur ou égal

Exemple :

```sql
SELECT title, author
FROM books
WHERE year >= 2018;
```

---

## 8) AND / OR / NOT

### AND
Les deux conditions doivent être vraies.

```sql
SELECT *
FROM books
WHERE year >= 2018
  AND author <> 'James Clear';
```

### OR
Au moins une condition doit être vraie.

```sql
SELECT *
FROM books
WHERE year >= 2018
   OR author = 'James Clear';
```

### NOT
Inverse une condition.

```sql
SELECT *
FROM books
WHERE NOT year = 2018;
```

---

## 9) BETWEEN
Intervalle inclusif.

```sql
SELECT title, author
FROM books
WHERE year BETWEEN 2018 AND 2022;
```

Équivalent à :

```sql
WHERE year >= 2018 AND year <= 2022
```

---

## 10) IN
Tester l’appartenance à une liste.

```sql
SELECT *
FROM books
WHERE year IN (2018, 2019, 2020);
```

---

## 11) LIKE
Recherche par motif dans du texte.

- `%` = n’importe quelle suite de caractères
- `_` = un seul caractère

Exemples :

```sql
SELECT *
FROM books
WHERE author LIKE '%lahrour%';
```

Cela match si `lahrour` apparaît n’importe où dans `author`.

Autres exemples :

```sql
WHERE title LIKE 'Python%'
WHERE title LIKE '%Code'
WHERE title LIKE '_ava'
```

---

## 12) IS NULL / IS NOT NULL
Tester l’absence de valeur.

```sql
SELECT *
FROM books
WHERE author IS NULL;
```

```sql
SELECT *
FROM books
WHERE author IS NOT NULL;
```

> Ne pas utiliser `= NULL`.

---

## 13) UPDATE
Modifier des données.

```sql
UPDATE books
SET year = 2020
WHERE id = 3;
```

### Attention
Sans `WHERE`, toutes les lignes sont modifiées.

```sql
UPDATE books
SET year = 2026;
```

---

## 14) DELETE
Supprimer des données.

```sql
DELETE FROM books
WHERE id = 2;
```

### Attention
Sans `WHERE`, toutes les lignes sont supprimées.

```sql
DELETE FROM books;
```

Le tableau reste, mais les lignes disparaissent.

---

## 15) ORDER BY
Trier les résultats.

```sql
SELECT *
FROM books
ORDER BY year ASC;
```

- `ASC` : croissant
- `DESC` : décroissant

Exemple :

```sql
SELECT title, year
FROM books
ORDER BY year DESC;
```

---

## 16) LIMIT
Limiter le nombre de lignes retournées.

```sql
SELECT *
FROM books
LIMIT 5;
```

Exemple avec tri :

```sql
SELECT *
FROM books
ORDER BY year DESC
LIMIT 3;
```

---

## 17) Fonctions d’agrégation
Les plus utilisées :

- `COUNT()` : compter
- `SUM()` : somme
- `AVG()` : moyenne
- `MIN()` : minimum
- `MAX()` : maximum

Exemples :

```sql
SELECT COUNT(*) FROM books;
SELECT AVG(year) FROM books;
SELECT MAX(year) FROM books;
```

---

## 18) GROUP BY
Grouper les lignes par valeur commune.

```sql
SELECT author, COUNT(*)
FROM books
GROUP BY author;
```

---

## 19) HAVING
Filtrer après le `GROUP BY`.

```sql
SELECT author, COUNT(*)
FROM books
GROUP BY author
HAVING COUNT(*) >= 2;
```

---

## 20) Relations entre tables
Les relations permettent de structurer les données proprement.

### One-to-One
Un enregistrement correspond à un seul autre.

### One-to-Many
Un utilisateur peut avoir plusieurs posts.

### Many-to-Many
Un étudiant peut suivre plusieurs cours, et un cours peut avoir plusieurs étudiants.

Exemple simple :

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## 21) FOREIGN KEY
La clé étrangère relie une table à une autre.

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
```

Cela veut dire :
- `posts.user_id` doit pointer vers un `users.id` existant.

---

## 22) JOIN
Combiner des tables.

### INNER JOIN
Retourne seulement les correspondances.

```sql
SELECT posts.title, users.username
FROM posts
INNER JOIN users ON posts.user_id = users.id;
```

### LEFT JOIN
Retourne toutes les lignes de gauche + correspondances de droite.

```sql
SELECT users.username, posts.title
FROM users
LEFT JOIN posts ON posts.user_id = users.id;
```

---

## 23) Transactions
Une transaction regroupe plusieurs opérations en une seule unité.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

En cas de problème :

```sql
ROLLBACK;
```

---

## 24) Indexes
Un index accélère certaines recherches.

```sql
CREATE INDEX idx_books_year ON books(year);
```

### Utilité
- accélérer les `WHERE`
- accélérer certains `JOIN`

### Coût
- prend de l’espace
- ralentit un peu `INSERT`, `UPDATE`, `DELETE`

---

## 25) Bonnes pratiques
- Utiliser `id` comme `PRIMARY KEY`.
- Mettre `UNIQUE` sur les champs vraiment uniques.
- Toujours écrire `WHERE` avec `UPDATE` et `DELETE`.
- Éviter les espaces inutiles dans les données.
- Utiliser des noms clairs : `published_at`, `likes_count`, `author`.
- Préférer `<>` si tu veux rester proche du standard SQL.

---

## 26) CRUD
Les 4 opérations de base :

- **Create** → `INSERT`
- **Read** → `SELECT`
- **Update** → `UPDATE`
- **Delete** → `DELETE`

---

## 27) Mini cheat sheet

```sql
CREATE TABLE ...
INSERT INTO ... VALUES (...)
SELECT ... FROM ... WHERE ...
UPDATE ... SET ... WHERE ...
DELETE FROM ... WHERE ...
ORDER BY ... ASC|DESC
LIMIT n
GROUP BY ...
HAVING ...
```

---

## 28) Exercices rapides

### Exercice 1
Créer une table `students` avec :
- `id`
- `name`
- `age`
- `email`

### Exercice 2
Ajouter 3 étudiants.

### Exercice 3
Afficher seulement les noms.

### Exercice 4
Afficher les étudiants âgés de 18 ans ou plus.

### Exercice 5
Mettre à jour l’email d’un étudiant.

### Exercice 6
Supprimer un étudiant via son `id`.

---

## 29) Pièges fréquents
- Oublier `WHERE` dans `UPDATE` / `DELETE`
- Confondre `AND` et `OR`
- Utiliser `= NULL` au lieu de `IS NULL`
- Mettre des espaces inutiles dans les chaînes
- Choisir une mauvaise clé primaire
- Ne pas indexer les colonnes souvent filtrées

---

## 30) Résumé mental
Pense SQL comme un moteur de sélection et de transformation :

- `SELECT` = lire
- `WHERE` = filtrer
- `ORDER BY` = trier
- `LIMIT` = restreindre
- `GROUP BY` = agréger
- `JOIN` = relier
- `INSERT/UPDATE/DELETE` = modifier l’état

