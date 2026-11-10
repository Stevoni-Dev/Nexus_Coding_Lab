"""Audit module for tracking customer-related actions. Will be stored in memory"""


class AuditEntry:
    def __init__(self):
        self.audit_log = []

# customer_id, actor_id and the trimmed reason
    def log_action(self, actor_id: str, customer_id: str, reason: str = ""):
        self.audit_log.append({
            "actor_id": actor_id,
            "customer_id": customer_id,
            "reason": reason,
        })