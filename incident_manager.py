"""Incident counting and session quarantine management."""


class IncidentCounter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0


class QuarantineManager:
    def __init__(self):
        self.sessions = set()

    def quarantine(self, session_id):
        self.sessions.add(session_id)
        print(f"[AUDIT] QUARANTINE | {{'session': '{session_id}'}}")

    def release(self, session_id):
        self.sessions.discard(session_id)
        print(f"[AUDIT] QUARANTINE_RELEASED | {{'session': '{session_id}'}}")

    def is_quarantined(self, session_id):
        return session_id in self.sessions
