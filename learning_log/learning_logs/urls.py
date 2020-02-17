from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
	#主页
	path('',views.index,name='index'),
	path('topics/',views.topics,name='topics'),
	path('topics/<topic_id>\d+/',views.topic,name='topic'),
	path('new_topic/',views.new_topic,name='new_topic'),
	path('new_entry/<topic_id>\d+',views.new_entry,name='new_entry'),
	path('edit_entry/<entry_id>\d+',views.edit_entry,name='edit_entry'),

]