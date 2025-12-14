from django.forms.widgets import NumberInput
from django.utils.translation import gettext_lazy as _

class MarkInput(NumberInput):
    input_type = "number"

    def __init__(self, *args, **kwargs):
        attrs = kwargs.get("attrs", {})
        attrs.setdefault("min", 1)
        attrs.setdefault("max", 10)
        attrs.setdefault("placeholder", _("Ungraded"))
        super().__init__(attrs=attrs)
