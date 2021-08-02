from typing import Any
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import InputTextForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import InputText


class InputTextView(generic.edit.FormView):
    form_class = InputTextForm
    template_name = "sentimentAnalysis/index.html"
    success_url = "predict/"

    def form_valid(self, form):
        print('success!')
        form.save()
        return super().form_valid(form)


def predict(request):
    return HttpResponseRedirect(reverse('sentimentAnalysis:index'))
