from django.forms import widgets
from django.utils.safestring import mark_safe

class CustomPictureImageFieldWidget(widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        default_html = super().render(name, value, attrs, **kwargs)
        
        # Initialize empty image HTML
        img_html = ''
        
        # Only try to show image if value exists and has a URL
        if value and hasattr(value, 'url'):
            try:
                img_html = mark_safe(f'<img src="{value.url}" width="200" class="mb-3 rounded" /><br>')
            except ValueError:
                # Handle case where file doesn't exist
                pass
                
        # Return both the image preview and file input
        return mark_safe(f'{img_html}{default_html}')