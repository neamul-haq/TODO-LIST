from django.urls import path
from todo_app.views import home , add_task,task_list,edit_list,delete_list

urlpatterns =[
    path('',home),
    path('add_new_list/',add_task , name = 'addList' ),
    path('task_list/',task_list , name = 'taskList' ),
    path('edit_list/<int:id>',edit_list , name = 'edit_list' ),
    path('delete_list/<int:id>', delete_list , name = 'delete_list' )

]