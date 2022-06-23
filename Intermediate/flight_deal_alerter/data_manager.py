import requests as req
from env.config import SHEETS_ENDPOINT as base_url, SHEETS_AUTH_HEADER as auth_header


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.base_url: str = base_url
        self.auth_header: dict = auth_header
        self.data = {}

    def get_cities(self) -> dict:
        res = req.get(url=f"{self.base_url}/cities", headers=self.auth_header)
        res.raise_for_status()
        self.data = res.json()["cities"]
        return self.data

    def update_city_sheet_row_field(self, field, row):
        change = {
            "city": {
            field: row[field]
            }
        }
        res = req.put(
            url=f"{self.base_url}/cities/{row['id']}", headers=self.auth_header, json=change)
        res.raise_for_status()

    def get_customer_emails(self):
        response = req.get(f"{self.base_url}/users")
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
