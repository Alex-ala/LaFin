from models.db_schema import Transactions
from models.database.user import encrypt


def create_transaction(date_created, date_valuta, description, amount, account_id, encryption_key, db_session):
    transaction = Transactions(date_valuta=date_valuta,
                               date_created=date_created,
                               description=encrypt(description, encryption_key),
                               amount=encrypt(amount, encryption_key),
                               account_id=account_id)
    db_session.add(transaction)
