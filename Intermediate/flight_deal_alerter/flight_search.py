import requests
from env.config import FLIGHT_API_KEY as key, FLIGHT_API_ENDPOINT as base_url

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        pass

    def get_iata_code(self, city_name):
        # TODO Send request
        code = "TESTING"
        return code