import asyncio

from asgiref.sync import async_to_sync
from rest_framework import serializers
from rest_framework import generics as api_views

from qna_demos.api.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodosListView(api_views.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # Variant 1, better in 99% of cases
    @async_to_sync
    async def get_queryset(self):
        queryset = super().get_queryset()

        count = await queryset.filter(is_done=True).acount()
        await asyncio.sleep(3)
        print(count)

        return queryset

    # Variant 2
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     count = async_to_sync(queryset.filter(is_done=True).acount())
    #     print(count)
    #
    #     return queryset
