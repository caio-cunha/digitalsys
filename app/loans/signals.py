from django.db.models.signals import post_save
from django.dispatch import receiver
from loans.models import Loans
from loans.tasks import task_verify_status_loans
from django.core import serializers

@receiver(post_save, sender=Loans, dispatch_uid='handle_loans_verify_status')
def handle_loans_verify_status(sender, instance, **kwargs):
    serialized_instance = serializers.serialize('json', [instance])
    try:
        task_verify_status_loans.delay(serialized_instance)
    except Exception as e:
        raise Exception("ERROR in task")

    

    