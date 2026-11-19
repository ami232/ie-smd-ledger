"""The data the application works with, and the tables that store it."""

import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import TypeDecorator


class Money(TypeDecorator):
    """An amount: a Decimal in Python, a whole number of cents in the database."""

    impl = Integer
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        cents = value * 100
        if cents != cents.to_integral_value():
            raise ValueError(f"{value} has fractions of a cent")
        return int(cents)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return Decimal(value).scaleb(-2)


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    transactions: Mapped[list[Transaction]] = relationship(back_populates="account")


class Transaction(Base):
    """One movement of money in one account. Negative amounts are money going out."""

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date]
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    description: Mapped[str] = mapped_column(String(200))
    category: Mapped[str] = mapped_column(String(50))
    amount: Mapped[Decimal] = mapped_column(Money)

    account: Mapped[Account] = relationship(back_populates="transactions")
