from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Weekly_schedule
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

# Create your views here.
class list_schedule(LoginRequiredMixin, ListView):
    # @login_required(login_url='/admin/login')
    model = Weekly_schedule
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for i in range(1,8):
            context['day' + str(i)] = Weekly_schedule.objects.filter(user=self.request.user).filter(day=i).order_by('start_time')
        return context

# @login_required(login_url='/admin/login/')
def add_schedule(request):
    form = ScheduleForm(request.POST or None)

    if (form.is_valid and request.method == 'POST'):
        fs = form.save(commit=False)
        fs.user= request.user
        fs.save()
        return HttpResponseRedirect('/weekly_schedule')

    response = {'form':form}
    return render(request, 'schedule_form.html', response)