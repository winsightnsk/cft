FROM python

WORKDIR /tests_project/

COPY src/requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt  --no-cache-dir

COPY entrypoint.sh .

COPY src/tests tests/