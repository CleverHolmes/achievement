git config --local user.name CleverHolmes
git config --local user.email hugo.rogers.16@gmail.com

git checkout -B branch
git add .
git commit --allow-empty -m "empty"
git push -u origin branch
git checkout master

echo asdf

gh pr create -f
gh pr merge --merge --delete-branch
sleep 40
