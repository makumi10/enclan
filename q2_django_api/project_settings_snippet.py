# Not a full settings.py - just the bits to add after
# `django-admin startproject project .`

# 1. add these to INSTALLED_APPS
#    "rest_framework",
#    "rest_framework.authtoken",
#    "blog_api",

# 2. tell DRF how to authenticate people
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "rest_framework.authentication.TokenAuthentication",
#         "rest_framework.authentication.SessionAuthentication",
#     ],
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAuthenticatedOrReadOnly",
#     ],
# }

# 3. in the project's urls.py
# from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/", include("blog_api.urls")),
#     path("api/auth-token/", obtain_auth_token),
# ]

# to use it: POST username/password to /api/auth-token/ to get a token,
# then send it as "Authorization: Token <token>" on requests
