# Деус – веб-страница за кафуле (Деловна пракса 2025/2026)

Django проект. Јазик: македонски.

## Стартување

```bash
python -m venv venv
venv/Scripts/pip install -r requirements.txt
venv/Scripts/python manage.py migrate
venv/Scripts/python manage.py seed          # примерок содржина
venv/Scripts/python manage.py createsuperuser
venv/Scripts/python manage.py runserver
```

Страницата: http://localhost:8000/ — Администрација: http://localhost:8000/admin/

## За објавување (deploy)

```bash
venv/Scripts/python manage.py collectstatic --noinput
```

Статичките датотеки ги служи WhiteNoise. Пред објавување во `config/settings.py`
поставете `DEBUG = False`, нов `SECRET_KEY` и вистински `ALLOWED_HOSTS`.
