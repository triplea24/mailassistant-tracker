from django.db import models
from django.db.models.signal import post_save
# from mailassist.auth.models import User
from django.contrib.auth.models import User
from uuid import uuid4 as track_key_generator
# from django.db.models.signal import pre_save

class Mail(models.Model)
	

class Contact(models.Model):
	name = models.CharField(max_length=256,blank = True)
	email = models.EmailField(unique = True)

class Message(models.Model):
	owner = models.ForeignKey(User)
	timestamp = models.DateTimeField(blank = True)
	subject = models.CharField(max_length=256)
	from_contact = models.ForeignKey(Contact)
	threadId = models.ForeignKey(Message,null = True,blank = True)
	read_count = models.IntegerField(default = 0)
	track_key = models.CharField(max_length = 36, unique = True , blank = True)

	def is_draft():
		return timestamp is not None
	def is_reply():
		return threadId is not None
	# fromContact
	
class Trace(models.Model):
	message = models.ForeignKey(Message)
	timestamp = models.DateTimeField(auto_now_add = True)
	device_ip = models.TextField(blank=True)
	device_browser = models.TextField(blank = True)
	device_browser_family = models.TextField(blank = True)
	device_browser_version_string = models.TextField(blank = True)
	device_os = models.TextField(blank = True)
	device_os_family = models.TextField(blank = True)
	device_os_version_string = models.TextField(blank = True)
	device_type = models.TextField(blank = True)
	device_type_family = models.TextField(blank = True) 

@receiver(post_save,sender=Message,dispath_uid = "generate a track key")
def generate_track_key(sender,instance,**kwargs):
	instance.track_key = str(track_key_generator())

@receiver(post_save,sender=Trace,dispath_uid = "update track counter")
def update_track_counter(sender,instance,**kwargs):
	instance.message.read_count += 1
