from rest_framework import serializers
from players_db.models import Team,Player
import random
from batting_ipl import Battingipl 
from batting_odi import Battingodi
from batting_test import Battingtest
from batting_ttwenty import Battingttwenty
from bowling_ipl import Bowlingipl 
from bowling_odi import Bowlingodi
from bowling_test import Bowlingtest
from bowling_ttwenty import Bowlingttwenty

from random import randint
import json
import time
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('pk','created','profile_id','name','dob','country','height','role','birthplace','url','about','bowling_style','batting_style')
class BattingiplSerializer(serializers.ModelSerializer):
    class Meta:
        model=Battingipl
        fields=('pk','matches','innings','pname','runs','balls','highest','average','sr','not_out','fours','sixes','ducks','fiftys','hundreds','twohundreds','threehundreds','fourhundreds')
class BattingodiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Battingodi
        fields=('pk','matches','innings','pname','runs','balls','highest','average','sr','not_out','fours','sixes','ducks','fiftys','hundreds','twohundreds','threehundreds','fourhundreds')
class BattingtestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Battingtest
        fields=('pk','matches','innings','pname','runs','balls','highest','average','sr','not_out','fours','sixes','ducks','fiftys','hundreds','twohundreds','threehundreds','fourhundreds')
class BattingttwentySerializer(serializers.ModelSerializer):
    class Meta:
        model=Battingttwenty
        fields=('pk','matches','innings','pname','runs','balls','highest','average','sr','not_out','fours','sixes','ducks','fiftys','hundreds','twohundreds','threehundreds','fourhundreds')
class BowlingiplSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bowlingipl
        fields=('pk','matches','pname','innings','runs','balls','maidens','average','eco','wickets','sr','bbi','bbm','four_w','five_w','ten_w')
class BowlingodiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bowlingodi
        fields=('pk','matches','pname','innings','runs','balls','maidens','average','eco','wickets','sr','bbi','bbm','four_w','five_w','ten_w')
class BowlingtestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bowlingtest
        fields=('pk','matches','pname','innings','runs','balls','maidens','average','eco','wickets','sr','bbi','bbm','four_w','five_w','ten_w')
class BowlingttwentySerializer(serializers.ModelSerializer):
    class Meta:
        model=Bowlingttwenty
        fields=('pk','matches','pname','innings','runs','balls','maidens','average','eco','wickets','sr','bbi','bbm','four_w','five_w','ten_w')
# class PlayerListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Player
#         fields = ('tname','ttype','teamplayers')

#     def create(self, validated_data):
#       teamplayers = validated_data.pop('teamplayers')
#       instance = Team.objects.create(**validated_data)
#       for teamplayer in teamplayers:
#         instance.teamplayers.add(teamplayer)
#       return instance
class PlayerListSerializer(serializers.ModelSerializer):
    pname = PlayerSerializer(many=True)
    class Meta:
        model = Player
        fields = ('tname','ttype','teamplayers')