from rest_framework import serializers
from .models import Hostel_Entry


class Hostel_Entry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Entry
        fields = ['id', 'Number', 'Entered_boy_girl_name', 'Entered_boy_girl_roll_no', 'Host_boy_girl_name', 'Host_boy_girl_roll_no', 'Room_no', 'Date', 'Entry', 'Exit']    

class Enter_into_Hostel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Entry
        fields = ['Number', 'Entered_boy_girl_name', 'Entered_boy_girl_roll_no', 'Host_boy_girl_name', 'Host_boy_girl_roll_no', 'Room_no', 'Date', 'Entry']    

class Exit_from_Hostel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Entry
        fields = ['Number', 'Entered_boy_girl_roll_no', 'Host_boy_girl_roll_no', 'Date', 'Entry', 'Exit']

class Not_exited_serializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Entry
        fields = ['id', 'Number', 'Entered_boy_girl_name', 'Entered_boy_girl_roll_no', 'Host_boy_girl_name', 'Host_boy_girl_roll_no', 'Room_no', 'Date', 'Entry']

