import models.widgets
from models.database.user import decrypt
from models.db_schema import Transactions
from models.decorators import check_session
blueprint = models.widgets.blueprints["testWidget"]

@blueprint.route('/')
@check_session
def entry_point(userid, key):
    return "TEEEEST"
