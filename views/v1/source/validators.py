import wtforms
from wtforms.validators import DataRequired, Optional, NumberRange, Length
from wtforms import ValidationError
from plugins.public.validators import BaseForm, InputRequired


class SourceListForm(BaseForm):
    page = wtforms.IntegerField(validators=[DataRequired()])
    limit = wtforms.IntegerField(validators=[NumberRange(min=1, max=50)], default=10)
    keyword = wtforms.StringField(default=None)