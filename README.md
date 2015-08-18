# DC Hack and Tell web site

This site should be serving at http://dchackandtell.github.io and http://dc.hackandtell.org


Check list of things DC Hack and Tell uses for organizing:

 * Meetup group
 * Github org
 * Gmail account
 * Google doc signup form
 * Hackpad for notes

## Editor's notes

To build the site:

    jekyll build --watch

To serve a local copy of the site, use the following command and then visit [http://127.0.0.1:4000/](http://127.0.0.1:4000/):

    jekyll serve

To add a new post, put it in the correct directory under `_posts/{year}`.

#### Ubuntu 14.04 installation pre-reqs

The apt-get version of jekyll is old and useless. Use this instead. However Ubuntu ruby2.0 defaults to ruby1.9 which makes gem not work correctly (and jekyll requires 2.0). 

    sudo apt-get install ruby2.0 ruby2.0-dev make gcc nodejs

    # Fix the ruby link problem
    sudo rm /usr/bin/ruby /usr/bin/gem /usr/bin/irb /usr/bin/rdoc /usr/bin/erb
    sudo ln -s /usr/bin/ruby2.0 /usr/bin/ruby
    sudo ln -s /usr/bin/gem2.0 /usr/bin/gem
    sudo ln -s /usr/bin/irb2.0 /usr/bin/irb
    sudo ln -s /usr/bin/rdoc2.0 /usr/bin/rdoc
    sudo ln -s /usr/bin/erb2.0 /usr/bin/erb
    sudo gem update --system
    sudo gem pristine --all

    sudo gem install jekyll --no-rdoc --no-ri
