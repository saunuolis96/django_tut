from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # silly:
    # url(r'^bla/latest\.html$', views.index),
    # end of silly
    # ex: /polls/
    url(r'^$', views.index, name='index'),
#     ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#      added the word 'specifics'
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]