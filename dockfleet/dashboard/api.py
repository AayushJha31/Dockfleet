from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
import time

app = FastAPI(
    title="DockFleet Dashboard API",
    version="0.1.0"
)

# Setup templates directory
templates = Jinja2Templates(directory="dockfleet/dashboard/templates")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/services")
def list_services():
    return [
        {"name": "api", "status": "running"},
        {"name": "worker", "status": "stopped"}
    ]

@app.get("/logs/{service}")
def stream_service_logs(service: str):
    def event_generator():
        counter = 1
        while True:
            log_line = f"[{service}] Log message {counter}"
            yield f"data: {log_line}\n\n"
            counter += 1
            time.sleep(2)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
    

@app.get("/", response_class=HTMLResponse)
def dashboard_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    