from django.test import TestCase
from django.urls import reverse
from .models import Country


class CountryModelTest(TestCase):
    def test_country_creation(self):
        country = Country.objects.create(
            cca3="FRA",
            name="France",
            population=67000000,
            area=551695
        )
        self.assertEqual(country.name, "France")


class CountryViewsTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            cca3="FRA",
            name="France"
        )

    def test_country_list_view(self):
        response = self.client.get("/countries/")
        self.assertEqual(response.status_code, 200)

    def test_country_detail_view(self):
        response = self.client.get(f"/countries/{self.country.cca3}/")
        self.assertEqual(response.status_code, 200)

