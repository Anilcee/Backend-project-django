from django.contrib import admin
from .models import PetGallery,OurServices,Pets,Comments,CustomUser,Team,HomeSlide

# Register your models here.
admin.site.register(PetGallery)
admin.site.register(Team)
admin.site.register(HomeSlide)
admin.site.register(OurServices)
admin.site.register(Pets)
admin.site.register(Comments)
admin.site.register(CustomUser)
