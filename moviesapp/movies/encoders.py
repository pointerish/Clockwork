from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model

class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):

        if isinstance(o, Model):
            return model_to_dict(o)

        return super().default(o)
