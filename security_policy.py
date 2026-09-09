"""Security policy configuration."""

from dataclasses import dataclass


@dataclass
class Policy:
    threshold: int = 3
    max_risk: float = 0.70
    suspicious_risk: float = 0.40
