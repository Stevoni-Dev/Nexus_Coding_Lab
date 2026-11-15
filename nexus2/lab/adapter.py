"""Lab wiring, not upstream Nexus code. Adapt this to your design.
Do not manufacture audit records in this adapter: production code must write them.
"""
from types import SimpleNamespace
from northstar.auth import AuthorizationService
from northstar.audit import InMemoryAuditEntry
from northstar.events import EventBus
from northstar.models import Customer
from northstar.notifications import NotificationClient, CustomerNotificationSubscriber
from northstar.repository import InMemoryCustomerRepository
from northstar.services import CustomerLifecycleService


def build():
    repository = InMemoryCustomerRepository()
    repository.save(Customer("c1", "Case Customer", "case@example.com"))
    bus = EventBus()
    client = NotificationClient()
    audit = InMemoryAuditEntry()
    bus.subscribe(CustomerNotificationSubscriber(client))
    lifecycle = CustomerLifecycleService(repository, AuthorizationService(), audit, bus)
    return SimpleNamespace(repository=repository, bus=bus, client=client,
                           lifecycle=lifecycle, audit=audit.audit_log)


def audit_records(system):
    # Return a list of mappings with customer_id, actor_id, reason.
    # Map your real audit objects here if necessary. Never synthesize the answer.
    return system.audit
