from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class UserAccountManager(BaseUserManager):
    def create_user(self, username, groups_id, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(username=username, groups_id=groups_id, email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def _create_user(self, username, groups, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(username=username, groups=groups, email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_admin(self, username, groups_id, email, password=None):
        user = self.model(username=username, groups_id=groups_id, email=email)
        user.set_password(password)
        user.is_superuser = False
        user.first_name = username + "ali"
        user.last_name = username + "ov"
        user.is_admin = True
        user.is_staff = False
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, groups_id, email, password):
        user = self.create_user(username, groups_id, email, password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, username, groups, email, password):
        user = self._create_user(username, groups, email, password)
        user.save(using=self._db)
        return user

    def create_superadmin(self, username, email, password):
        group = Group.objects.filter(name="admin").first()
        if not group:
            group = Group()
            group.name = "admin"
            group.save()
        groups_id = group.id
        user = self.create_admin(username, groups_id, email, password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username_):
        return self.get(username=username_)
