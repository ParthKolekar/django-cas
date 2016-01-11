========
Usage
========

You can now use the `django_cas.views.login` and 
`django-cas.views.logout` to do login and logouts by overriding
the default Django authentcation url endpoint.

Since there are no models, there is no real need of 
putting it in your `INSTALLED_APPS`.

Give the `CAS_SERVER_URL` in your settings.py

Add the Authentication Backend as 

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'django_cas.backends.CASBackend'
    )

Add the login middleware to intercept all login views with 
django-cas login views.

    MIDDLEWARE_CLASS = (
        ...
        'django_cas.middleware.CASMiddleware',
        ...
    )

Be sure that AuthenticationMiddleware is installed prior to this middleware.

Set your urls in your urls.py to where you want your django-cas
login endpoints. 

     url(r'^accounts/login' , 'django_cas.views.login', name='login_url'),
     url(r'^accounts/logout' , 'django_cas.views.logout', name='logout_url'),


Alternatively, in Django 1.7.4, you can set the `LOGIN_URL` and `LOGOUT_URL`
to set the Django endpoints exactly where your django-cas endpoints are so that
all authentication is done by django-cas.


Populated Views Backend
-----------------------

For wrapping about on your login flow, create a PopulatedCASBackend, 
and override the django_cas.backends.CASBackend with your own.

    from django_cas.backends import CASBackend

    class PopulatedCASBackend(CASBackend):
    """
        CAS authentication with user data populated for custom
        authentication.
    """

    def authenticate(self, ticket, service):
        """
            Authenticates CAS ticket and retrieves 
            user data.
        """

        user = super(PopulatedCASBackend, self).authenticate(ticket, service)
        attributes = request.session.get('attr')

        do_something_with_attributes()

        return user
