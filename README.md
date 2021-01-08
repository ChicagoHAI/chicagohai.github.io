# chicagohai.github.io

Clone:  
`git clone --recurse-submodules https://github.com/ChicagoHAI/chicagohai.github.io`

# Edit content and publish

## How to edit contents
For homepage, edit `content/_index.md`.

For publication, edit `content/publication.md` and `data/papers.yml`. Here, I use a template to enumerate publications in `data/papers.yml` file. You can modify the representation in `layouts/shortcodes/listPapers.html`.

## Locally run server
run `hugo server` in base directory.

## How to publish website
After finishing editing the content, we can update static files in `docs/` by
```
# at base dir
hugo
```
To see site settings, go to `GitHub Pages` in `Settings` on github repo page. Remember to change source from `root/` to `docs/`.

# Environments
## Install Go
See details here. https://golang.org/doc/install .
```
# Linux
weget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz
# add this into your bashrc/zshrc
export PATH=$PATH:/usr/local/go/bin
```

## Install Hugo
```
mkdir $HOME/src
cd $HOME/src
git clone https://github.com/gohugoio/hugo.git
cd hugo
go install --tags extended
# check where is you $GO_PATH and add it into your $PATH
```
If you encounter any problems, please refer to [trouble shooting](#Trouble-Shooting).

## Trouble Shooting
### 
`# github.com/bep/golibsass/internal/libsass
exec: "gcc": executable file not found in $PATH`

see https://linuxize.com/post/how-to-install-gcc-compiler-on-ubuntu-18-04/ .