from django.db.models import TextChoices


# Role user options
class RoleUserChoices(TextChoices):
    NORMAL = 'normal_user', 'normal user'
    SUPER = 'super_user', 'super user'
