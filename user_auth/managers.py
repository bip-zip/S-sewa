from django.contrib.auth.models import BaseUserManager 
class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, is_admin=False, is_staff=False, is_active=True, is_customer=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
     

        user = self.model(
            email=self.normalize_email(email)
        )
        user.phone = phone
        user.set_password(password)  # change password to hash
        user.is_customer = is_customer
        user.is_admin = is_admin
        user.is_staff = is_staff
        # user.is_active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
    
        user = self.model(
            email=self.normalize_email(email)
        )
       
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        # user.is_active = True
        user.save(using=self._db)
        return user