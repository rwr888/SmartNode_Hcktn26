
---

# docs/alerts.md

Versión 0.1

```markdown
# SmartNode Platform
## Alerts Module
**Version:** 0.1

---

# Purpose

The Alerts Module is responsible for generating notifications after the Rules Engine evaluates machine operating conditions.

Alerts represent actionable events that may require operator attention.

---

# Alert Flow
Simulator / ESP32

↓

Machine Service

↓

Rules Engine

↓

Alert Service

↓

MongoDB


---

# Alert Structure

Each alert contains:

| Field | Description |
|---------|-------------|
| machine_id | Machine identifier |
| health | Machine health level |
| diagnostic | Engineering diagnosis |
| recommendation | Suggested action |
| acknowledged | Operator acknowledgment |
| timestamp | Creation time |

---

# Health Levels

| Level | Meaning |
|--------|---------|
| NORMAL | Machine operating normally |
| ATTENTION | Early abnormal condition |
| WARNING | Maintenance should be scheduled |
| CRITICAL | Immediate intervention required |

---

# Current Behavior

The module currently:

- Generates alerts automatically.
- Stores alerts in MongoDB.
- Prevents duplicate active alerts.
- Leaves alerts unacknowledged until future operator interaction.

---

# Future Features

- GET /alerts
- Alert acknowledgment
- Alert history
- Email notifications
- Telegram notifications
- WhatsApp notifications
- Dashboard notifications
- Alert priority filtering