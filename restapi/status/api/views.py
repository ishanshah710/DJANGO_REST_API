import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins

from status.api.serializers import StatusSerializer
from status.models import Status
from django.shortcuts import get_object_or_404

# method for taking valid json data
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


# one endpoint for all CRUDL
class StatusAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView):
    permission_classes       =   []
    authentication_classes   =   []
    serializer_class = StatusSerializer
    passed_pk = None

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request

        # getting pk bcoz we have to do all CRUDL on api/status/ only and we are not passing pk there
        passed_pk = request.GET.get('pk' , None) or self.passed_pk
        queyset = self.get_queryset()

        obj = None
        if passed_pk is not None:
            obj = get_object_or_404(queyset , pk=passed_pk)
            self.check_object_permissions(request , obj)  # bulit in method of rest_framework
        return obj

    def get(self , request , *args ,**kwargs):
        url_passed_pk = request.GET.get('pk' , None)

        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(body_)

        new_passed_pk = json_data.get('pk',None)


        # print(request.body)
        # print(request.data)

        passed_pk = url_passed_pk or new_passed_pk or None
        self.passed_pk = passed_pk
        if passed_pk is not None:
            return self.retrieve(request , *args , **kwargs)
        return super().get(request , *args , **kwargs)

    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)

    def put(self , request , *args , **kwargs):
        url_passed_pk = request.GET.get('pk' , None)

        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(body_)

        new_passed_pk = json_data.get('pk',None)

        passed_pk = url_passed_pk or new_passed_pk or None
        self.passed_pk = passed_pk
        return self.update(request , *args , **kwargs)

    def patch(self , request , *args , **kwargs):
        url_passed_pk = request.GET.get('pk' , None)

        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(body_)

        new_passed_pk = json_data.get('pk',None)

        passed_pk = url_passed_pk or new_passed_pk or None
        self.passed_pk = passed_pk
        return self.update(request , *args , **kwargs)

    def delete(self , request , *args , **kwargs):
        url_passed_pk = request.GET.get('pk' , None)

        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(body_)

        new_passed_pk = json_data.get('pk',None)

        passed_pk = url_passed_pk or new_passed_pk or None
        self.passed_pk = passed_pk
        return self.destroy(request , *args , **kwargs)



class StatusListSearchAPIView(APIView):
    permission_classes       =   []
    authentication_classes   =   []

    def get(self , request , format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs , many=True)
        return Response(serializer.data)


# class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
#     permission_classes       =   []
#     authentication_classes   =   []
#     # queryset = Status.objects.all() -->commented this bcoz now we have defined get_queryset method below!
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

    #  It is very similar to django views like following!
    #  It is not for coding just for showing that seraializrers are very similar to forms
    # class StatusCreateView(CreateView):
    #     queryset = Status.objects.all()
    #     form_class = StatusForm

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes       =   []
    authentication_classes   =   []
    queryset = Status.objects.all()
    #-->we havent defined method get_queryset bcoz here we used queryset attribute instead

    serializer_class = StatusSerializer

    # def perform_create(self , serializer):
    #     serializer.save(user=self.request.user)


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes       =   []
    authentication_classes   =   []
    queryset = Status.objects.all()
    #-->we havent defined method get_queryset bcoz here we used queryset attribute instead

    serializer_class = StatusSerializer




class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes       =   []
    authentication_classes   =   []
    queryset = Status.objects.all()
    #-->we havent defined method get_queryset bcoz here we used queryset attribute instead

    serializer_class = StatusSerializer

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes       =   []
    authentication_classes   =   []
    queryset = Status.objects.all()
    #-->we havent defined method get_queryset bcoz here we used queryset attribute instead

    serializer_class = StatusSerializer




# we r using mixins for more efficiency

# CreateModelMixin --> post method
# class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
#     permission_classes       =   []
#     authentication_classes   =   []
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self , request , *args , **kwargs):
#         return self.create(request , *args , **kwargs)


# UpdateModelMixin :- put method
# DestroyModelMixin :- delete method

class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin ,generics.RetrieveAPIView):
    permission_classes       =   []
    authentication_classes   =   []
    queryset = Status.objects.all()
    #-->we havent defined method get_queryset bcoz here we used queryset attribute instead

    serializer_class = StatusSerializer

    def put(self , request , *args , **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self , request , *args , **kwargs):
        return self.destroy(request , *args , **kwargs)

    def patch(self , request , *args , **kwargs):
        return self.update(request, *args, **kwargs)


# following is equlivalent to whole above StatusDetailAPIView
class StatusDetail2APIView(generics.RetrieveUpdateDestroyAPIView): # Given -tog path in urls
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
