"""Qiskit-based quantum reservoir used for demonstration risk scoring."""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


class QuantumReservoir:
    def __init__(self, shots: int = 1000):
        self.shots = shots
        self.backend = AerSimulator()

    def _build_circuit(self, inputs: dict) -> QuantumCircuit:
        x1 = inputs["authentication"]
        x2 = inputs["traffic"]
        x3 = inputs["integrity"]
        x4 = inputs["session"]
        x5 = inputs["policy"]

        angle0 = (0.20 * x1 + 0.20 * x2 + 0.30 * x3) * 3.14159
        angle1 = (0.15 * x4 + 0.15 * x5) * 3.14159

        qc = QuantumCircuit(2, 2, name="quantum_reservoir")

        qc.ry(angle0, 0)
        qc.ry(angle1, 1)

        qc.cx(0, 1)
        qc.rx(0.7, 0)
        qc.rz(0.4, 1)
        qc.cx(1, 0)
        qc.ry(0.5, 0)
        qc.rx(0.3, 1)

        qc.measure(0, 0)
        qc.measure(1, 1)

        return qc

    def run(self, inputs: dict):
        qc = self._build_circuit(inputs)
        compiled = transpile(qc, self.backend)

        result = self.backend.run(
            compiled,
            shots=self.shots,
        ).result()

        counts = result.get_counts()
        total = sum(counts.values())

        p00 = counts.get("00", 0) / total
        p01 = counts.get("01", 0) / total
        p10 = counts.get("10", 0) / total
        p11 = counts.get("11", 0) / total

        features = [p00, p01, p10, p11]

        risk = (
            0.10 * p00
            + 0.20 * p01
            + 0.30 * p10
            + 0.40 * p11
        )

        return round(risk, 3), counts, features
