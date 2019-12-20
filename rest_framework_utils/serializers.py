from rest_framework import serializers
from .validators import phonenum_validator
from . import mixin


class PhonenumField(serializers.CharField):
    def __init__(self, **kwargs):
        super(PhonenumField, self).__init__(**kwargs)
        self.validators.append(phonenum_validator)


class Serializer(mixin.SerializerMixIn, serializers.Serializer):
    pass


class ModelSerializer(mixin.SerializerMixIn, serializers.ModelSerializer):
    pass
