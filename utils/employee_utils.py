from django.db.models import Q, Count
from users.models import Employee


def get_available_employee(form):
    selected_date = form.cleaned_data["date"]
    selected_time = form.cleaned_data["time"]
    service = form.cleaned_data["service"]

    # Get the available employee
    employees = Employee.objects.filter(services=service).select_related("reservations")

    # Exclude employees that are already booked
    available_employees = employees.exclude(
        Q(reservations__date=selected_date)
        & Q(reservations__time=selected_time)
        & Q(reservations__status=True)
    )

    # Get the employee with the least reservations for that day
    available_employee = (
        available_employees.annotate(
            num_reservations=Count(
                "reservations", filter=Q(reservations__date=selected_date)
            )
        )
        .order_by("num_reservations")
        .first()
    )

    return available_employee
