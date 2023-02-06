# formation_git


poetry run pre-commit install
export PATH="$HOME/.poetry/bin:$PATH"

git st
git commit --amend
git push -f


# revenir sur la version d'avant 
> git lg --all
>
reflog visualiser l'historique local
> git reflog
> 
> git checkout num_commit
> 
> git branch -f "name_branch"
> 
> git checkout "name_branch"
> 
si vous voulez créer une nouvelle branche pour conserver les commits que vous créez, il suffit d'utiliser l'option -c de la commande switch comme ceci :
> 
> git switch -c <nom-de-la-nouvelle-branche
 
> git reset soft num_commit
> 
> git status
> 
> git diff --cached
> 
> git commit -m ""
> 
> git push -f 
# rebase interactif
> git rebase origin/master
> 
>  git push -f origin "name_branch"
 # faire un merge entre deux branches
> la commande git merge permet de ramener les modifications d'une branche qui à bifurqué de la branche  courante
> pour réaliser un merge, il faut
> 1 se placer sur la branche de destination. C'est à dire, la branche qui va recevoir les modification d'autre branche
> git checkout <nom_branche>
> puis utiliser la commande git merge [branche_a_merge]
> git checkout <destination_branche>
> git merge <branche_a_merge>
> un commit de merge est crée pour permettre d'avoir 
> 
> 
# squasher 
pour ne pas retrouver des commits de travail dans votre branche de production, il est essentiel de squasher ces commits avant de fusionner la branche
squasher des commits signifie regrouper plusieurs commits en un seul. si vous avez 3 commits A-B-c et que vous les regroupez B et C dans le commit A, vous avez "squashé vos commits"
on va regrouper 4 commits  qu'on a généré dans un seul commit
pour cela, on va faire un rebase interactif à partir du commit qui précède le commit qu'on veut garder.
git rebase -i XXXX
un éditeur s'ouvre 
le commit que je veux garder je laisse pick
je ne veux pas garder les autres, je veux qu'ils soient fusionnés dans le commit que je veux garder. je vais donc remplacer "pick" par "squash"
il faut ensuite faire un push -f car on souhaite réécrire l'historique de la branche distante