# formation_git


git add test.py

git commit -m ""

git push


git rebase origin/master
 resolve all conflicts manually, mark them as resolved with 
git add then run 
git rebase --continue
to abort and get back to the state before "git rebase", run " git rebase --abort"


git lg --all 
git fetch
git status
git rebase origin/master
git add 
git add 
git status

réglez les conflits puis lancez "git rebase --continue"
utilisez "git rebase -- abort" pour extraire la branche d'origine


si vous voulez créer une nouvelle branche pour conserver les commits que vous créez,
il vous suffit d'utliser l'option -c de la commande comme ceci :
git switch -c <nom-de-la-nouvelle-branche>
ou annuler cette opération 
git switch -



git branch -f feat/hcpi-14
git lg --all
git status
git add .
git lg --all
poetry run pre-commit install
export PATH="$HOME/.poetry/bin:$PATH"

git st
git commit --amend
git push -f