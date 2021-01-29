from django.test import TestCase
from django.test import Client
from django.test import LiveServerTestCase
from django.urls import resolve
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time

class RegularTourTest(TestCase):
    def test_list_regular_tour_page_is_exist(self):
        self.response() = Client().get('/regularTour/listRegularTour/')
        self.assertEqual(self.response.status_code, 200)
    
    def test_create_regular_tour_page_is_exist(self):
        self.response() = Client().get('/regularTour/createRegularTour/')
        self.assertEqual(self.response.status_code, 200)