from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class MyClubUser(AbstractBaseUser):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    password1 = models.CharField(verbose_name='Password', max_length=20, null=True)
    password2 = models.CharField(verbose_name='Password confirmation', max_length=20, null=True)
    objects = UserManager()
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)


class Item(models.Model):
    name = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="items")
    image = models.ImageField(null=True)
    price = models.IntegerField(null=True)


class Order(models.Model):
    notes = models.TextField(blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)


class Feedback(models.Model):
    msg = models.CharField(max_length=120, null=True)


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120, null=True)
    event_date = models.DateTimeField('Event Date', null=True)
    attendees = models.IntegerField(null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
