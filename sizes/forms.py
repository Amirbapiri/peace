from django.forms import ModelForm

from .models import Size


class SizesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SizesForm, self).__init__(*args, **kwargs)
        fieldsMap = {
            "height": "قد",
            "weight": "وزن",
            "neck": "گردن",
            "chest": "سینه",
            "arm": "بازو",
            "wrist": "مچ",
            "waist": "کمر",
            "hamstring": "ران",
            "calf": "ساق",
        }

        for k, v in self.fields.items():
            self.fields[k].label = ""
            v.widget.attrs['class'] = "input mb-2"
            if k in fieldsMap:
                v.widget.attrs['placeholder'] = fieldsMap[k]

    class Meta:
        model = Size
        fields = ["height", "weight", "neck", "chest", "arm", "wrist",
                  "waist", "hamstring", "calf"]
