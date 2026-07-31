# SmartNode Platform

## Architecture Document

**Version:** 0.2

---

# 1. Purpose

SmartNode Platform is a modular IoT platform designed to monitor industrial and agricultural equipment by collecting, storing, and analyzing operational data.

The current version uses an industrial simulator that generates realistic machine states. The architecture is designed so the simulator can later be replaced by ESP32-based IoT nodes without requiring changes to the backend.

---

# 2. Problem Statement

Small and medium-sized companies often lack affordable predictive maintenance solutions due to:

* High implementation cost
* Proprietary hardware
* Complex infrastructure
* Limited scalability

---

# 3. Proposed Solution

Develop a modular backend where each component has a single responsibility.

The platform accepts information from either simulated devices or future ESP32 sensor nodes while keeping the same REST API and database structure.

---

# 4. Current Architecture

```text
Industrial Simulator
        │
        ▼
Machine Builder
        │
        ▼
FastAPI REST API
        │
        ├── Health Module
        ├── Sensors Module
        ├── Machines Module
        └── Database Module
                │
                ▼
             MongoDB
```

---

# 5. Future Architecture

```text
ESP32 Sensor Nodes
        │
        ▼
FastAPI REST API
        │
        ▼
MongoDB
        │
        ▼
Rules Engine
        │
        ▼
Dashboard
```

The simulator will eventually be replaced by physical IoT devices while preserving the backend architecture.

---

# 6. Project Modules

| Module       | Responsibility                             |
| ------------ | ------------------------------------------ |
| Health       | Service health check                       |
| Sensors      | Sensor endpoints                           |
| Machines     | Machine state generation and management    |
| Database     | MongoDB configuration and connection       |
| Simulator    | Future industrial simulator implementation |
| Dashboard    | Future visualization interface             |
| Firmware     | Future ESP32 firmware                      |
| Rules Engine | Future anomaly detection                   |

---

# 7. Technology Stack

* Python 3.13
* FastAPI
* MongoDB
* PyMongo
* Pydantic
* Git
* GitHub
* Visual Studio Code

---

# 8. Design Principles

* Modular architecture
* Separation of responsibilities
* Scalability
* Hardware-independent backend
* RESTful API design

---

# 9. Current Development Status

Implemented:

* FastAPI backend
* Health endpoint
* Sensors endpoint
* Machines endpoint
* Industrial machine simulation
* MongoDB integration
* Modular project structure

Planned:

* Rules Engine
* Alerts module
* Dashboard
* ESP32 integration
* Historical measurements
* Authentication
