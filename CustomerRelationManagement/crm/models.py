from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MyUserManager(BaseUserManager):
    # ['designation','first_name','last_name','phone','address1','address2','city','state','pin',
    #                        'department']
    def create_user(self, email, designation,first_name,last_name,phone,address1,address2,city,state,pin, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            designation=designation,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            pin=pin
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Department(models.Model):
    dept_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.dept_name

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    designation=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address1=models.CharField(max_length=120)
    address2=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    options=(("kerala","kerala"),
             ("ThamilNadu", "ThamilNadu"),
             ("Mumbai","Mumbai"),
             ("Delhi","Delhi"),
             ("pune","pune")

             )
    state=models.CharField(max_length=120,choices=options,default="Mumabi")
    pin=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['designation','first_name','last_name','phone','address1','address2','city','state','pin',
                       'department']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
