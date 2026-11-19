"""Reading and writing transactions: the CSV file and the database."""

import csv
import datetime
from decimal import Decimal
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from ledger.models import Account, Transaction


def find_account(session: Session, name: str) -> Account | None:
    """The account with this name, or None if there is none."""
    return session.scalars(select(Account).where(Account.name == name)).first()


def get_or_create_account(session: Session, name: str) -> Account:
    account = find_account(session, name)
    if account is None:
        account = Account(name=name)
        session.add(account)
    return account


def import_csv(session: Session, path: Path) -> int:
    """Adds the transactions of a CSV file to the database. Returns how many."""
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        session.add(
            Transaction(
                date=datetime.date.fromisoformat(row["date"]),
                account=get_or_create_account(session, row["account"]),
                description=row["description"],
                category=row["category"],
                amount=Decimal(row["amount"]),
            )
        )
    session.commit()
    return len(rows)


def load_transactions(session: Session) -> list[Transaction]:
    """All the transactions in the database, oldest first."""
    return list(session.scalars(select(Transaction).order_by(Transaction.date)))


def add_transaction(
    session: Session,
    account_name: str,
    amount: Decimal,
    category: str,
    description: str,
    date: datetime.date,
) -> Transaction:
    """Records one transaction in an existing account."""
    account = find_account(session, account_name)
    if account is None:
        raise ValueError(f"there is no account called {account_name!r}")
    if amount != round(amount, 2):
        raise ValueError(f"{amount} has more than two decimals")
    transaction = Transaction(
        date=date,
        account=account,
        description=description,
        category=category,
        amount=amount,
    )
    session.add(transaction)
    session.commit()
    return transaction
