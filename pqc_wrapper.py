"""PQC abstraction layer for the hackathon demonstration."""


class PQCWrapper:
    """
    Demonstration-only PQC interface.

    IMPORTANT:
    This class does not implement real ML-KEM cryptography.
    Replace these methods with a vetted cryptographic library
    before using the architecture in a real security system.
    """

    def __init__(self):
        self.algorithm = "ML-KEM-768"

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def encrypt(self, data):
        print(f"[AUDIT] ENCRYPT | algorithm={self.algorithm}")
        return f"PQC_ENCRYPTED({data})"

    def decrypt(self, data):
        print(f"[AUDIT] DECRYPT | algorithm={self.algorithm}")
        prefix = "PQC_ENCRYPTED("
        if data.startswith(prefix) and data.endswith(")"):
            return data[len(prefix):-1]
        return data
