from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm
from django.views.generic.base import View


class UserFormView(View):
    form_class = UserForm  # Получаем класс формы

    def get(self, request):  # функция отправки с сервера
        form = self.form_class(None)

        context = {
            'forms': form
        }

        return render(request, 'logup.html', context)

    def post(self, request):  # функция получения от пользователя
        form = self.form_class(request.POST)  # принимем пост запрос

        context = {
            'forms': form
        }

        if form.is_valid():  # проверка формы на валидность
            user = form.save(commit=False)
            username = form.cleaned_data['username']  # Получаем username
            password = form.cleaned_data['password']  # Получаем password

            user.set_password(password)  # записываем новый пароль в базу и шифруем
            user.save()  # сохраняем

            user = authenticate(username=username, password=password)  # Применияем аутентификацию

            if user is not None:

                if user.is_active:
                    login(request, user)  # Авторизация
                    return redirect('/')

        return render(request, 'logup.html', context)


def logout_user(request):
    context = { }
    logout(request)

    return render(request, 'logout.html', context)
