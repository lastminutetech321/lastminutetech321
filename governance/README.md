# Governance Layer

This directory defines the constitutional, operational, and constraint framework
for the Nautical Compass system.

Governance precedes execution.
No application behavior may override governance rules.

---

## Purpose

The governance layer exists to:

- Define system authority and limits
- Establish non-negotiable constraints
- Control capability exposure
- Govern intake, analysis, and outputs
- Preserve long-term integrity and trust

Governance is declarative, not reactive.

---

## Scope

This layer may:

- Allow or deny access
- Create obligations
- Trigger enforcement
- Establish representation
- Define escalation thresholds

This layer does NOT:

- Execute business logic
- Process user requests
- Perform analysis

---

## Authority Model

Governance operates as the highest layer in the system hierarchy.

Order of precedence:

1. Governance
2. Intake
3. Analysis
4. Application logic
5. Output

If a lower layer conflicts with governance, governance prevails.

---

## Change Control

Governance rules are:

- Versioned
- Auditable
- Intentionally slow to change

No automated process may modify governance without explicit authorization.

---

## Relationship to Other Layers

- Intake is governed by this layer
- Analysis is constrained by this layer
- Application code must defer to this layer

Governance does not observe.
Governance decides.

---

## Status

Active.
Foundational.
Non-optional.