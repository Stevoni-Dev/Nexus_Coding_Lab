import pytest
from unittest.mock import Mock

from northstar.auth import Actor
from northstar.errors import CustomerNotFoundError


def test_deactivate_customer(registration, lifecycle):
    customer = registration.register(
        Actor("u1", "admin"),
        "Carlos Rivera",
        "carlos@example.com",
    )
    updated = lifecycle.deactivate(
        Actor("u2", "manager"),
        customer.customer_id,
        "Requested by customer",
    )
    assert updated.active is False


def test_deactivate_sends_notification(registration, lifecycle, notifications):
    customer = registration.register(
        Actor("u1", "admin"),
        "Jordan Lee",
        "jordan@example.com",
    )
    notifications.sent_messages.clear()

    lifecycle.deactivate(
        Actor("u2", "manager"),
        customer.customer_id,
        "Duplicate account",
    )
    assert notifications.sent_messages == [
        ("jordan@example.com", "Your Atlas account has been deactivated.")
    ]

# def test_deactivation_notification_failure_error(registration, lifecycle, notifications):
#     customer = registration.register(
#         Actor("u1", "admin"),
#         "Alex Morgan",
#         "alex@example.com",
#     )
#     # Mock the send method to raise an exception
#     Mock.patch.object(notifications, "send", side_effect=Exception("Notification failed")).start()

#     with pytest.raises(Exception, match="Notification failed"):
#         lifecycle.deactivate(
#             Actor("u2", "manager"),
#             customer.customer_id,
#             "Requested by customer",
#         )
#     assert notifications.sent_messages == []
#     assert not lifecycle.is_active(customer.customer_id)


def test_deactivate_missing_customer_raises(lifecycle):
    with pytest.raises(CustomerNotFoundError):
        lifecycle.deactivate(
            Actor("u1", "admin"),
            "missing",
            "Requested by customer",
        )


def test_deactivate_requires_reason(registration, lifecycle):
    customer = registration.register(
        Actor("u1", "admin"),
        "Taylor Kim",
        "taylor@example.com",
    )
    with pytest.raises(ValueError):
        lifecycle.deactivate(
            Actor("u1", "admin"),
            customer.customer_id,
            "no",
        )
