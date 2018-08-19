# DC Hack && Tell website

This site should be serving at https://dchackandtell.github.io and https://dc.hackandtell.org


Check list of things DC Hack and Tell uses for organizing:

 * [Meetup group](https://www.meetup.com/DC-Hack-and-Tell/)
 * [Github org](https://github.com/dchackandtell)
 * [Google doc signup form](https://docs.google.com/forms/d/15F33kAQFgI825JECUI7uAqXrdgbr1dkjO0DRK4MOKq4/viewform)
 * [Google doc for notes](https://docs.google.com/document/d/1DM_qVHEGPNP-UzSGKNlee8lmroNqap4Fg4RgERxxTiY/edit)
 * [Twitter account](https://twitter.com/dchackandtell)
 * Gmail account

## Editor's notes

To build and serve the site locally:

    jekyll serve

then visit [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

To add a new post, put it in the correct directory under `_posts/{year}`.
To draft a post (but not create the link), set the status to `notext`.

#### Ubuntu 16.04 installation pre-reqs

This should be enough to build the site:

    sudo apt-get install jekyll
