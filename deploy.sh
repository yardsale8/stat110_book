git checkout master
git subtree split --prefix build/stat110 -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages
