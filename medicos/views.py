from django.http import request
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medico, Agenda, Especialidade, Cliente


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
                               self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")


class MedicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Medico
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'telefone', 'especialidade']
    success_url = reverse_lazy('medicos:medicos_lista')


class MedicoUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Medico
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'telefone', 'especialidade']
    success_url = reverse_lazy('medicos:medicos_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MedicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'medicos/medicos_list.html'

    def get_queryset(self):
        return Medico.objects.all().order_by('-pk')


class MedicoDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Medico
    success_url = reverse_lazy('medicos:medicos_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Profissional excluído com sucesso!")
        return reverse_lazy('medicos:medicos_lista')


class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome']
    success_url = reverse_lazy('medicos:especialidade_lista')


class EspecialidadeUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome']
    success_url = reverse_lazy('medicos:especialidade_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'medicos/especialidade_list.html'

    def get_queryset(self):
        return Especialidade.objects.all().order_by('-pk')


class EspecialidadeDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Especialidade
    success_url = reverse_lazy('medicos:especialidade_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Procedimento excluído com sucesso!")
        return reverse_lazy('medicos:especialidade_lista')


class ClienteCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Cliente
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('medicos:cliente_lista')


class ClienteUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Cliente
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('medicos:cliente_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClienteDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('medicos:cliente_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Cliente excluído com sucesso!")
        return reverse_lazy('medicos:cliente_lista')


class ClienteListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'medicos/cliente_list.html'

    def get_queryset(self):
        return Cliente.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario', 'cliente']
    success_url = reverse_lazy('medicos:agenda_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario', 'cliente']
    success_url = reverse_lazy('medicos:agenda_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('medicos:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('medicos:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return Agenda.objects.filter(dia__icontains=search).order_by('dia')
        else:
            return Agenda.objects.all().order_by('dia')


medico_cadastro = MedicoCreateView.as_view()
medico_atualizar = MedicoUpdateView.as_view()
medico_lista = MedicoListView.as_view()
medico_deletar = MedicoDeleteView.as_view()

especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_atualizar = EspecialidadeUpdateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()
especialidade_deletar = EspecialidadeDeleteView.as_view()

cliente_cadastro = ClienteCreateView.as_view()
cliente_atualizar = ClienteUpdateView.as_view()
cliente_lista = ClienteListView.as_view()
cliente_deletar = ClienteDeleteView.as_view()

agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()
