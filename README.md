# Boon URL Shortener App ![Boon URL Shortener App](/router/static/images/boon2.png)

A Django URL Shortener App created with Django 3.0 and Python 3.8 to shorten any URL given. This project is an ALX project.

**Live Site**: https://sbxboon.niiodoi.tech/

**Project Site**: https://sbxboon.niiodoi.tech/landing

## Installation (How to Setup in Localhost)

1. Clone this repository.
2. Open the cloned repository.
3. Install dependencies using ``pip install -r requirements.txt``
**OR**
Install ``pipenv`` using ``pip install pipenv`` and initialise a Virtual Machine using ``pipenv install`` in the directory.
4. Set environment variables like `SECRET_KEY`, `DEBUG_VALUE`.
5. Run the Django Server using ``python manage.py runserver`` and then goto ``localhost:8000`` or ``127.0.0.1:8000`` and see the server running.

### Usage (Environment Variables):

`SECRET_KEY`: Django secret key which can be any long hexadecimal value. Django recommends *atleast* **50 characters** to make it secure.
`DEBUG_VALUE`: Set it as **"True"** for Debug environment and **"False"** for Production.


## Features

- Can shorten any url.
- Can see all the shortened urls created with it.
- Can choose any custom value to shorten the url.

### Features to add

- Improve the CSS of the site.
- Add a User Authentication system.
- Add a process to delete any redirects not used within 7 days.

*More features can be suggested in Issues.*

#### Known Issues:

No issues detected till now.

*Please make a GitHub issue if any other bugs are found.*

## Notes

This project was created on **Ubuntu-20.04 LTS** and tested under **Windows 10** and **Ubuntu**, and is expected to work fully in other systems too.

This project is still under development. Parts of the source codes may not be well documented. Also suitable prompts may not be available for the user at the moment.

More features and fixes are yet to come. Meanwhile suggestions, ideas, bug reports are welcomed.

## Related Projects
* [Bitly](https://bitly.com/)
* [TinyURL](https://tinyurl.com/app)

## License

[Project Licensing](https://github.com/Nii-Odoi1/Boon/blob/master/LICENSE)

## Author

[Nii Tetteh Odoi](https://www.linkedin.com/in/nii-odoi/)
