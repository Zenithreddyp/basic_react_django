from django.contrib.auth.models import User
from rest_framework import serializers #compulsory becoz of serilizer 
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
        extra_kwargs={"password":{"write_only":True}}#means it can only be writen cannt be read 
#“Don’t let the user send the author… I (the backend) will decide who the author is.”

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id","title","content","created_at","author"]
        extra_kwargs={"author":{"read_only":True}}
    
