## Initial Setup: Create Virtual Env and Install required packages
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Database creation
```
flask db init
flask db migrate
flask db upgrade
```

## Running the app
```
export FLASK_APP=main.py
flask run
```


