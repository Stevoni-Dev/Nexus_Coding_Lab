"""Audit module for tracking customer-related actions. Will be stored in memory"""


class AuditEntry:       

# customer_id, actor_id and the trimmed reason
    def log_action(self, actor_id: str, customer_id: str, reason: str = ""):
        raise NotImplementedError("This method should be implemented by subclasses")


class InMemoryAuditEntry(AuditEntry):
    def __init__(self):
        self.audit_log = []

    def log_action(self, actor_id: str, customer_id: str, reason: str = ""):
        self.audit_log.append({
            "actor_id": actor_id,
            "customer_id": customer_id,
            "reason": reason,
        })

class SqlAuditEntry(AuditEntry):
    def log_action(self, actor_id: str, customer_id: str, reason: str = ""):
        # Here you would implement the logic to store the audit entry in a SQL database
        raise NotImplementedError("SQL audit logging not implemented yet")