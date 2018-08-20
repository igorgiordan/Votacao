
from django import forms

from . import models

class RegistrationUserForm(forms.ModelForm):
  
  class Meta:
    model = models.UUIDUser
    fields = ('first_name', 'last_name', 'username', 'email', 'password')
    labels = {
    	'first_name': 'Primeiro Nome',
    	'last_name': 'Sobrenome',
    	'username': 'Nome de Usuário',
    	'email': 'E-mail',
    	'password': 'Senha',
    }
    widgets = {
      'password': forms.PasswordInput()
    }

class AddProposal(forms.ModelForm):

	class Meta:
		model = models.Proposal
		fields = ('name', 'description')
		labels = {
    		'name': 'Nome da Proposta',
    		'description': 'Descrição',
    	}

class ApproveForm(forms.ModelForm):
		class Meta:
			model = models.Vote
			aux = models.Vote.objects.all()
			fields = ('kind', 'proposal')
			labels = {
				'kind': 'Tipo:',
				'proposal': 'Proposta',
			}

class CommentForm(forms.ModelForm):
		class Meta:
			model = models.Comment
			fields = ('text', 'proposal')
			labels = {
					'text': 'Comente:',
					'proposal': 'Proposta',
				}	