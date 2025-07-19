from django.db import models

class Order(models.Model):
    customer_name = models.CharField("اسم العميل", max_length=100)
    order_date = models.DateTimeField("تاريخ الطلب", auto_now_add=True)
    is_paid = models.BooleanField("مدفوع؟", default=False)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب {self.id} - {self.customer_name}"
