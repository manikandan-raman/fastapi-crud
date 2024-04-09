# FastAPI - CRUD

## Database

We've used Postgres as our database.

### Database Migrations

It's very important to be able to manage database tables migrations and schema updates as our service grows or tables schema changes over time.
We use SQLAlchemy `alembic` to manage database migrations. To read more https://alembic.sqlalchemy.org/.

Follow the below steps to enable `alembic` migration for your service.
There are different ways to use `alembic` library in your service. I've described two different methods.

1. Go into a directory and create a python virtual environment, and activate it.

```bash
cd /path/to/a/dir
python3 -m venv venv
source venv/bin/activate
```

2. Add `alembic` to `requirements.txt` file and install packages:

```bash
pip install -r requirements.txt
```

_Please make sure that your database is up and accessible from localhost_.

You need to run the above command every time your tables schema changes.

Apply the changes:

```bash
alembic upgrade head
```

This command will reflect the new changes into database table.
You need to run this command every time you have new revision files.

#### To run the app

Make sure docker is installed in your system

```bash
docker compose up
```
