from django.db import models
from django.core.validators import RegexValidator

class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated_at')

    class Meta:
        abstract = True

class Loans(Timestamp):
    name = models.CharField(max_length=100, verbose_name='name')
    cpf = models.CharField(
        verbose_name='cpf',
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex="^[0-9]{11}$",
            )
        ],
    )
    address = models.CharField(max_length=300, verbose_name='address')
    value = models.FloatField(verbose_name='value')
    status = models.BooleanField(verbose_name='status', default=False, null=False, blank=False)

    def __str__(self) -> str:
        return self.name