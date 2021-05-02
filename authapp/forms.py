from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'Введите имя пользователя'

            if field_name == 'password':
                field.widget.attrs['placeholder'] = 'Введите пароль'

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'avatar':
                field.widget.attrs['class'] = 'form-control py-4'
            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'Введите имя пользователя'
            if field_name == 'email':
                field.widget.attrs['placeholder'] = 'Введите адрес эл. почты'
            if field_name == 'first_name':
                field.widget.attrs['placeholder'] = 'Введите имя'
            if field_name == 'last_name':
                field.widget.attrs['placeholder'] = 'Введите фамилию'
            if field_name == 'password1':
                field.widget.attrs['placeholder'] = 'Введите пароль'
            if field_name == 'password2':
                field.widget.attrs['placeholder'] = 'Подтвердите пароль'
            if field_name == 'age':
                field.widget.attrs['placeholder'] = 'Введите возраст'
            if field_name == 'city':
                field.widget.attrs['placeholder'] = 'Введите город'

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'age', 'city', 'avatar')

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data['age']
        try:
            if age < 18 or age > 150:
                self.add_error('age', 'Check the age. 18 is minimum.')
        except:
            pass
