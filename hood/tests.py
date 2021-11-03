from django.test import TestCase
from hood.models import Post, Profile, Business, Neighbourhood
from django.contrib.auth.models import User

# Create your tests here.
class Neighbourhoodtest(TestCase):
    '''
    Class to test all neighbourhood model methods
    '''
    def setUp(self):
        '''
        Function to create new instance of a neighbourhood class
        '''
        self.hood=Neighbourhood(name='Kibera',location='Kibera',image='pic.jpg',)
        self.hood.save()

    def test_instance(self):
        '''
        Test neighbourhood class instantiation
        '''
        self.assertTrue(isinstance(self.hood,Neighbourhood))

    def tearDown(self):
        '''
        Function to delete every test instance after it runs
        '''
        Neighbourhood.objects.all().delete()

    def create_hood_test(self):
        '''
        Tests that a new hood is saved 
        '''
        self.hood.create_hood()
        hoodlist = Neighbourhood.objects.all()
        self.assertTrue(len(hoodlist)==1)

    def delete_hood_test(self):
        '''
        Tests that a Neighborhood instance can be deleted
        '''
        self.hood.save()
        Neighbourhood.delete(self.hood)
        hoodlist = Neighbourhood.objects.all()
        self.assertEqual(len(hoodlist,0))


class Profiletest(TestCase):
    '''
    Class to test the profile class methods
    '''
    def setUp(self):
        self.profile=Profile(username='test', email='test@hood.com', profile_pic = 'pic.jpeg', bio = "test", neighbourhood = "nairobi")
        

    def test_instance(self):
        '''
        Test class to check instantiation of a new profile instance
        '''
        self.assertTrue(isinstance(self.profile,Profile))

    def tearDown(self):
        '''
        Class to delete all test instances after tests finish running
        '''
        User.objects.all().delete()
        Profile.objects.all().delete()

    def save_profile_test(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==1)

    def delete_profile_test(self):
        '''
        Tests that a profile instance can be deleted succesfully
        '''
        self.profile.save()
        Profile.delete(self.profile)
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles,0))

class Businesstest(TestCase):
    '''
    Class to test the business class models
    '''
    def setUp(self):
        self.bs= Business(name='test',owner="dan",neighbourhoodhood=1,email='test@gmail.com',description='my test')
        self.bs.save()

    def tearDown(self):
        '''
        Will delete all test instances on completion
        '''
        Business.objects.all().delete()

    def savebussines_test(self):
        '''
        testcase to test instantiation of business class object
        '''    
        self.bs.save()
        bslist=Business.objects.all()
        self.assertTrue(len(bslist)==1)

    def delete_business_test(self):
        '''
        testcase to delete a instance of business class
        '''
        self.bs.save()
        Business.delete_biz(self.bs)
        bslist=Business.objects.all()
        self.assertTrue(len(bslist)==0)