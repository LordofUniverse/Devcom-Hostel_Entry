from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Hostel_Entry
from .serializers import *

# Create your views here.


# Make a database

## Hostel name              -> Integer
## Entered boy or girl name -> String
## Host boy or girl name    -> String
## Host Room no             -> String
## Enter Date               -> Date
## Enter time               -> Integer
## Exit time                -> Integer


class Hostel_Entries(viewsets.ModelViewSet):
    serializer_class = Hostel_Entry_Serializer
    queryset = Hostel_Entry.objects.all()

class Enter_into_Hostel(APIView):
    # def get(self, request, format=None):
        # snippets = Hostel_Entry.objects.all()
        # serializer = Hostel_all_Serializer(snippets, many=True)
        # return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Enter_into_Hostel_Serializer(data=request.data)
        if serializer.is_valid():
            
            Number = serializer.data.get('Number')
            Entered_boy_girl_name = serializer.data.get('Entered_boy_girl_name')
            Entered_boy_girl_roll_no = serializer.data.get('Entered_boy_girl_roll_no')
            Host_boy_girl_name = serializer.data.get('Host_boy_girl_name')
            Host_boy_girl_roll_no = serializer.data.get('Host_boy_girl_roll_no')
            Room_no = serializer.data.get('Room_no')
            Date = serializer.data.get('Date')
            Entry = serializer.data.get('Entry')

            queryset = Hostel_Entry.objects.filter(Number = Number, Entered_boy_girl_roll_no = Entered_boy_girl_roll_no, Date = Date, Exit = 'not filled')
            queryset2 = Hostel_Entry.objects.filter(Number = Number, Host_boy_girl_roll_no = Host_boy_girl_roll_no, Date = Date, Exit = 'not filled')
            

            if queryset.exists() or queryset2.exists():

                # count1 = queryset.count()
                # count2 = queryset.count()
                # print("count: ", count1, count2)

                # if (count1 > 1){
                #     queryset_checkifexited = Hostel_Entry.objects.filter(Number = Number, Entered_boy_girl_roll_no = Entered_boy_girl_roll_no, Date = Date)
                # }

                # data = Hostel_Entry.objects.get(Number = Number, Entered_boy_girl_roll_no = Entered_boy_girl_roll_no, Date = Date)
                # print('hi')
                # print(data.Number)
                # print(data.Exit)
                # print('hi')

                if queryset.exists():
                    return Response({'msg': 'Boy/Girl whose roll no is to be filled is already entered for today'}, status=status.HTTP_226_IM_USED )
                else:
                    return Response({'msg': 'Host Boy/Girl whose roll no is to be filled is already entered for someone else today'}, status=status.HTTP_226_IM_USED )

                
            else:

                room = Hostel_Entry(Number = Number,  Entered_boy_girl_name = Entered_boy_girl_name, Entered_boy_girl_roll_no = Entered_boy_girl_roll_no, Host_boy_girl_name = Host_boy_girl_name, Host_boy_girl_roll_no = Host_boy_girl_roll_no, Room_no = Room_no, Date = Date, Entry = Entry)
                room.save()

                return Response({'msg': 'Entry registered!'}, status=status.HTTP_201_CREATED)
                    

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Exit_from_Hostel(APIView):

    def post(self, request, format=None):
        serializer = Exit_from_Hostel_Serializer(data=request.data)
        if serializer.is_valid():

            Number = serializer.data.get('Number')
            # Entered_boy_girl_name = serializer.data.get('Entered_boy_girl_name')
            Entered_boy_girl_roll_no = serializer.data.get('Entered_boy_girl_roll_no')
            # Host_boy_girl_name = serializer.data.get('Host_boy_girl_name')
            Host_boy_girl_roll_no = serializer.data.get('Host_boy_girl_roll_no')
            # Room_no = serializer.data.get('Room_no')
            Date = serializer.data.get('Date')
            Entry = serializer.data.get('Entry')
            Exit = serializer.data.get('Exit')

            queryset = Hostel_Entry.objects.filter(Number = Number, Entered_boy_girl_roll_no = Entered_boy_girl_roll_no, Host_boy_girl_roll_no = Host_boy_girl_roll_no, Date = Date, Entry = Entry)
            
            if queryset.exists():

                data = Hostel_Entry.objects.get(Number = Number, Entered_boy_girl_roll_no = Entered_boy_girl_roll_no, Host_boy_girl_roll_no = Host_boy_girl_roll_no, Date = Date, Entry = Entry)
                print(data.Exit)
                print(type(data.Exit))

                if data.Exit == 'not filled':
                    queryset.update(Exit = Exit)
                    return Response({'msg': 'Exit registered'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'msg': 'Exit has already been registered'}, status=status.HTTP_201_CREATED)


            else:
                return Response({'msg': 'Input data not matching'}, status=status.HTTP_226_IM_USED )
                    
        # return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Details_of_not_exited(APIView):
    # def get(self, request, format=None):
        # snippets = Hostel_Entry.objects.all()
        # serializer = Hostel_all_Serializer(snippets, many=True)
        # return Response(serializer.data)

    def get(self, request, format=None):
            Data = Hostel_Entry.objects.filter(Exit = 'not filled')
            serializer = Not_exited_serializer(Data, many=True)
            return Response(serializer.data)

        return Response({'Bad Request': 'Some problem occured...'}, status=status.HTTP_400_BAD_REQUEST)  