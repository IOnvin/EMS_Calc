from django import forms
from .models import QuoteInputModel, Location


class QuoteInputForm(forms.ModelForm):
    class Meta:
        model = QuoteInputModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].querset = Location.objects.none()

        if 'hostingProvider' in self.data:
            try:
                hostingProvider_id = int(self.data.get('hostingProvider'))
                self.fields['location'].queryset = Location.objects.filter(hostingProvider_id=hostingProvider_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['location'].queryset = self.instance.hostingProvider.location_set.order_by('name')


'''class HostingForm(forms.ModelForm):
    class Meta:
        model = HostingModel
        fields = '__all__'
        '''

