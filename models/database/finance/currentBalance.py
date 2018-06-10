from models.db_schema import Transactions, Accounts
from models.database.user import decrypt


def get_balances_for_user(user_id, encryption_key):
    # get account ids for user
    accounts = Accounts.query.filter_by(user_id=user_id)
    balances = dict()
    for account in accounts:
        balances[account.name.decode('utf-8')] = get_balance_for_account(account.id, encryption_key)
    return balances


def get_balance_for_account(account_id, encryption_key):
    transactions = Transactions.query.filter_by(account_id=account_id)
    balance = 0.0
    for transaction in transactions:
        balance += float(decrypt(transaction.amount, encryption_key).decode('utf-8'))
    currency = Accounts.query.filter_by(id=account_id).first().currency.short
    pair = dict()
    pair['currency'] = currency
    pair['value'] = balance
    return pair
