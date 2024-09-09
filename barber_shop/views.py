from django.views.generic import TemplateView
from reservations.forms import ReservationForm
from reservations.models import Service
from users.models import Branch, Employee


class HomeView(TemplateView):

    services = Service.objects.filter(status=True, is_highlighted=True).only("name", "price", "cover")
    employees = Employee.objects.all().only("user__username", "profile_photo")
    units = Branch.objects.all().only("district", "address", "photo")

    template_name = "barber_shop/home.html"
    extra_context = {
        "btn_action": "Confirm",
        "form": ReservationForm(),
        "services": services,
        "employees": employees,
        "units": units,
    }
