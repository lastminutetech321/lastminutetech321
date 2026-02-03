# Application Layer

This directory contains application logic for the Nautical Compass system.

The Application Layer is responsible for execution **only**.
It operates strictly within constraints defined by governance and intake.

No authority originates here.

Governance precedes execution.

---

## Purpose

The application layer exists to:

- Execute approved system capabilities
- Implement workflows defined by higher layers
- Perform deterministic processing
- Produce outputs permitted by governance
- Serve interfaces (API, UI, integrations)

The application layer is procedural, not authoritative.

---

## Scope

This layer may:

- Execute business logic
- Process validated requests
- Call internal services
- Produce system outputs
- Interface with external systems (when authorized)

This layer does NOT:

- Define rules
- Interpret governance
- Override constraints
- Activate capabilities
- Make policy decisions

---

## Constraints

The Application Layer is constrained by:

1. Governance Layer (absolute authority)
2. Intake Layer (input validation and gating)
3. Analysis Layer (if enabled)

If a conflict exists, execution must halt.

The application layer may fail safely.
It may not self-authorize.

---

## Relationship to Other Layers

- Governance defines what is allowed
- Intake controls what enters
- Analysis informs (when enabled)
- Application executes
- Output emits results

Execution is downstream of authority.

---

## Change Policy

Application code may change frequently.

However:

- No change may bypass governance
- No feature may activate without approval
- No shortcut may weaken constraints

Velocity is permitted.
Autonomy is not.

---

## Status

Active.
Executable.
Subordinate.