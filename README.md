# Django Quickstart

(Original script https://github.com/henriquebastos/django-quickstart )

Adjusted to better fit my initial setup

This template includes:

- .env setup with <a href="https://github.com/henriquebastos/python-decouple">Decouple</a>
- Pytest and pytest-django
- Static assets serving with dj-static (WSGI server)
- <a href="https://django-jazzmin.readthedocs.io/">Jazzmin</a> for django admin template
- <a href="https://django-extensions.readthedocs.io/en/latest/">Django extensions</a> for the cool `python manage.py shell_plus` environment

## One liner:

1. Copy and paste the code below in your terminal
2. Hit 'Enter'
3. Type in your project's name (no spaces or funny chars)
4. Hit 'Enter'


```
read PROJECT_NAME && \
mkdir $PROJECT_NAME && \
cd $PROJECT_NAME && \
python3 -m venv .venv && \
source .venv/bin/activate && \
python3 -m pip install --upgrade pip && \
python3 -m pip install django && \
django-admin startproject --template https://github.com/GuiFV/django-quickstart/archive/master.zip --name=.env,pytest.ini $PROJECT_NAME . && \
pip3 install --prefer-binary -r requirements-dev.txt && \
git init && \
git add . && \
git commit -m 'Initial import'
```
## Afterwards:

5. Change SECRET_KEY in .env (you can use https://djecrety.ir/)
6. Create a repo
7. Set it up locally using `git remote add origin https://github.com/YOURNAME/REPO_CREATED/`
8. git push to your new repo
9. Happy coding :)


