from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models,forms
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}
        query = self.request.GET.get('query', None)

        if query:
            where['title__icontains'] = query

        return query_set.filter(**where)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateFrom
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name= 'project/update.html'
    object:models.Project

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.pk])

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().user == self.request.user


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project', '')
        project = models.Project.objects.get(pk=project_id)
        return project.user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
    

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])