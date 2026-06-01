# Hello San Ramon

A tiny single-page FastAPI app that greets San Ramon and shows the current server date and time.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```

Then open http://127.0.0.1:8080

## Docker

```bash
docker build -t hello-san-ramon .
docker run -p 8080:8080 hello-san-ramon
```
