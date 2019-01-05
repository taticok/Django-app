from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='タイトル', lookup_expr='contains')

    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('start_date', 'start_date'),
            ('end_date', 'end_date'),
        ),
        field_labels={
            'name': '氏名',
            'start_date': '開始日',
            'end_date': '終了日',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('name','start_date','end_date','memo')
