https://fastapi-users.github.io/fastapi-users/configuration/full-example/

alembic init -t async alembic

change alembic.ini sqlalchemy.url and alembic/env.py target=Base.metadata

alembic revision --autogenerate -m "init"

alembic upgrade head
