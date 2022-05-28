from django.test import TestCase
from .models import Category, Photo, Location

class LocationTest(TestCase):
    
    def setUp(self):
        """
        create new instances before a test
        
        """
        self.nairobi = Location(name = "Nairobi")
        
    def test_save_location(self):
        '''
        test whether new locations are added to the db 
        '''
        self.nairobi.save_location()
        self.tokyo.save_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations),2)
        
    def test_display_locations(self):
        '''
        This tests whether the display location function is getting the locations from the db
        '''
        self.nairobi.save_location()
        self.tokyo.save_location()
        self.assertEqual(len(Location.display_all_locations()), 2)    
        
class CategoryTest(TestCase):
    def setUp(self):
        '''
        creates new instances before a test
        '''
        self.nature = Category(name = "nature")
        self.travel = Category(name = "travel")

    def test_save_category_method(self):
        '''
        test whether new locations are added to the db 
        '''
        self.nature.save_category()
        self.animals.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 2)
        
class PhotoTest(TestCase):
    def setUp(self):
        '''
        creates new instances before a test
        '''
        self.nature = Category( name= "nature")
        self.nairobi = Location (name = "Nairobi")
        self.flower = Photo(photo = "image.png", name ='maua', description = 'beautiful', category= self.nature, location= self.nairobi)
        
        
    def tearDown(self):
            '''
            clears database after each test
            '''
            Photo.objects.all().delete()
            Category.objects.all().delete()
            Location.objects.all().delete()
    