# ledger

Reference version of `ledger`, the application built step by step in the labs of **Software Management & Development** (IE University, MFT & MCSDI). The labs and notes are at [ami232/ie-smd](https://github.com/ami232/ie-smd).

`ledger` keeps the transactions of your accounts in a database and prints the balance of each account, the spending by category and the net change of each month.

## Versions

Each tag is one state of the project, the solution of one lab:

| Tag | Contents |
|---|---|
| `s05-start`, `ledger-script` | the ledger as one file: Python 3.14 project with uv, `rich` for the table, Ruff as a development dependency, a VS Code debug configuration |
| `ledger-package` | a package with `models`, `storage`, `reports` and `cli`, a `months` command, Ruff rules in `pyproject.toml` |
| `ledger-sqlite` | the transactions in a SQLite database through SQLAlchemy (`db.py`), with `import` and `add` commands; `models.py` and `reports.py` as in `ledger-package` |

If you fall behind, copy the files of the tag you need into your own repository (on GitHub: switch to the tag, then **Code → Download ZIP**). Don't fork or clone this repository as your own: your repository must have your own history.

## Run it

```bash
uv run ledger import      # loads data/transactions.csv into ledger.db
uv run ledger balance
uv run ledger spending
uv run ledger months
uv run ledger add checking -12.50 restaurants "Lunch"
```
