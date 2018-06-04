from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, ProhibitNullCharactersValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.db import models


# Validator Methods
def validate_plate(value):
    message = _('Space characters are not allowed.')
    code = 'space_characters_not_allowed'
    if " " in str(value):
        raise ValidationError(message, code=code)


# Model Classes
class User(AbstractUser):
    # Validators
    phone_regex_validator = RegexValidator(regex=r'^(.+90.(5(\d{2}).)*(\d{7}))',
                                           message=_("Phone number must be entered in the format: '+90(539)9999999'."))
    # Custom Fields
    phone_number = models.CharField(validators=[phone_regex_validator], max_length=15, blank=True)
    last_read_time = models.DateTimeField(default=datetime.now)


class Plate(models.Model):
    plate = models.CharField(validators=[ProhibitNullCharactersValidator, validate_plate], max_length=12, unique=True)
    owner = models.ForeignKey(User, db_column="user", on_delete=models.PROTECT)

    def __str__(self): return '{}'.format(self.plate)

    def __unicode__(self): return '{}'.format(self.plate)


class Message(models.Model):
    related_plate = models.ForeignKey(Plate, related_name="message_plate", on_delete=models.PROTECT)
    m_from = models.ForeignKey(User, related_name="message_from", on_delete=models.PROTECT)
    m_to = models.ForeignKey(User, related_name="message_to", on_delete=models.PROTECT)
    is_read = models.BooleanField(default=False)
