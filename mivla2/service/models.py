
import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Каждому пользователю нужен понятный человеку уникальный идентификатор,
    # который мы можем использовать для предоставления User в пользовательском
    # интерфейсе. Мы так же проиндексируем этот столбец в базе данных для
    # повышения скорости поиска в дальнейшем.
    username = models.CharField(db_index=True, max_length=255, unique=True)

    # Так же мы нуждаемся в поле, с помощью которого будем иметь возможность
    # связаться с пользователем и идентифицировать его при входе в систему.
    # Поскольку адрес почты нам нужен в любом случае, мы также будем
    # использовать его для входы в систему, так как это наиболее
    # распространенная форма учетных данных на данный момент (ну еще телефон).
    email = models.EmailField(db_index=True, unique=True)

    # Когда пользователь более не желает пользоваться нашей системой, он может
    # захотеть удалить свой аккаунт. Для нас это проблема, так как собираемые
    # нами данные очень ценны, и мы не хотим их удалять :) Мы просто предложим
    # пользователям способ деактивировать учетку вместо ее полного удаления.
    # Таким образом, они не будут отображаться на сайте, но мы все еще сможем
    # далее анализировать информацию.
    is_active = models.BooleanField(default=True)

    # Этот флаг определяет, кто может войти в административную часть нашего
    # сайта. Для большинства пользователей это флаг будет ложным.
    is_staff = models.BooleanField(default=False)

    # Временная метка создания объекта.
    created_at = models.DateTimeField(auto_now_add=True)

    # Временная метка показывающая время последнего обновления объекта.
    updated_at = models.DateTimeField(auto_now=True)

    # Дополнительный поля, необходимые Django
    # при указании кастомной модели пользователя.

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.username


class Colours(BaseModel):
    class Meta:
        db_table = 'colours'
    colour_id = models.BigAutoField(primary_key=True)
    colour_name = models.CharField(null=False, max_length=30)

    def __str__(self):
        return f'Цвет - {self.colour_name}'


class Diler(BaseModel):
    class Meta:
        db_table = 'diler'
    diler_id = models.AutoField(primary_key=True)
    diler_name = models.CharField(null=False, max_length=30)
    is_related = models.BooleanField(null=False)

    def __str__(self):
        return f'Поставщик - {self.diler_name}'


class Shipment(BaseModel):
    class Meta:
        db_table = 'shipment'
    ship_id = models.BigAutoField(primary_key=True)
    ship_date = models.DateField(null=False)
    weight = models.FloatField(max_length=30)
    diler = models.ForeignKey(Diler, on_delete=models.CASCADE)

    def __str__(self):
        return f'Поставка №{self.ship_id}'


class Furniture(BaseModel):
    class Meta:
        db_table = 'furniture'

    length = models.FloatField(max_length=20, null=False, blank=False)
    height = models.FloatField(max_length=20, null=False, blank=False)
    depth = models.FloatField(max_length=20, null=False, blank=False)
    ship = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE)


class Sofa(BaseModel):
    class Meta:
        db_table = 'sofa'

    self_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(Furniture, on_delete=models.PROTECT)
    num_seats = models.IntegerField(null=False, blank=False)
    expand = models.BooleanField(null=False)
    corner = models.BooleanField(null=False)

    def __str__(self):
        if self.expand:
            return f"Диван угловой {self.self_id}"
        else:
            return f"Диван {self.self_id}"


class Wardrobe(BaseModel):
    class Meta:
        db_table = 'wardrobe'

    self_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(Furniture, on_delete=models.PROTECT)
    num_shelfs = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Шкаф {self.self_id}"


class Stol(BaseModel):
    class Meta:
        db_table = 'stol'

    self_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(Furniture, on_delete=models.PROTECT)
    expand = models.BooleanField(null=False)

    def __str__(self):
        if self.expand:
            return f"Стол угловой {self.self_id}"
        else:
            return f"Стол {self.self_id}"


class Orders(BaseModel):
    class Meta:
        db_table = 'orders'

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order_date = models.DateField(null=False)
    order_cost = models.FloatField(max_length=15, null=False)
    product = models.ForeignKey(Furniture, on_delete=models.PROTECT)

