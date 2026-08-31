from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="properties")
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="properties/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"pk": self.pk})

class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inquiries")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.property.title}"
