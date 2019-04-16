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
```