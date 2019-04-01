## Setup
1. Install requirements.txt by running `pip3 install -r requirements.txt` in the root directory. (Optionally, set up a virtual environment beforehand)

2. Set up MySQL database locally (either using the `mysql_import.py` file in judge scraper repo, or import via the file `assets/court_data.sql`.

3. Add a `.env` file with the following environment variables:

```
MYSQL_DATABASE_USER=username
MYSQL_DATABASE_PASSWORD=password
MYSQL_DATABASE_DB=db_name
MYSQL_DATABASE_HOST=localhost
```

4. Run `python3 app.py` to start the application.
