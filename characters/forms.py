from django import forms
from .models import Character, Location

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'status': 'Status',
            'species': 'Espécie',
            'type': 'Tipo',
            'gender': 'Gênero',
            'origin_name': 'Nome de Origem',
            'location_name': 'Nome do Local',
            'image': 'Imagem',
            'api_id': 'ID da API',
            'location': 'Localização',
            'dimension': 'Dimensão',
            'residents_count': 'Número de Residentes',
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'api_id', 'residents_count'] 
        labels = {
            'name': 'Nome',
            'api_id': 'ID da API',
            'residents_count': 'Número de Residentes',
        }