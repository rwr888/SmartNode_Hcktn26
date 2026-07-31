# SmartNode Platform

## Rules Engine Specification

**Version:** 0.1

---

# Purpose

The Rules Engine analyzes the operational condition of every machine using telemetry data received by the platform.

Its objective is not only to detect abnormal conditions, but also to provide an initial technical diagnosis and a maintenance recommendation.

The Rules Engine is independent from the data source.

Telemetry may come from:

* Industrial Simulator
* ESP32 IoT Node
* PLC
* External API
* Future hardware integrations

---

# Current Monitored Variables

| Variable    | Description                            |
| ----------- | -------------------------------------- |
| Status      | Current operating state of the machine |
| Temperature | Operating temperature (°C)             |
| Vibration   | Mechanical vibration level             |
| Current     | Electrical current consumption (A)     |

---

# Machine Health Levels

| Level     | Description                                     |
| --------- | ----------------------------------------------- |
| NORMAL    | Machine operating within expected conditions.   |
| ATTENTION | Slight deviation detected. Continue monitoring. |
| WARNING   | Maintenance inspection recommended.             |
| CRITICAL  | Immediate intervention required.                |

---

# Diagnostic Rules

| ID    | Status  | Temperature | Vibration | Current | Health    | Diagnostic                                                 | Recommendation                                                                           |
| ----- | ------- | ----------- | --------- | ------- | --------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| R-001 | Running | Normal      | Normal    | Normal  | NORMAL    | Normal operation                                           | Continue monitoring.                                                                     |
| R-002 | Running | High        | Normal    | High    | ATTENTION | Possible overload.                                         | Reduce load and monitor temperature.                                                     |
| R-003 | Running | High        | High      | Normal  | WARNING   | Possible bearing wear.                                     | Inspect bearings during the next maintenance window.                                     |
| R-004 | Running | High        | High      | High    | CRITICAL  | Possible mechanical failure.                               | Stop machine immediately and perform inspection.                                         |
| R-005 | Idle    | Normal      | Low       | Low     | NORMAL    | Machine stopped normally.                                  | No action required.                                                                      |
| R-006 | Idle    | High        | Low       | Low     | WARNING   | Machine heating while idle.                                | Inspect cooling system and verify shutdown sequence.                                     |
| R-007 | Running | Normal      | Normal    | High    | WARNING   | Electrical overload detected.                              | Inspect electrical system and load conditions.                                           |
| R-008 | Running | Normal      | High      | Normal  | WARNING   | Possible shaft misalignment.                               | Check coupling and shaft alignment.                                                      |
| R-009 | Running | Any         | Critical  | Any     | CRITICAL  | Excessive vibration detected.                              | Stop machine and inspect rotating components.                                            |
| R-010 | Fault   | Any         | Any       | Any     | CRITICAL  | Machine fault reported.                                    | Immediate inspection required.                                                           |
| R-011 | Idle    | Normal      | Low       | High    | WARNING   | Unexpected current draw.                                   | Inspect contactors, wiring and electrical system.                                        |
| R-012 | Running | Critical    | Any       | High    | CRITICAL  | Possible winding insulation failure or severe overheating. | Stop machine immediately. Perform insulation resistance test and inspect motor windings. |

---

# Rule Evaluation Priority

Rules are evaluated according to their severity.

1. CRITICAL
2. WARNING
3. ATTENTION
4. NORMAL

If multiple rules are satisfied simultaneously, the engine returns the highest priority condition.

---

# Future Variables

The Rules Engine has been designed to support additional telemetry without architectural changes.

Future variables may include:

* Voltage
* Humidity
* Pressure
* Flow rate
* RPM
* Power consumption
* Power factor
* Operating hours
* Lubrication level
* Ambient temperature

---

# Design Principles

* Independent from hardware.
* Independent from communication protocol.
* Independent from database implementation.
* Easy to extend with new variables.
* Easy to add new diagnostic rules.
* Focused on predictive maintenance.
* Designed for industrial scalability.

---

# Long-Term Vision

The current implementation evaluates simulated telemetry generated by the SmartNode Simulator.

In future versions, the simulator will be replaced by ESP32-based SmartNode devices without modifying the Rules Engine, allowing the same diagnostic logic to operate in real industrial and agricultural environments.
