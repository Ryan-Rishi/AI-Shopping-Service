from django.db import models

# Defining the Product model
class Product(models.Model):
    # The name of the product, a character field with a maximum length of 255
    name = models.CharField(max_length=255)

    # The price of the product, a decimal field with a maximum of 10 digits and 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # The description of the product, a text field
    description = models.TextField()

    # The URL of the product's image, a URL field
    image_url = models.URLField()

    # Add more fields as needed

    # String representation of the Product model
    def __str__(self):
        return self.name