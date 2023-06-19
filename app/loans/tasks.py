from celery import shared_task
from django.core import serializers

@shared_task(name='verify_status_loans')
def task_verify_status_loans(instance):
    deserialized_instances = serializers.deserialize('json', instance)
    if deserialized_instances:
        for deserialized_obj in deserialized_instances:
            instance = deserialized_obj.object       
            if instance.id % 2 == 0: instance.status = False
            else: instance.status = True
        instance.save()
