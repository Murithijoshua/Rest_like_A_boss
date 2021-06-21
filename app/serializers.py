from typing import SupportsRound
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source ='owner.username')
    owner_id = serializers.ReadOnlyField(source = 'owner.id')
    votes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title','url','created','owner', 'owner_id']
    def get_votes(self,post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote 
        fields = ['id ']