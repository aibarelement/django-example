from rest_framework import serializers


def title_validator(value):
    if value == 'super':
        raise serializers.ValidationError('This field must not be equal to "super"')


class TitleValidator:

    def __call__(self, value):
        if value == 'super':
            raise serializers.ValidationError('This field must not be equal to "super"')