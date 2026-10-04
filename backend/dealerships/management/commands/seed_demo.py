from django.core.management.base import BaseCommand
from dealerships.models import Dealer,Review,CarMake,CarModel
class Command(BaseCommand):
    def handle(self,*a,**k):
        for n,c,s in [("Prairie Auto Center","Topeka","Kansas"),("Lone Star Motors","Wichita","Kansas"),("Metro Car Plaza","Dallas","Texas"),("Mountain View Autos","Denver","Colorado")]:
            d,_=Dealer.objects.get_or_create(name=n,defaults={"city":c,"state":s,"address":"100 Main St"})
            Review.objects.get_or_create(dealer=d,name="Demo Customer",review="Fantastic services")
        for n,mods in [("Toyota",["Camry","Corolla"]),("Honda",["Civic","Accord"]),("Ford",["Mustang","Escape"])]:
            m,_=CarMake.objects.get_or_create(name=n)
            for model in mods: CarModel.objects.get_or_create(make=m,name=model)
        self.stdout.write(self.style.SUCCESS("Demo data loaded"))
