import time
import requests
from django.core.management.base import BaseCommand
from countries.models import Country

API_URL = "https://restcountries.com/v3.1/all?fields=name,cca3,capital,region,subregion,population,area,flags"

class Command(BaseCommand):
    help = "Import countries from REST Countries API"

    def handle(self, *args, **kwargs):
        retries = 3

        for attempt in range(retries):
            try:
                response = requests.get(API_URL, timeout=10)
                response.raise_for_status()
                data = response.json()
                break
            except requests.RequestException as e:
                self.stdout.write(f"Tentative {attempt + 1} échouée")
                time.sleep(2)
        else:
            self.stderr.write("API indisponible après plusieurs tentatives")
            return

        for item in data:
            capitals = item.get("capital")

            Country.objects.update_or_create(
                cca3=item.get("cca3"),
                defaults={
                    "name": item["name"]["common"],
                    "capital": capitals[0] if capitals else None,
                    "region": item.get("region"),
                    "subregion": item.get("subregion"),
                    "population": item.get("population", 0),
                    "area": item.get("area", 0),
                    "flag_url": item.get("flags", {}).get("png"),
                }
            )

        self.stdout.write(self.style.SUCCESS("Import terminé"))
