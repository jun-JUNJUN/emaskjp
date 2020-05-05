from django import forms
from .models import Entity, Demand, Supplier, SupplierContact, Supply

# reference: https://qiita.com/kk-ster/items/4618dd0a499c2c405b47


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['entity_name', 'zip_code',
                  'prefecture', 'address1', 'address2']
        labels = {
            'entity_name': '医療機関名',
            'zip_code': '〒',
        }
        error_messages = {
            'entity_name': {
                'required': '医療機関名を入力してください',
                'min_length': '医療機関名を入力してください'
            },
            'prefecture': {
                'required': '都道府県は必須です',
                'min_length': '郵便番号7桁入力してください'
            },
        }
        widgets = {
            'zip_code':
                forms.TextInput(
                    attrs={'class': 'p-postal-code',
                           'placeholder': '記入例: 8900053'},
                ),
            'prefecture':
                forms.TextInput(
                    attrs={'class': 'p-region', 'placeholder': '記入例: 鹿児島県'},
                ),
            'address1':
                forms.TextInput(
                    attrs={'class': 'p-locality p-street-address p-extended-address',
                           'placeholder': '記入例: 鹿児島市中央町５'},
                ),
            'address2':
                forms.TextInput(
                    attrs={'class': '', 'placeholder': '記入例: 千代田ビル'},
                ),
        }


class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = '__all__'
        max_digits = {
            'demand_qty': 6,
        }
        labels = {
            'begin_date': '月',
            'begin_date_display': '年/月',
            'demand_qty': '足りない数',
        }
        error_messages = {
            'demand_qty': {
                'required': '足りない数を入力するか、「0」(=足りている)を入力してください',
                'min_value': '-(マイナス)の数を入力しないでください'
            }
        }
        widgets = {
            'demand_qty':
                forms.NumberInput(
                    attrs={
                        'class': 'p-demand-qty',
                        'placeholder': '記入例: 100',
                    }
                ),
        }


# reference: https://github.com/naritotakizawa/django-inlineformset-sample/blob/master/app/forms.py
DemandFormSet = forms.modelformset_factory(
    Demand,
    form=DemandForm,
    max_num=3,
)


class DemandFormSet3(forms.Form):
    demand0_date = forms.DateField()
    demand1_date = forms.DateField()
    demand2_date = forms.DateField()
    demand0_qty = forms.DecimalField()
    demand1_qty = forms.DecimalField()
    demand2_qty = forms.DecimalField()
    demand0_date_display = forms.CharField()
    demand1_date_display = forms.CharField()
    demand2_date_display = forms.CharField()


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'zip_code',
                  'prefecture', 'address1', 'address2']
        labels = {
            'name': '送付者のお名前',
            'zip_code': '〒',
            'address1': '市区町村番地',
            'address2': 'マンション名、号室',
        }
        widgets = {
            'zip_code':
                forms.TextInput(
                    attrs={'class': 'p-postal-code',
                           'placeholder': '記入例: 8900053'},
                ),
            'prefecture':
                forms.TextInput(
                    attrs={'class': 'p-region', 'placeholder': '記入例: 鹿児島県'},
                ),
            'address1':
                forms.TextInput(
                    attrs={'class': 'p-locality p-street-address p-extended-address',
                           'placeholder': '記入例: 鹿児島市中央町５'},
                ),
            'address2':
                forms.TextInput(
                    attrs={'class': '', 'placeholder': '記入例: 千代田ビル'},
                ),
        }


class SupplierContactForm(forms.ModelForm):
    class Meta:
        model = SupplierContact
        exclude = ['supplier']


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        exclude = [
            'destination_entity', 'supplier'
        ]
