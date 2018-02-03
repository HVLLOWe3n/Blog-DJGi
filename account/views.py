from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from django.views.generic.base import View


class UserFormView(View):
    form_class = UserForm

    def get(self, request):
        form = self.form_class(None)

        context = {
            'forms': form
        }

        return render(request, 'logup.html', context)

    def post(self, request):
        form = self.form_class(request.POST)

        context = {
            'forms': form
        }

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, 'logup.html', context)
