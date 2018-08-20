from __future__ import unicode_literals

import uuid


from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission

class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
     return "%s" %(self.first_name)
  
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class Proposal(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='UUIDUser')
    name = models.CharField(max_length=150, verbose_name='nome')
    description = models.TextField(verbose_name='descrição')

    def __str__(self):
     return "%s" %(self.name)

    class Meta:
        verbose_name = 'proposta'
        verbose_name_plural = 'propostas'

class Vote(models.Model):
    kindchoice = (
        (1, 'sim'),
        (2, 'não')
    )
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='UUIDUser2')
    kind = models.IntegerField(choices=kindchoice, verbose_name="tipo")
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='proposta')


    def __str__(self):
        return "%s" %(self.kind)

    class Meta:
        verbose_name = 'voto'
        verbose_name_plural = 'votos'

class Comment(models.Model):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='UUIDUser3')
    text = models.TextField(verbose_name='comentário')
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='proposta2')

    def __str__(self):
        return "%s" %(self.text)

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'