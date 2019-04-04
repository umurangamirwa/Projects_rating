from django.test import TestCase
from .models import Project,Profile,Rating

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rates= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rates,Project))

    # Testing Save Method
    def test_save_method(self):
        self.rates.save_image()
        description= Project.objects.all()
        self.assertTrue(len(description) > 0)

        
       
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.rates= Rating()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rates,Rating))

   
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.rates= Profile( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rates,Profile))
