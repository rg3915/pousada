## Como contribuir?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/denisfaria/pousada.git
cd pousada
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python create_data.py
python manage.py runserver
```

## Links

[gist rg3915 django-widget-tweaks](https://gist.github.com/rg3915/f0cb92e1ac8a707bba8e1a881fb4c09f)

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

[CCBV](http://ccbv.co.uk/)