from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    
    # dest1 = Destination()
    # dest1.name= 'Mumbai'
    # dest1.desc = 'The City that have Never Sleep'
    # dest1.img = 'assets/images/destination_1.jpg'
    # dest1.price=700
    # dest1.offer = False
    
    # dest2 = Destination()
    # dest2.name= 'Hyderabad'
    # dest2.desc = 'The City have Biriyani to eat'
    # dest2.img = 'assets\images\destination_1.jpg'
    # dest2.price=700
    # dest2.offer = True
    
  
    
    # dest3 = Destination()
    # dest3.name= 'Bangalore'
    # dest3.desc = 'The City have everything '
    # dest3.img = 'assets\images\destination_3.jpg'
    # dest3.price=700
    # dest3.offer = False
    
    
    # dests = [dest1,dest2,dest3]
    dests = Destination.objects.all()
     
    return render(request, "index.html", {'dests': dests})
                  