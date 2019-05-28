from django.urls import path
from status.api.views import *
from status.views import *

urlpatterns = [
    # path('',StatusListSearchAPIView.as_view()),  # /api/status/
    path('',StatusAPIView.as_view()),

    # path('create/',StatusCreateAPIView.as_view()),  # /api/status/create/
    # path('<int:pk>/',StatusDetailAPIView.as_view()), # /api/status/3/
    # path('<int:pk>-tog/',StatusDetail2APIView.as_view())
    # path('<int:pk>/update/',StatusUpdateAPIView.as_view()), # /api/status/3/update/
    # path('<int:pk>/delete/',StatusDeleteAPIView.as_view()), # /api/status/3/delete/
]


# /api/status --> List --> CRUD including List and search

# /api/status/4 --> Detail --> CRUD
