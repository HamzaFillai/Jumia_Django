from rest_framework import serializers
from tutorials.models import Profil
from tutorials.models import Cluster


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('id',
                  'nom',
                  'prenom',
                  'age',
                  'email',
                  'password')

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = ('id',
                  'idUser',
                  'idProduct',
                  'date',
                  'classe')