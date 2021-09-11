import urllib.request, urllib.parse
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Gets the API key from .env file
api_key = os.getenv("GOOGLE_GEOCODE_API_KEY")

if api_key is False or api_key is None:
  print("please check the api key")
  url = "https://google.com"
else: 
  url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
  address = input("Enter location: ")
  if len(address) < 1 or address == "q": break

  # Parameters for the geocode search query 
  params = {}
  params["address"] = address
  params["key"] = api_key

  # urlencode() converts an object of key-value pairs to a percent-encoded ASCII test strings.
  url += urllib.parse.urlencode(params)

  # Shows the url
  print("Retrieving", url)

  # Sends a GET request
  u_handle = urllib.request.urlopen(url)
  data = u_handle.read().decode()

  # Load the json data
  try:
    json_data = json.loads(data)
  except:
    json_data = None

  if json_data is None or json_data["status"] != "OK":
    print("Failure to Retrieve Location")
    print(data)
    continue

  # the json has two keys "results" & "status"
  print(f"Status: {json_data['status']}")

  street_add = json_data["results"][0]["formatted_address"]
  coords = json_data["results"][0]["geometry"]["location"]

  print(f"Street Address: {street_add}")
  print(f"Coords: {coords}")