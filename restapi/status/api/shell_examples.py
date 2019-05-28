from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

'''
Serialize a single object
'''

# obj = Status.objects.first()
# serializer = StatusSerializer(obj)
# serializer.data
# json_data = JSONRenderer().render(serializer.data)
# print(json_data)
#
# stream = BytesIO(json_data)
# data = JSONParser().parse(stream)
# print(data)
#

# '''
# Serialize a queryset
# '''
#
# qs = Status.objects.all()
# serializer2 = StatusSerializer(qs , many=True)
# serializer2.data
# json_data2 = JSONRenderer().render(serializer2.data)
# print(json_data2)
#
# stream2 = BytesIO(json_data2)
# data2 = JSONParser().parse(stream2)
# print(data2)
#
#
# '''
# create obj
# '''
#
# data = {'user' : 1}
# serializer = StatusSerializer(data = data)
# serializer.is_valid()
# serializer.save()
#
# # if serializer.is_valid(): # can also do this
# #     serializer.save()
#
# '''
# Update obj
# '''
# obj = Status.objects.first()
# data = {'content' : 'some new content' , 'user' : 1}
# update_serializer = StatusSerializer(obj , data=data)
# update_serializer.is_valid()
# # update_serializer.save()
#
#
#
# '''
# Delete obj
# '''
# data = {'user':1,'content':'delete it!'}
# create_obj_serializer = StatusSerializer(data=data)
# create_obj_serializer.is_valid()
# create_obj = create_obj_serializer.save() # instance of the object
# # print(create_obj)
#
#
# # we r just deleting last object
#
# obj = Status.objects.last()
# get_data_serializer = StatusSerializer(obj)
#
# print(get_data_serializer.data)
#
# # print(obj.delete())
#



# we can also use serializers like following!

# from rest_framework import serializers
# class CustomSerializers(serializers.Serializer): # we can also do this like in models
#     content  = serializers.CharField()
#     email = serializers.EmailField()
#
#
# data = {'email':'hello@gmail.com' , 'content':'using serializer'}
# create_obj_serializer = CustomSerializers(data=data)
# if create_obj_serializer.is_valid():
#     valid_data = create_obj_serializer.data
#     print(valid_data)
