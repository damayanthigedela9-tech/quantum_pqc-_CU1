# Adaptive Quantum-Resilient Security System

## Qiskit Edition

A hackathon-ready proof-of-concept that combines:

- Quantum reservoir computing using Qiskit Aer
- Security telemetry risk scoring
- Sustained suspicious-activity detection
- Incident thresholding
- Session quarantine
- Security/integrity verification
- Approved post-quantum algorithm rotation
- Session re-establishment
- Audit logging

## Architecture

```text
Security Telemetry
       |
       v
Quantum Reservoir
       |
       v
Quantum Risk Score
       |
       v
Suspicious Activity?
    /          \
   No          Yes
   |            |
Normal      Incident Counter
Operation       |
                v
          Risk Verification
                |
                v
        Threshold Reached?
           /          \
          No           Yes
          |             |
      Monitor       Block Session
                        |
                        v
                   Quarantine
                        |
                        v
                Integrity Check
                   /        \
                 Fail       Pass
                  |           |
             Keep Quarantine  v
                         Rotate Approved
                           PQC Algorithm
                               |
                               v
                       Re-establish Session
                               |
                               v
                           Resume Secure
```

## Technology Stack

- Python
- Qiskit
- Qiskit Aer
- Quantum circuit simulation
- Post-quantum cryptography abstraction
- Rule-based adaptive security control

## Project Structure

```text
adaptive-quantum-resilient-security/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── quantum_reservoir.py
│   ├── security_policy.py
│   ├── incident_manager.py
│   └── pqc_wrapper.py
└── demo/
    └── sample_signals.json
```

## Installation

Recommended: Python 3.11–3.13 for a stable hackathon environment.

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run

From the project root:

```bash
python main.py
```

You should see:

```text
ADAPTIVE QUANTUM-RESILIENT SECURITY

NORMAL TEST
[QRC] Quantum reservoir output
Quantum risk score: ...

EVENT 1
SUSPICIOUS ACTIVITY DETECTED
THRESHOLD NOT REACHED

EVENT 2
SUSPICIOUS ACTIVITY DETECTED
THRESHOLD NOT REACHED

EVENT 3
THRESHOLD REACHED
BLOCK SUSPICIOUS SESSION
QUARANTINE
SECURITY VERIFICATION PASSED
CHANGING APPROVED PQC ALGORITHM
SECURITY RE-ESTABLISHED
SYSTEM_RESUMED
```

The exact quantum risk score can vary because the simulator uses finite measurement shots.

## Important Security Note

This repository is a proof-of-concept for a hackathon.

`PQCWrapper` intentionally provides an abstraction/demo interface. Its `encrypt()` and `decrypt()` methods are **not real ML-KEM cryptographic operations**.

The project demonstrates how an adaptive security controller could select between approved PQC algorithms. A production implementation must use a vetted, standards-compliant cryptographic library and perform proper key encapsulation, authentication, key lifecycle management, and secure session handling.

## Hackathon Value

### Problem

Conventional security systems may rely on static thresholds and fixed cryptographic configurations. They can struggle to adapt when suspicious behavior persists.

### Proposed Solution

This prototype introduces a feedback loop:

```text
Telemetry
   ↓
Quantum Risk Analysis
   ↓
Threat Detection
   ↓
Incident Accumulation
   ↓
Automatic Quarantine
   ↓
Security Verification
   ↓
PQC Algorithm Adaptation
   ↓
Secure Session Re-establishment
```

### Key Innovation

The system combines a small Qiskit quantum reservoir with an adaptive security controller. Quantum measurement probabilities are converted into a risk score, which drives the security response.

## Future Enhancements

- Real ML-KEM integration using a vetted cryptographic implementation
- ML-based anomaly detection
- Real-time network/security telemetry
- Dashboard visualization
- Persistent audit database
- Multi-session risk tracking
- Key rotation and lifecycle management
- Hardware quantum backend experiments
- SIEM/SOC integration
- Alert notification system

## License

For hackathon and educational demonstration use.
