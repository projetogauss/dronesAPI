from django.db import models

# Create your models here.
class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

#toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages', release_date=toy_release_date, toy_category='Actionfigures', was_included_in_home=False)
#sqlite3 db.sqlite3 "SELECT * FROM toys_toy ORDER BY name;"

#json_string_for_new_toy = '{"name":"Clash Royale play set","description":"6
#figures from Clash Royale","release_date":"2017-10-09T12:10:00.776594Z","toy_category":"Playset","was_
#included_in_home":false}'
#json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8")
#stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
#parser = JSONParser()
#parsed_new_toy = parser.parse(stream_for_new_toy)
#print(parsed_new_toy)