from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter
from django.forms.widgets import DateInput
from .models import Post, Category
from django.forms import CheckboxSelectMultiple



class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label = 'Category',
        widget = CheckboxSelectMultiple()
    )

    creation_time = DateFilter(
        field_name='creation_time',
        widget=DateInput(
            attrs={'type': 'date'}
        ),
        lookup_expr='date',
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }