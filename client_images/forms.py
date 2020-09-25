from django.forms import ModelForm

from .models import ClientImage


class ClientImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientImageForm, self).__init__(*args, **kwargs)

        fieldsMap = {
            "front": "عکس از جلو",
            "side": "عکس از کنار",
            "back": "عکس از پشت",
        }
        # Assigning class and placeholder and removeing label from fields
        for k, v in self.fields.items():
            self.fields[k].label = fieldsMap[k]
            v.widget.attrs['class'] = 'input'

    class Meta:
        model = ClientImage
        fields = "__all__"
