# ledger

Reference version of `ledger`, the application built step by step in the labs of **Software Management & Development** (IE University, MFT & MCSDI). The labs and notes are at [ami232/ie-smd](https://github.com/ami232/ie-smd).

`ledger` keeps the transactions of your accounts in a database and prints the balance of each account, the spending by category and the net change of each month.

## Versions

Each tag is the state of the project **at the start of a session**, which is also the solution of the previous lab:

| Tag | Start of | Contents |
|---|---|---|
| `s05-start` | session 5 (Git) | the result of Lab 4: Python 3.14 project with uv, `rich` for the table, Ruff as a development dependency, a VS Code debug configuration |
| `s06-start` | session 6 (project structure) | the same code as `s05-start`: Lab 5 only put it in a repository |
| `s07-start` | session 7 (databases) | the result of Lab 6: a package with `models`, `storage`, `reports` and `cli`, a `months` command, Ruff rules in `pyproject.toml` |
| `s08-start` | session 8 (API) | the result of Lab 7: the transactions in a SQLite database through SQLAlchemy, with `import` and `add` commands |

If you fall behind, copy the files of the tag for your session into your own repository (on GitHub: switch to the tag, then **Code → Download ZIP**). Don't fork or clone this repository as your own: your repository must have your own history.

## Run it

```bash
uv run ledger import      # loads data/transactions.csv into ledger.db
uv run ledger balance
uv run ledger spending
uv run ledger months
uv run ledger add checking -12.50 restaurants "Lunch"
```
