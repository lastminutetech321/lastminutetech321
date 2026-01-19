from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Literal
from datetime import datetime
from uuid import uuid4
app = FastAPI(title="LMT321", version="0.1.0")
# ----------------------------
# In-memory store (Phase A)
# NOTE: This resets on redeploy. Database comes later.
# ----------------------------
JOBS: Dict[str, dict] = {}

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
# Jobs (Phase A: intake + read)
# ----------------------------

@app.post("/v1/jobs/intake", response_model=JobResponse)
def job_intake(payload: JobRequest):
    job_id = str(uuid4())
    received_at = datetime.utcnow().isoformat()

    JOBS[job_id] = {
        "job_id": job_id,
        "received_at": received_at,
        "data": payload.model_dump(),
    }

    return JobResponse(
        job_id=job_id,
        received_at=received_at,
        data=payload
    )


@app.get("/v1/jobs/{job_id}")
def job_get(job_id: str):
    job = JOBS.get(job_id)
    if not job:
        return {"ok": False, "error": "job_not_found", "job_id": job_id}
    return {"ok": True, **job}


@app.get("/v1/jobs")
def job_list():
    # lightweight list view
    return {
        "ok": True,
        "count": len(JOBS),
        "jobs": [
            {"job_id": j["job_id"], "received_at": j["received_at"]}
            for j in JOBS.values()
        ],
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

from pydantic import field_validator

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

    start_time: Optional[str] = None
    end_time: Optional[str] = None
    roles_needed: List[Role] = []
    headcount: Optional[int] = None
    budget_notes: Optional[str] = None

    @field_validator("client_name")
    @classmethod
    def client_name_not_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("client_name is required")
        return v

    @field_validator("headcount")
    @classmethod
    def headcount_positive(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        if v <= 0:
            raise ValueError("headcount must be > 0")
        return v
class JobResponse(BaseModel):
    job_id: str
    received_at: str
    data: JobRequest

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