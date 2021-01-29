from django.test import TestCase, Client
from .views import get_token
from .models import BookingModel
from regularTour.models import RegularTourModel
from schedule.models import RegTourScheduleModel
import datetime
# Create your tests here.

class UnitTestBooking(TestCase):
    def test_token_return_64_char(self):
        a = get_token()
        self.assertEqual(len(a), 64)

    def test_booking_model(self):
        regTour = RegularTourModel.objects.create(
            destination = "jkt",
            description = "desc",
            distance = "2km",
            duration = "2hours",
            meeting_point = "here",
            route = "there",
            photo = ".jpg",
            location_map = "here",
        )
        sched = RegTourScheduleModel.objects.create(
            date = datetime.datetime.now().strftime('%Y-%m-%d'),
            startTime = datetime.datetime.now().strftime("%X"),
            slot = 10,
            language = "English",
            tourGuide = "her",
            regularTour = regTour
        )
        book = BookingModel.objects.create(
            fullName = "albedo",
            mail = "albedo@gmail.com",
            participants = 2,
            country = "Australia",
            phone =123456,
            confirmed = False,
            token = "rjVLQw30dNGcm6mzTNzgnI665Vxk1C6OwgQR8DGdS059hQMWqJETgIygsSykiuUQ",
            schedule = sched,
        )
        count = BookingModel.objects.all().count()
        self.assertEqual(count, 1)

        a = book.getScheduleID()
        self.assertEqual(book.id, a)

        a = book.getRegTourID()
        self.assertEqual(regTour.id, a)

        confirmation_url = '/confirmation/' + book.token
        response = self.client.get(confirmation_url)
        self.assertEqual(response.status_code, 200)

        read_url = '/booking/' + str(regTour.id) + '/' + str(sched.id)
        response = self.client.get(read_url)
        self.assertEqual(response.status_code, 200)

        book.confirmed = True
        book.save()
        confirmation_url = '/confirmation/' + book.token
        response = self.client.get(confirmation_url)
        self.assertEqual(response.status_code, 200)

        delete_booking = '/booking/'+str(book.id)+'/delete'
        response = self.client.get(delete_booking)
        self.assertEqual(BookingModel.objects.all().count(), 0)

    def test_booking_form_url_exists(self):
        regTour = RegularTourModel.objects.create(
            destination = "jkt",
            description = "desc",
            distance = "2km",
            duration = "2hours",
            meeting_point = "here",
            route = "there",
            photo = ".jpg",
            location_map = "here",
        )
        sched = RegTourScheduleModel.objects.create(
            date = datetime.datetime.now().strftime('%Y-%m-%d'),
            startTime = datetime.datetime.now().strftime("%X"),
            slot = 10,
            language = "English",
            tourGuide = "her",
            regularTour = regTour
        )
        url_form = '/regTour/' + str(regTour.id) + '/' + str(sched.id) + '/booking'
        response = self.client.get(url_form)
        self.assertEqual(response.status_code, 200)

        new_resp = self.client.get(url_form)
        html_resp = new_resp.content.decode('utf8')
        self.assertIn('</form>', html_resp)