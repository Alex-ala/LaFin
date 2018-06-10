from models.db_schema import Transactions
from models.database.user import encrypt, decrypt


def create_transaction(date_created, date_valuta, description, amount, account_id, encryption_key, db_session):
    existing_transactions = Transactions.query.filter_by(date_created=date_created, date_valuta=date_valuta, account_id=account_id).all()
    for et in existing_transactions:
        if decrypt(et.description, encryption_key) == description:
            return 1
    transaction = Transactions(date_valuta=date_valuta,
                               date_created=date_created,
                               description=encrypt(description, encryption_key),
                               amount=encrypt(amount, encryption_key),
                               account_id=account_id)
    db_session.add(transaction)
    return 0
