This app - pre-employment test work.

### Docs

Postman collection

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/3dc235690e494fa57cc7)

or swagger docs

http://0.0.0.0:8000/docs

### build docker image

```docker build -t store-automation .```

### run app

```docker run --rm -p 8000:8000 -v var:/app/var store-automation```

### populate table with users and products

```docker run --rm -v var:/app/var store-automation /app/tools/db_filler.py```
