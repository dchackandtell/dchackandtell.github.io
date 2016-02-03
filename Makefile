# Editors: I made a quick Makefile to help me edit, deploy and test
.PHONY: build serve view edit

current_post = _posts/2015/2015-12-08-round-27.md

all:
	echo "Make commands: edit, build, serve"

build:
	jekyll build --watch

serve:
	jekyll serve

view:
	xdg-open http://127.0.0.1:4000/

edit:
	emacs $(current_post) &
