from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse

from . import models
from .forms import *

class Index(ListView):
    template_name = 'index.html'
    model = models.Proposal

class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'cadastro.html'
    success_url = reverse_lazy('voting:login')
    form_class = RegistrationUserForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.set_password(obj.password)
    	obj.save()
    	return super(UserCreateView, self).form_valid(form)

class AddProposalView(CreateView):
	model = models.Proposal
	template_name = 'add-proposal.html'
	success_url = reverse_lazy('voting:index')
	form_class = AddProposal

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(AddProposalView, self).form_valid(form)

class Vote(DetailView):
	model = models.Proposal
	template_name = 'proposta.html'

	def get_context_data(self, **kwargs):
		#kwargs['proposals'] = models.Proposal.objects.all()
		kwargs['comments'] = models.Comment.objects.filter(proposal = self.object.pk)
		return super(Vote, self).get_context_data(**kwargs)


class Vote2(DetailView):
	model = models.Proposal
	template_name = 'comment_list.html'
	
	def get_context_data(self, **kwargs):
		kwargs['comments'] = models.Comment.objects.filter(proposal = self.object.pk)
		return super(Vote2, self).get_context_data(**kwargs)

class Approve(CreateView):
	model = models.Vote
	template_name = 'votosim.html'
	success_url = reverse_lazy('voting:index')
	form_class = ApproveForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(Approve, self).form_valid(form)
	# def get_queryset(self):
	# 	if 'proposal' in self.request.GET:
	# 		return models.Vote.objects.filter(proposal=self.request.GET['proposal'])
	# 	return models.Vote.objects.all()
class CommentView(CreateView):
	model = models.Comment
	template_name = 'comment.html'
	success_url = reverse_lazy('voting:index')
	form_class = CommentForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(CommentView, self).form_valid(form)
# class VoteUp(UpdateView):
# 	model = models.Proposal
# 	template_name = 
# 	success_url = reverse_lazy()
# 	fields = ['comment']