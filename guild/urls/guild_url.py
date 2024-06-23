from django.urls import path
from guild.views.guild_view import CreateListGuild, RetrieveUpdateDeleteGuild, AddMemberToGuild, ListMyGuilds


urlpatterns = [
    path('guilds/', CreateListGuild.as_view(), name='guilds'),
    path('guilds/<uuid:id>/', CreateListGuild.as_view(), name='guilds'),
    path('guilds/delete/<uuid:guild_id>/', RetrieveUpdateDeleteGuild.as_view(), name='guilds'),    
    path('guilds/<uuid:guild_id>/add_member/<uuid:user_id>/', AddMemberToGuild.as_view(), name='add_member_to_guild'),
    path('guilds/my_guilds/', ListMyGuilds.as_view(), name='my_guilds')
]
