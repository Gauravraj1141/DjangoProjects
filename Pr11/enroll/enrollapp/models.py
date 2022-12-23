from django.db import models
from datetime import datetime
import json
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete

from django.dispatch import receiver
# Create your models here.


class tasks(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    remiander = models.BooleanField()


class taskdate(models.Model):
    taskname = models.ForeignKey(tasks, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)


class taskhistory(models.Model):
    taskhis = models.TextField(default='{}')


@receiver(pre_save, sender=tasks)
def pre_save_signal(sender, instance, **kwargs):
    print("-------------")
    print("presave task signal generated ")
    print(instance.name)
    print(instance.desc)
    print(instance.remiander)


# when we add our task then signal will generated and here we add date  in the taskdata

@receiver(post_save, sender=tasks)
def Post_save_signal(sender, instance, **kwargs):
    print("-------------")
    print("Post task signal generated ")
    taskdate.objects.create(taskname=instance, date=datetime.now())
    print('successfully added ...')


@receiver(pre_delete, sender=tasks)
def Pre_delete_signal(sender, instance, **kwargs):
    print("-------------")
    print("Pre delete signal generated............. ")
    history = {'task': instance.name, 'desc': instance.desc,
               "remainder": instance.remiander}
    historydata = json.dumps(history)
    print("hey history data is : >> ", historydata)
    taskhistory.objects.create(taskhis=historydata)
    print('successfully added ...')


@receiver(post_delete, sender=tasks)
def Post_delete_signal(sender, instance, **kwargs):
    print("-------------")
    print("post delete signal generated............. ")
    print(instance)
