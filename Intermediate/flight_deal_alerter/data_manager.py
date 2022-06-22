import requests as req
from env.config import SHEETS_ENDPOINT as base_url, SHEETS_AUTH_HEADER as auth_header


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.base_url: str = base_url
        self.auth_header: dict = auth_header
        self.data = {}

    def get_sheet_data(self) -> dict:
        res = req.get(url=self.base_url, headers=self.auth_header)
        res.raise_for_status()
        self.data = res.json()["cities"]
        return self.data

    def update_sheet_data(self, new_data):
        for item in new_data:
            change = {
                "city": {
                    "iataCode": item["iataCode"]
                }
            }
            res = req.put(
                url=f"{self.base_url}/{item['id']}", headers=self.auth_header, json=change)
        res.raise_for_status()
        return self.get_sheet_data()
