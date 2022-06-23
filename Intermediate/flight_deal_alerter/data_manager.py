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

    def update_sheet_row_field(self, field, row):
        change = {
            "city": {
            field: row[field]
            }
        }
        res = req.put(
            url=f"{self.base_url}/{row['id']}", headers=self.auth_header, json=change)
        res.raise_for_status()
