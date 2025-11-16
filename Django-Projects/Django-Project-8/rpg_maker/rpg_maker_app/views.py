from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Character, Attribute, InventoryItem
from .forms import CharacterForm, AttributeForm, InventoryItemForm, AttributeFormSet, InventoryItemFormSet
from .filters import CharacterFilterSet, AttributeFilterSet, InventoryItemFilterSet
from .serializers import CharacterModelSerializer, CharacterWriteSerializer, AttributeModelSerializer, AttributeWriteSerializer, InventoryItemModelSerializer, InventoryItemWriteSerializer
from rest_framework.exceptions import NotFound
from django.http import Http404

# Create your views here.
class CharacterListView(ListView):
    model = Character
    template_name = 'character/list.html'
    context_object_name = 'character_list'
    paginate_by = 10

    def get_queryset(self):
        self.filterset = CharacterFilterSet(self.request.GET, queryset=super().get_queryset())
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'character/detail.html'
    context_object_name = 'character_detail'


class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'character/form.html'
    success_url = reverse_lazy('character_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['attribute_form'] = AttributeFormSet(self.request.POST)
            context['inventory_form'] = InventoryItemFormSet(self.request.POST)
        else:
            context['attribute_form'] = AttributeFormSet()
            context['inventory_form'] = InventoryItemFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        attribute_form = context['attribute_form']
        inventory_form = context['inventory_form']

        if attribute_form.is_valid() and inventory_form.is_valid():
            self.object = form.save()
            attribute_form.instance = self.object
            attribute_form.save()
            inventory_form.instance = self.object
            inventory_form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class CharacterUpdateView(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'character/form.html'

    def get_success_url(self):
        return reverse('character_detail', kwargs = {'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['attribute_form'] = AttributeFormSet(self.request.POST)
            context['inventory_form'] = InventoryItemFormSet(self.request.POST)
        else:
            context['attribute_form'] = AttributeFormSet()
            context['inventory_form'] = InventoryItemFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        attribute_form = context['attribute_form']
        inventory_form = context['inventory_form']

        if attribute_form.is_valid() and inventory_form.is_valid():
            self.object = form.save()
            attribute_form.instance = self.object
            attribute_form.save()
            inventory_form.instance = self.object
            inventory_form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class CharacterDeleteView(DeleteView):
    model = Character
    template_name = 'character/delete_confirm.html'
    success_url = reverse_lazy('character_list')


class CharacterListApiView(APIView):
    def get(self, request):
        try:
            characters = Character.objects.all()
            serializer = CharacterModelSerializer(characters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e)


    def post(self, request):
        try:
            serializer = CharacterWriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CharacterDetailApiView(APIView):
    def get(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterModelSerializer(character)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Character.DoesNotExist:
            raise NotFound('Персонаж не найден')
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterWriteSerializer(character, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterWriteSerializer(character, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
            character.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AttributeListView(ListView):
    model = Attribute
    template_name = 'attribute/list.html'
    context_object_name = 'attribute_list'
    paginate_by = 10

    def get_queryset(self):
        self.filterset = AttributeFilterSet(self.request.GET, queryset=super().get_queryset())
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class AttributeDetailView(DetailView):
    model = Attribute
    template_name = 'attribute/detail.html'
    context_object_name = 'attribute_detail'


class AttributeCreateView(CreateView):
    model = Attribute
    form_class = AttributeForm
    template_name = 'attribute/form.html'
    success_url = reverse_lazy('attribute_list')


class AttributeUpdateView(UpdateView):
    model = Attribute
    form_class = AttributeForm
    template_name = 'attribute/form.html'

    def get_success_url(self):
        return reverse('attribute_detail', kwargs = {'pk': self.object.pk})


class AttributeDeleteView(DeleteView):
    model = Attribute
    template_name = 'attribute/delete_confirm.html'
    success_url = reverse_lazy('attribute_list')


class AttributeListApiView(APIView):
    def get(self, request):
        try:
            attribute = Attribute.objects.all()
            serializer = AttributeModelSerializer(attribute, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e)


    def post(self, request):
        try:
            serializer = AttributeWriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AttributeDetailApiView(APIView):
    def get(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
            serializer = AttributeModelSerializer(attribute)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Character.DoesNotExist:
            raise NotFound('Аттрибут не найден')
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
            serializer = AttributeWriteSerializer(attribute, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
            serializer = AttributeWriteSerializer(attribute, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
            attribute.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class InventoryItemListView(ListView):
    model = InventoryItem
    template_name = 'inventory_item/list.html'
    context_object_name = 'inventory_item_list'
    paginate_by = 30

    def get_queryset(self):
        self.filterset = InventoryItemFilterSet(self.request.GET, queryset=super().get_queryset())
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class InventoryItemDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventory_item/detail.html'
    context_object_name = 'inventory_item_detail'


class InventoryItemCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory_item/form.html'
    success_url = reverse_lazy('inventory_item_list')


class InventoryItemUpdateView(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory_item/form.html'

    def get_success_url(self):
        return reverse('inventory_item_detail', kwargs = {'pk': self.object.pk})


class InventoryItemDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory_item/delete_confirm.html'
    success_url = reverse_lazy('inventory_item_list')


class InventoryItemListApiView(APIView):
    def get(self, request):
        try:
            inventory_item = InventoryItem.objects.all()
            serializer = InventoryItemModelSerializer(inventory_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e)


    def post(self, request):
        try:
            serializer = InventoryItemWriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class InventoryItemDetailApiView(APIView):
    def get(self, request, pk):
        try:
            inventory_item = InventoryItem.objects.get(pk=pk)
            serializer = InventoryItemModelSerializer(inventory_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Character.DoesNotExist:
            raise NotFound('Объект не найден')
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk):
        try:
            inventory_item = InventoryItem.objects.get(pk=pk)
            serializer = InventoryItemWriteSerializer(inventory_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            inventory_item = InventoryItem.objects.get(pk=pk)
            serializer = InventoryItemWriteSerializer(inventory_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            inventory_item = InventoryItem.objects.get(pk=pk)
            inventory_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

