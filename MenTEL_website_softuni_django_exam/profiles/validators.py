from django.core.exceptions import ValidationError

def username_letter_validator(value):
    for char in value:
        if not char.isallnum() and char != "_":
            raise ValidationError("Username can contain only letters, digits and underscores!")
