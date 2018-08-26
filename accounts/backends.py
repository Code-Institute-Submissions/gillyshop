from django.contrib.auth.models import User


class CaseInsensitiveAuth:
    """
    Authenticate a of User by using a case-insensitive query to check a
    combination of the supplied email/username and password.
    To avoid the risk of having two users with similar usernames,
    distinguished only by letter case (e.g. 'john' and 'John'), consider
    updating your User model to save usernames as lower case entries to
    the database.
    This will ensure all usernames have unique spellings, and as a result,
    our case insensitive query will return a single result only.
    """

# class EmailAuth:
#     """authenticate a user by an exact match on the email and password"""
    
    def authenticate(self, username=None, password=None):
        """get an instance of user based off the email and verified password"""
        
        
        try:
            user = User.objects.get(email=username)
            
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """used bu the django authentication system to retrive a user instance"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
            
        except User.DoesNotExist:
            return None