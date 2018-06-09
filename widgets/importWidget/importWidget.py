import models.widgets
from models.decorators import check_session
from widgets.importWidget.processing import create_transaction
from models.database.db_session import get_db_session
import csv
from flask import render_template, request
blueprint = models.widgets.blueprints["importWidget"]


@blueprint.route('/')
def entry_point():
    return render_template('import.html')


@blueprint.route('/import', methods=['POST'])
@check_session
def upload(user, key):
    file = request.files['csv_file']
    text = [line.decode('latin-1').rstrip('\r\n') for line in file.stream]
    delimiter = request.form.get('char')
    csvreader = csv.reader(text, delimiter=delimiter)
    account_id = request.form.get('account_id')
    dbs = get_db_session()
    for row in csvreader:
        if len(row) < 5:
            continue
        date_created = row[0].encode('utf-8')
        date_valuta = row[4].encode('utf-8')
        description = row[1].encode('utf-8')
        amount = (row[2] + row[3]).encode('utf-8')
        account_id = account_id
        create_transaction(date_created=date_created, date_valuta=date_valuta, description=description, amount=amount,
                           account_id=account_id, encryption_key=key, db_session=dbs)
    dbs.commit()
    return request.form.get('char')
