#!/bin/bash


export PATH=${PATH}:/code
export PYTHONPATH=${PYTHONPATH}:/code

echo ${PYTHONPATH}

cd /code

# Apply database migrations
echo "Apply database migrations"
alembic upgrade head