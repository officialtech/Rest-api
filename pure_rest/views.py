
from . models import Book
from .serializers import BookSerializer
# from django.http import HttpResponse
# from django.views.generic import View
# import io
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from .models import Book, Author, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class PublisherView(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]











# @method_decorator(csrf_exempt, name="dispatch")
# class BookApiView(View):

#     def get(self, request, *args, **kwargs):
#         data = request.body
#         if len(data) != 0:
#             '''Means have something'''
#             stream = io.BytesIO(data)
#             pdata = JSONParser().parse(stream)
#             gid = pdata.get('gid', None)
#             if gid is not None:
#                 db_data = Book.objects.get(id=gid)
#                 if db_data is None:
#                     json_data = JSONRenderer().render({"message": "Invalid ID"})
#                     HttpResponse(json_data, content_type="application/json", status=404)
#                 book = BookSerializer(db_data)
#                 json_data = JSONRenderer().render(book.data)
#                 return HttpResponse(json_data, content_type="application/json", status=200)

#         qs = Book.objects.all()
#         all_books = BookSerializer(qs, many=True)
#         print(".>>>>>>", all_books.data)
#         json_data = JSONRenderer().render(all_books.data)
#         return HttpResponse(json_data, content_type="application/json")
    


#     def post(self, request, *args, **kwargs):
#         data = request.body
#         stream = io.BytesIO(data)
#         pdata = JSONParser().parse(stream)
#         serializer = BookSerializer(data=pdata)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(serializer, content_type="application/json", status=200)
        
#         return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application/json", status=404)


#     def put(self, request, *args, **kwargs):
#         data = request.body
#         stream = io.BytesIO(data)
#         pdata = JSONParser().parse(stream)
#         if pdata.get('gid', None) is None:
#             json_data = JSONRenderer().render({'message': 'ID is required to update.'})
#             return HttpResponse(json_data, content_type="application/json")

#         serializer = BookSerializer(data=pdata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             json_data = JSONRenderer().render({'message': 'Updated successfully'})
#             return HttpResponse(json_data, 'application/json')

#         return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application/json", status=404)


#     def delete(self, request):
#         data = request.body
#         stream = io.BytesIO(data)
#         pdata = JSONParser().parse(stream)
#         gid = pdata.get('gid', None)
#         if gid is None:
#             json_data = JSONRenderer().render({'message': 'ID is required to delete.'})
#             return HttpResponse(json_data, content_type="application/json")
#         book = Book.objects.get(id=gid)
#         if book is None:
#             json_data = JSONRenderer().render({'message': 'Book not available with this ID'})
#             return HttpResponse(json_data, content_type="application/json")
#         status, deleted_item = book.delete()
#         if status == 1:
#             json_data = JSONRenderer().render({'message': 'Book deleted successfully'})
#             return HttpResponse(json_data, content_type="application/json")

#         json_data = JSONRenderer().render(book.errors)
#         return HttpResponse(json_data, content_type="application/json", status=404)
