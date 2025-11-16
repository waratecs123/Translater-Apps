from django import forms
from .models import Character, Attribute, InventoryItem
from django.forms import inlineformset_factory


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'character_class', 'level', 'backstory', 'skill', 'spell']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'race': forms.Select(attrs={'class': 'form-control'}),
            'character_class': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите уровень (0-1000)'}),
            'backstory': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите историю'}),
            'skill': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'spell': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
        }
        labels = {
            'name': 'Имя',
            'race': 'Раса',
            'character_class': 'Класс',
            'level': 'Уровень',
            'backstory': 'История',
            'skill': 'Умение',
            'spell': 'Заклинание',
        }


class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        widgets = {
            'strength': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите силу (0-1000)'}),
            'dexterity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите ловкость (0-1000)'}),
            'constitution': forms.Select(attrs={'class': 'form-control'}),
            'intelligence': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите интеллект (0-1000)'}),
            'wisdom': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите мудрость (0-1000)'}),
            "charisma": forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите харизму (0-1000)'})
        }
        labels = {
            'strength': 'Сила',
            'dexterity': 'Ловкость',
            'constitution': 'Телосложение',
            'intelligence': 'Интеллект',
            'wisdom': 'Мудрость',
            'charisma': 'Харизма',
        }


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['item', 'quantity', 'is_equipped']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000, 'placeholder': 'Введите количество (0-1000)'}),
            'is_equipped': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
        labels = {
            'item': 'Предмет',
            'quantity': 'Количество',
            'is_equipped': 'Одет',
        }

AttributeFormSet = inlineformset_factory(
    Character,
    Attribute,
    form=AttributeForm,
    extra=1,
    can_delete=False
)

InventoryItemFormSet = inlineformset_factory(
    Character,
    InventoryItem,
    form=InventoryItemForm,
    extra=1,
    can_delete=True
)