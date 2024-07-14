from django.test import TestCase
from .models import CustomUser, Product, Staff, Category

# Create your tests here.

class TestCreateCategory(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testCategory = Category.objects.create(name="category")
        productCategory = Product.objects.create(name="product")

    def testCategory(self):
        cat = Category.objects.get(id=1)             
        pro = Product.objects.get(id=1)
        self.assertEqual(str(cat), "category")
        self.assertEqual(str(pro), "product")

