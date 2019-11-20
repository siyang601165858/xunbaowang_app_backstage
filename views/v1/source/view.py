import json
import base64
from flask import request
from views.v1.source import api


@api.route('/callback/', methods=['GET', 'POST'])
def callback():
    print(json.loads(base64.b64decode(request.data).decode()))
    return 'success'