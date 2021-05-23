### build docker image


run build

```docker build -t store-automation .```

or

```docker buildx build -t store-automation --platform=linux/amd64 .```

### run app

```docker run -p 8000:8000 store-automation```

