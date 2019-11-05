# Editors: I made a quick Makefile to help me edit, deploy and test
.PHONY: build serve view edit

current_post = _posts/2019/2019-10-00-round-71.md

all:
	echo "Make commands: edit, build, serve"

build:
	jekyll build --watch

serve:
	jekyll serve

view:
	xdg-open http://127.0.0.1:4000/

fix_links:
	python markdownify.py $(current_post)

edit:
	emacs $(current_post) &
