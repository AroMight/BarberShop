from django.db import models
from users.models import Employee, Customer


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.ImageField(
        upload_to='services/covers/%Y/%m/%d', null=True, blank=True, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration_time = models.DurationField()
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    barbers = models.ManyToManyField(Employee, related_name='services')

    def __str__(self):
        return str(self.name)


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer) + ' - ' + str(self.service) + ' - ' + str(self.date) + ' - ' + str(self.time)

    class Meta:
        ordering = ['date', 'time']
