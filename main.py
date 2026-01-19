from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Literal
from datetime import datetime

app = FastAPI(title="LMT321", version="0.1.0")


# -----------------------------
# Health / status
# -----------------------------
from datetime import datetime

@app.get("/")
def root():
    return {"status": "LMT321 live"}

@app.get("/v1/health")
def v1_health():
    return {
        "status": "ok",
        "service": "LMT321",
        "version": "v1",
        "ts": datetime.utcnow().isoformat()
    }

# ----------------------------
# Versioned engine routes (protected)
# ----------------------------
@app.get("/v1/engine/ping")
def engine_ping():
    return {"engine": "ok"}


# -----------------------------
# Job Intake Models
# -----------------------------
Role = Literal[
    "A1", "A2", "V1", "V2", "LD", "L1", "L2",
    "Stagehand", "Rigger", "Audio Engineer", "Video Engineer", "Lighting Tech",
    "Camera Op", "Utility"
]

class JobRequest(BaseModel):
    client_name: str
    client_company: Optional[str] = None
    client_email: Optional[EmailStr] = None
    client_phone: Optional[str] = None

    event_name: Optional[str] = None
    venue_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    notes: Optional[str] = None

    start_time: Optional[str] = None  # keep as string for now (simple)
    end_time: Optional[str] = None
    roles_needed: List[Role] = []
    headcount: Optional[int] = None
    budget_notes: Optional[str] = None


class Availability(BaseModel):
    tech_name: str
    tech_email: Optional[EmailStr] = None
    tech_phone: Optional[str] = None
    roles: List[Role] = []
    date: str  # "YYYY-MM-DD"
    available: bool = True
    notes: Optional[str] = None


class ConfirmAssignment(BaseModel):
    request_id: str
    tech_name: str
    tech_email: Optional[EmailStr] = None
    confirmed: bool
    notes: Optional[str] = None


# -----------------------------
# Job Intake Endpoints (MVP)
# -----------------------------
@app.post("/request-tech")
def request_tech(payload: JobRequest):
    # Later: write to DB / send notifications / create ticket
    return {
        "received": True,
        "request_id": f"req_{int(datetime.utcnow().timestamp())}",
        "payload": payload.model_dump(),
    }

@app.post("/availability")
def availability(payload: Availability):
    # Later: store availability + matching logic
    return {"received": True, "payload": payload.model_dump()}

@app.post("/confirm")
def confirm(payload: ConfirmAssignment):
    # Later: lock assignment + notify client + update logs
    return {"received": True, "payload": payload.model_dump()}