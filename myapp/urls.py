
from django.urls import path

from myapp.views import addstudent, home, studentIdCall, updateStudent, studentDelete,signup,signin,user_logout,update_password

urlpatterns = [
    
    path('home/', home, name='home'), 

    path('addstudent/', addstudent, name='addstudent'),

    path('studentIdCall/<int:id>', studentIdCall , name='studentIdCall'),

    path('updateStudent/',updateStudent,name='updateStudent'),

    path('studentDelete/<int:id>',studentDelete,name='studentDelete'),

    path('signup/', signup ,name='signup'),

    path('signin/',signin,name='signin'),

    path('logout/',user_logout,name='logout'),

    path('updatepassword/',update_password,name='updatepassword')
    
    
]