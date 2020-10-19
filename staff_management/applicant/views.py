from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from applicant.forms import ApplicantUserUpdateForm
from applicant.models import ApplicantUser
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView,ListView
# from .mixins import GroupRequiredMixin
from applicant.helpers import PaginationHelper
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_obj = request.user

        if user_obj.is_admin:
            print("admin_home")
            context = {'user':user_obj}
            return render(request, 'pages/admin_home.html', context)

        else:
            print("applicant_home")

            context = {'user':user_obj}
            return render(request, 'pages/applicant_home.html', context)

    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)



class ApplicantDetailView(LoginRequiredMixin, DetailView):

    model = ApplicantUser

    slug_field = "id"
    slug_url_kwarg = "id"
    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailView, self).get_context_data(**kwargs)
        context['form'] = ApplicantUserUpdateForm()
        return context


applicant_detail_view = ApplicantDetailView.as_view()

# class ApplicationUpdateView()
class ApplicantUpdateView(LoginRequiredMixin, UpdateView):

    model = ApplicantUser
    # fields = ["full_name"]
    fields = ['full_name','mobile',
    'aadhaar',
    'chronic_disease',
    'child_disease',
    'disabled',
    'gender',
    'dob',
    'marital_status',
    'district',
    'school',
    'join_date']
    def get_success_url(self):
        return reverse("applicant:detail", kwargs={"id": self.request.user.id})

    def get_object(self):
        # print(self.request.user)
        # import ipdb;ipdb.set_trace()
        return ApplicantUser.objects.get(id=self.request.user.id)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)




class ApplicantUserBaseView( View, PaginationHelper):

    """
    Base view for Flash
    """
    group_required = ['fauthor', 'sadmin']

    def get_app_user(self):
        return get_object_or_404(
            ApplicantUser.objects.all(),
            pk=self.kwargs.get('id')
        )


class ApplicantUserListView(View, PaginationHelper):
    """
    Flash Create View
    """

    def get(self, request, *args, **kwargs):

        app_user = self.paginate(request, ApplicantUser.objects.all())

        return render(
            request,
            'applicant/app_user_list.html',
            {
                'app_user': app_user,
            }
        )


class ApplicantUserJsonView(BaseDatatableView):
    """
    Model list view.
    """

    model = ApplicantUser
    columns = ['email',
    'full_name',
    'gender',
    'school',
    'au_points',
    'direct_eligible',
    'id'
    ]
    order_columns = [
        'au_points',
 
    ]

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'id':
            # escape HTML for security reasons
            return super(ApplicantUserJsonView, self).render_column(row, column)
        else:
            return super(ApplicantUserJsonView, self).render_column(row, column)

    def get_initial_queryset(self):
        # import ipdb;ipdb.set_trace()
        return ApplicantUser.objects.filter(email__staff=False).order_by('-au_points')

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(full_name__icontains=search) 

                # Q(year_model_year__icontains=search)
            )
        return qs

