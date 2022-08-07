from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

MIN_AGE = 9
STOP_DOMAIN = 'rambler'


def nine_years_older(value: date):
    if relativedelta(date.today(), value).year < MIN_AGE:
        raise ValidationError("Your age must be over 9 years old.")


def except_rambler(value: str):
    domain_name = value.split('@')
    if STOP_DOMAIN in domain_name[1]:
        raise ValidationError("Registration with Rambler is prohibited.")
