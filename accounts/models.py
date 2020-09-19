from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from profiles.models import Profile


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email or not username or not first_name or not last_name or not password:
            raise ValueError(
                "Users must have email, username, password, first name and last name")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        if not email or not username or not first_name or not last_name or not password:
            raise ValueError(
                "Users must have email, username, password, first name and last name")
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    class Types(models.TextChoices):
        COACH = "COACH", "Coach"
        CLIENT = "CLIENT", "Client"

    type = models.CharField(verbose_name="Type", max_length=10,
                            choices=Types.choices, default=Types.CLIENT)

    email = models.EmailField(verbose_name="email",
                              max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=30)
    last_name = models.CharField(verbose_name="last name", max_length=40)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class CoachManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.COACH)


class CoachExtra(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    workout_price = models.DecimalField(
        max_digits=15, decimal_places=3, default=0.000)
    meal_price = models.DecimalField(
        max_digits=15, decimal_places=3, default=0.000)


class Coach(Account):
    objects = CoachManager()

    @property
    def extra(self):
        return self.coachextra

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Account.Types.COACH
        return super().save(*args, **kwargs)


class ClientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.CLIENT)


class Client(Account):
    objects = ClientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Account.Types.CLIENT
        return super().save(*args, **kwargs)
