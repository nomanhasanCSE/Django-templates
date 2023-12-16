from django import forms

class contactForm(forms.Form):
        name = forms.CharField(label="Full Name:", initial ='Noman', disabled= True, help_text ="total length must be within 70 characters", required =False, widget =forms.Textarea(attrs={'id':'text_area', 'class': 'class1 class2', 'placeholder' :'EnterYour name'}))
        file = forms.FileField()
        # email = forms.EmailField(label="User Email")
        #Age = forms.IntegerField()
        Age = forms.CharField(widget = forms.NumberInput)
        # Weight = forms.FloatField()
        # Balance = forms.DecimalField()
        # Cheack = forms.BooleanField()
        # Birthday = forms.DateField()
        Birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
        # Appointment = forms.DateTimeField()
        Appontment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
        
        CHOICES=[('S','Small'), ('M','Medium'),('L', 'Large')]
        # Size = forms.ChoiceField(choices=CHOICES)
        Size = forms.ChoiceField(choices=CHOICES,widget= forms.RadioSelect)
        MEAL=[('P','Pepperoni'), ('M','Mashroom'),('B', 'Beef')]
        # Pizza= forms.MultipleChoiceField(choices= MEAL)
        Pizza= forms.MultipleChoiceField(choices= MEAL,widget= forms.CheckboxSelectMultiple)