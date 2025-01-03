from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        # Optionally log or print the model name
        print(f"{model.__name__} is already registered.")
