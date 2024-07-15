from django import forms
from .models import Car, Part

class CarSelectForm(forms.Form):
    make = forms.ChoiceField(choices=[])
    year = forms.ChoiceField(choices=[])
    model = forms.ChoiceField(choices=[])
    engine = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        makes = Car.objects.values_list('make', flat=True).distinct().order_by('make')
        self.fields['make'].choices = [('', 'Select Make')] + [(make, make) for make in makes]
        # Populate year choices
        years = Car.objects.values_list('year', flat=True).distinct().order_by('-year')# descending order
        self.fields['year'].choices = [('', 'Select Year')] + [(str(year), str(year)) for year in years]
        # Populate model choices
        models = Car.objects.values_list('model', flat=True).distinct().order_by('model')
        self.fields['model'].choices = [('', 'Select Model')] + [(model, model) for model in models]  
        # Populate engine choices   
        engines = Car.objects.values_list('engine', flat=True).distinct().order_by('engine')
        self.fields['engine'].choices = [('', 'Select Engine')] + [(engine, engine) for engine in engines]

class PartSelectForm(forms.Form):
    name = forms.ChoiceField(choices=[])
    description = forms.ChoiceField(choices=[])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate name choices
        names = Part.objects.values_list('name', flat=True).distinct().order_by('name')
        self.fields['name'].choices = [('', 'Select Part Name')] + [(name, name) for name in names]
        # Populate description choices
        descriptions = Part.objects.values_list('description', flat=True).distinct().order_by('description')
        self.fields['description'].choices = [('', 'Select Description')] + [(desc, desc) for desc in descriptions]