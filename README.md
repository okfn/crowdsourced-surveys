## Overview

This project is a prototype built to assist crowdsourcing of data about schools
in Tanzania. It is built oin top of Ushahidi, a crowdsourcing platform, and has 
some extra glue / management code to hold it all together and automate things as 
much as possible.

Here are some relevant links for the Tanzania schools crowdsourcing project:

* [The Ushahidi API](https://crowdsurvey-api.herokuapp.com) instance we used
* [The Ushahidi web client](https://crowdsurvey.herokuapp.com)
* [An embedded form](https://tz-schools.oklabs.org/) created to simplify crowd's 
interaction with us (hosted on GitHub Pages, code is in 
[the `gh-pages` branch](https://github.com/okfn/crowdsourced-surveys/tree/gh-pages)
* [This GitHub repository](https://github.com/okfn/crowdsourced-surveys/)


## CLI tool

The code in this repository deals with the Ushahidi API, mostly to "seed" the 
database with forms and answers.

### Installation

* With `pipenv`
  * `$ pipenv install` to install dependencies
  * `$ pipenv shell` to activate the environment
* With pip/virtualenv: use the provided requirements.txt file

### Usage

```
$ python cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Commands:
  delete_form
  fake_answer
  heroku_adjust_upload
  send_answer
  send_form
  test
```

For individual commands syntax and description, call any of them with the `--help` flag, like this:
```
$ python cli.py test --help
Usage: cli.py test [OPTIONS]

Options:
  -a, --auth  Test authentication
  -p, --ping  Ping test
  -t, --time  Time to API and back
  -e, --env   Print env vars (paged)
  --help      Show this message and exit.

```

## License

MIT License

Copyright (c) 2018 Open Knowledge International
