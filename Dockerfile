FROM python:3.8

# Configure Poetry
ENV POETRY_VERSION=1.2.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-ansi

# Run your app
COPY . /app
EXPOSE 5000:5000
CMD [ "poetry", "run", "python3", "views.py" ]



# sudo docker run -d -p 5000:5000 --name 4isto --network My_Net --user matvey@Inspiron-5565