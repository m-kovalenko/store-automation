import enum


class OrderStatus(enum.IntEnum):
    in_progress = 1
    processed = 2
    paid = 3


class UserRole(enum.IntEnum):
    cashier = 1
    salesman = 2
    accountant = 3
