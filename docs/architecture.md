# SmartNode Platform
## Architecture Document
**Version:** 0.1

---

# 1. Purpose

SmartNode Platform is a modular IoT platform designed to monitor industrial and agricultural equipment by collecting, storing, and analyzing sensor data.

The initial version will use simulated sensor data, allowing the software platform to be fully developed before integrating physical hardware.

---

# 2. Problem Statement

Small and medium-sized companies often lack affordable predictive maintenance solutions due to:

- High implementation cost.
- Proprietary hardware.
- Complex infrastructure.

---

# 3. Proposed Solution

Develop a modular platform composed of independent components.

Any data source (simulator or ESP32) can send measurements to the same API.

---

# 4. System Architecture

Simulator / ESP32
        │
        ▼
     FastAPI
        │
        ▼
     MongoDB
        │
        ▼
 Rules Engine
        │
        ▼
 Dashboard

---

# 5. Modules

| Module | Responsibility |
|---------|----------------|
| Simulator | Generate sensor data |
| API | Receive and validate data |
| Database | Store measurements |
| Rules Engine | Detect anomalies |
| Dashboard | Display system status |

---

# 6. Technology Stack

- Python
- FastAPI
- MongoDB
- Git
- GitHub
- Visual Studio Code

---

# 7. Future Expansion

Future versions will replace the simulator with an ESP32 without modifying the backend architecture.  