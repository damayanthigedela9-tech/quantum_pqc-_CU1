"""
Adaptive Quantum-Resilient Security System — Qiskit Edition

Run:
    pip install -r requirements.txt
    python main.py

NOTE:
The PQCWrapper is a demonstration abstraction. It does NOT perform
real ML-KEM encryption/decryption.
"""

from time import time

from src.quantum_reservoir import QuantumReservoir
from src.security_policy import Policy
from src.incident_manager import IncidentCounter, QuarantineManager
from src.pqc_wrapper import PQCWrapper


APPROVED = ["ML-KEM-768", "ML-KEM-1024"]
CURRENT = APPROVED[0]

policy = Policy()
qreservoir = QuantumReservoir()
counter = IncidentCounter()
quarantine_manager = QuarantineManager()
wrapper = PQCWrapper()


def log(event, **data):
    print(f"[AUDIT] {event} | {data}")


def threat_monitor(signal):
    risk, counts, features = qreservoir.run(signal)

    print("\n[QRC] Quantum reservoir output")
    print("Measurement counts:", counts)
    print("Quantum features:", features)
    print("Quantum risk score:", risk)

    log("QRC_RISK_ANALYSIS", risk=risk, features=features)
    return risk


def verify_incident(score):
    confirmed = score >= policy.max_risk
    log("INCIDENT_VERIFICATION", score=score, confirmed=confirmed)
    return confirmed


def security_verification(data):
    valid = data.get("integrity_ok", False)
    log("SECURITY_CHECK", integrity=valid)
    return valid


def change_algorithm():
    global CURRENT

    old = CURRENT
    alternatives = [a for a in APPROVED if a != CURRENT]

    if not alternatives:
        raise RuntimeError("No approved PQC alternative available")

    CURRENT = alternatives[0]
    log("ALGORITHM_CHANGED", old=old, new=CURRENT)


def re_establish_security(session_id):
    new_session = f"{session_id}-NEW-{int(time())}"
    log(
        "SECURITY_REESTABLISHED",
        algorithm=CURRENT,
        session=new_session,
    )
    return new_session


def process_request(session_id, data, signal):
    print("\n" + "=" * 60)
    print("ADAPTIVE QUANTUM-RESILIENT SECURITY")
    print("=" * 60)

    print(f"\nCurrent PQC algorithm: {CURRENT}")

    encrypted = wrapper.encrypt(data)

    risk = threat_monitor(signal)
    suspicious = risk >= policy.suspicious_risk

    if not suspicious:
        print("\n✓ NO SUSPICIOUS ACTIVITY")
        print("→ CONTINUE NORMAL OPERATION")
        log("NORMAL_OPERATION", session=session_id)
        return encrypted

    print("\n⚠ SUSPICIOUS ACTIVITY DETECTED")

    count = counter.increase()
    print(f"Attack count: {count}/{policy.threshold}")
    log("SUSPICIOUS_ACTIVITY", count=count, risk=risk)

    if not verify_incident(risk):
        print("\n→ INCIDENT NOT CONFIRMED")
        print("→ CONTINUE MONITORING")
        return encrypted

    if count < policy.threshold:
        print("\n→ THRESHOLD NOT REACHED")
        print("→ MONITORING CONTINUES")
        return encrypted

    print("\n🚫 THRESHOLD REACHED")
    print("→ BLOCK SUSPICIOUS SESSION")
    log("SESSION_BLOCKED", session=session_id)

    quarantine_manager.quarantine(session_id)

    if not security_verification(data):
        print("\n⚠ SECURITY VERIFICATION FAILED")
        print("→ DATA REMAINS QUARANTINED")
        return None

    print("\n✓ SECURITY VERIFICATION PASSED")

    print("\n→ CHANGING APPROVED PQC ALGORITHM")
    change_algorithm()

    new_session = re_establish_security(session_id)

    quarantine_manager.release(session_id)
    counter.reset()

    print("\n✓ SECURITY RE-ESTABLISHED")
    print("✓ RESUME SECURE DATA")

    log("SYSTEM_RESUMED", session=new_session, algorithm=CURRENT)

    return wrapper.encrypt(data)


def main():
    session = "SESSION-001"

    data = {
        "message": "Sensitive PQC data",
        "integrity_ok": True,
    }

    normal_signal = {
        "authentication": 0.05,
        "traffic": 0.10,
        "integrity": 0.05,
        "session": 0.05,
        "policy": 0.00,
    }

    suspicious_signal = {
        "authentication": 0.90,
        "traffic": 0.90,
        "integrity": 0.90,
        "session": 0.80,
        "policy": 0.90,
    }

    print("\n\nNORMAL TEST")
    process_request(session, data, normal_signal)

    for i in range(3):
        print(f"\n\n========== EVENT {i + 1} ==========")
        process_request(session, data, suspicious_signal)


if __name__ == "__main__":
    main()
