from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from clientes.models import Cliente, Transacao


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


class IndexView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'index.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        return Cliente.objects.order_by('nome')


class ClienteCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Cliente
    login_url = 'accounts:login'
    template_name = 'form.html'
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('clientes:cliente_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Cliente'
        return context


class ClienteUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Cliente
    login_url = 'accounts:login'
    template_name = 'form.html'
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('clientes:cliente_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Cliente'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClienteListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'lists/cliente_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return Cliente.objects.filter(nome__icontains=search).order_by('nome')
        else:
            return Cliente.objects.all().order_by('nome')


class ClienteDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Cliente excluído com sucesso!")
        return reverse_lazy('clientes:cliente_lista')


class TransacaoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Transacao
    login_url = 'accounts:login'
    template_name = 'transacao_form.html'
    fields = ['cliente', 'data', 'descricao', 'quantidade_kg', 'tipo', 'valor_total', 'valor_kg']

    def __init__(self):
        self.success_url = None

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('clientes:transacao_lista', kwargs={'pk': kwargs['pk']})
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ultimo_parametro = self.request.path.split("/")[-2]
        context['ultimo_parametro'] = ultimo_parametro
        context['form_name'] = 'Transacao'
        form = context.get('form')
        if form:
            form.fields['cliente'].initial = ultimo_parametro

        return context


class TransacaoUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Transacao
    login_url = 'accounts:login'
    template_name = 'transacao_form.html'
    fields = ['cliente', 'data', 'descricao', 'quantidade_kg', 'tipo', 'valor_total', 'valor_kg']

    def __init__(self):
        self.success_url = None

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('clientes:transacao_lista', kwargs={'pk': kwargs['pk']})
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Transacao'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransacaoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'accounts:login'
    template_name = 'lists/transacao_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transacao_id = self.kwargs.get('pk')
        total_soma = Transacao.objects.filter(cliente__id=transacao_id).aggregate(total=Sum('quantidade_kg'))['total']
        context['total_soma'] = total_soma
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        transacao_id = self.kwargs.get('pk')

        if search:
            return Transacao.objects.filter(descricao__icontains=search, cliente__id=transacao_id).order_by('-data')
        else:
            return Transacao.objects.filter(cliente__id=transacao_id).order_by('-data')


class TransacaoDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Transacao
    success_url = reverse_lazy('clientes:transacao_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Movimentação excluída com sucesso!")
        return reverse_lazy('clientes:transacao_lista', kwargs={'pk': self.kwargs['pk']})


cliente_cadastro = ClienteCreateView.as_view()
cliente_atualizar = ClienteUpdateView.as_view()
cliente_lista = ClienteListView.as_view()
cliente_deletar = ClienteDeleteView.as_view()

transacao_cadastro = TransacaoCreateView.as_view()
transacao_atualizar = TransacaoUpdateView.as_view()
transacao_lista = TransacaoListView.as_view()
transacao_deletar = TransacaoDeleteView.as_view()

