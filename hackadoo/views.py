from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from django.shortcuts import render


from hackadoo.serializers import EmailJWTSerializer

def home(request):

    context = {
        'page_title': "The Time Traveler's Gazette",
    }

    if settings.DEBUG:
        return render(request, 'index_debug.html', context=context)
    return render(request, 'index.html', context=context)



class JWTFromEmailObtainPairView(jwt_views.TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = EmailJWTSerializer
