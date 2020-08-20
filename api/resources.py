from import_export import resources
from .models import AutoData


class AutoDataResource(resources.ModelResource):
    class Meta:
        model = AutoData