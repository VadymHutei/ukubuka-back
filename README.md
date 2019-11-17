# Ukubuka Back

## running

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

## venv

```bash
apt install python3.7-venv
python3 -m venv ./
source ./bin/activate
deactivate
```

## pip

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip freeze > requirements.txt
```
