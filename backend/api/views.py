from django.shortcuts import render           # Used for HTML templates (not needed if you're doing an API-only project)
from django.contrib.auth.models import User   #	Imports Django’s built-in User model
from rest_framework import generics           # Gives you shortcut class-based views like CreateAPIView, ListAPIView, etc.
from .serializers import UserSerializer,NoteSerializer       # The serializer you created — handles JSON <→ User conversion
from rest_framework.permissions import IsAuthenticated,AllowAny   #	These control who can access the view (authentication permissions)
from .models import Note

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)#actually serilizer.save() is enought but in serilizers we used extra_kwargs = {"author": {"read_only": True}}   So the client cannot set the author (which is a security best practice). This ensures the Note is linked to whoever is logged in. 
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    # queryset = Note.objects.all()
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    



class CreateUserView(generics.CreateAPIView):#registration form for user to login
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]










# | View Class          | What It Does                                 | HTTP Methods  |
# | ------------------- | -------------------------------------------- | ------------- |
# | `CreateAPIView`     | Handles **creating** objects                 | `POST` only   |
# | `ListCreateAPIView` | Handles **listing** and **creating** objects | `GET`, `POST` |
# | `DestroyAPIView`    | Handles **deleting** objects                 | `DELETE` only |
