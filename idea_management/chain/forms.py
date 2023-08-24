from django import forms
from django.forms import formset_factory
from accounts.models import User


class EditChainForm(forms.Form):

    @staticmethod
    def get_managers():
        manager_choices = list()
        managers = User.objects.filter(is_manager=True)

        for manager in managers:
            manager_choices.append((manager.id, f'{manager.first_name} {manager.last_name}'))
        
        return manager_choices
    
    chain_link = forms.ChoiceField(
        label='',
        choices=get_managers(),
        widget=forms.Select(
            attrs={
                'class': 'btn btn-secondary dropdown-toggle',
                'aria-labelledby': 'dropdownMenuButton'
            }
        )
    )


class ParentEditChainForm(forms.Form):
        
    chain_links = formset_factory(EditChainForm, extra=3)
