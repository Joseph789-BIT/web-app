from django.forms import widgets


class CustomPictureImageFieldWidget(widgets.FileInput):


    def render(self, name, value, attrs= None, **kwargs):
        default_html = super().render(name, value, attrs, **kwargs)