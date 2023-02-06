Formation Git
=============
## Installation
#### sur OS X:
- si vous avez Xcode, git est déjà installé
- si vous avez Homebrew, `brew install git`
- sinon téléchargez Git ici : https://git-scm.com/download/mac

#### configurer Git
``` bash
git config --global user.email 
git config --global user.name
```
### Utilisation

### 1. Cloner le dépôt
``` bash
git clone XXX
Aller dans le dossier  formation_git
cd formation_git
```
### 2. Ajouter un fichier 
``` 
creéz un nouveau fichier 
echo "Hello, je suis en formation" >> formation.txt
# Un nouveau fichier a été créé
git status
# dire à Git  de suivre le nouveau fichier
git add formation.txt
le fichier a été ajouté à la staging et est prêt à être commité
```

### 3. commiter & pusher
```
un commit réprésente un état du reposity à un moment donné.
comment nommer son commit ?
- se limiter à un nombre de caractéres (par exemple 50 ou 80 caractères)
- Ne pas mettre de ponctuation
- Commencer par un verbe à l'impératif: un commit doit pouvoir compléter la phrase suivante: if applied, this commit will [commit name]
git commit -m 'Initial commit'
# pousser le nouveau commit
git push
```
### 4. Jongler avec les branches
```
On crée une nouvelle branche et on va dessus
stratégie de nommage des branches: 
- nom de la branche divisé en 3: <type>/<ticket>/<description>
<type> : peut être : fix, feat, optim, test, misc 
<description>: jusqu'à 4 mots
git checkout -b new-merge
# On crée un fichier
echo "ma-premiere-branche" > branche.txt
# On l'ajoute et on commit
git add branche.txt
git commit -m "Création de ma première branche"
# On la pousse sur le serveur 
git push --set-upstream origin new-merge
```
### 5. Gérer un conflit

```
on fusionne une branche dans le master
git merge new-merge
on fait une pause et on regarde ce qui vient de se passer
git status 
# on modifie le fichier puis on l'ajoute
git add merge.txt
# on finit la résolution de conflit en commitant
git commit
En cas de panique, on peut toujours annuler le merge en faisant `git merge --abort`
```
### 6 Revenir en arrière

```
cas 1 : les mises à jour on t été rejetées car la pointe de la branche courante est derrière
git fetch
git switch --detach origin/main
git branch -f main 
git switch main
git merge --no-ff new-merge

cas 2 :
git fetch
git lg --all
git checkout num-commit
git branch -f main
git checkout main
git merge --no-ff new-merge

```