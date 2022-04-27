from datetime import datetime
from django.db import models
import datetime

# Make a database

## Hostel num               -> Integer
## Entered boy or girl name -> String
## Host boy or girl name    -> String
## Host Room no             -> String
## Enter Date               -> Integer
## Enter time               -> Integer
## Exit time                -> Integer


# d = datetime(2015, 10, 09, 23, 55, 59, 342380)
# hostel_entry_object = Hostel_Entry.objects.create(Date = d)
# hostel_entry_object.save()

#d = datetime.time(10, 33, 45)  
# exit_object = Hostel_Entry.objects.create(Exit = d)
# exit_object.save()

class Hostel_Entry(models.Model):                     # Example Format:
    Number = models.IntegerField()                    # 16
    Entered_boy_girl_name = models.TextField()        # Name
    Entered_boy_girl_roll_no = models.IntegerField()  # Roll_no
    Host_boy_girl_name = models.TextField()           # Vinu
    Host_boy_girl_roll_no = models.IntegerField()     # 210050165
    Room_no = models.TextField()                      # C307
    Date = models.TextField()                         # 24-06-2022
    Entry = models.TextField()                        # 08-30
    Exit = models.TextField(default="not filled")     # 22-00
