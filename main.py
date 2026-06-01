import os
from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Hello San Ramon")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    now = datetime.now()
    today = now.strftime("%A, %B %d, %Y")
    current_time = now.strftime("%I:%M:%S %p")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello San Ramon</title>
    <style>
        body {{
            margin: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #fff;
            text-align: center;
        }}
        h1 {{ font-size: 3rem; margin: 0 0 0.5rem; }}
        p  {{ font-size: 1.5rem; opacity: 0.9; margin: 0; }}
    </style>
</head>
<body>
    <h1>Hello San Ramon</h1>
    <p>Today is {today}</p>
    <p>The time is {current_time}</p>
</body>
</html>"""


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
