import urllib.request, urllib.parse
import json
from dotenv import load_dotenv
import os

# Loads the .env file
load_dotenv()

# Gets the API key from .env file
api_key = os.getenv("GOOGLE_GEOCODE_API_KEY")

if api_key is False or api_key is None:
  print("Please check the api key!")
  quit()
else: 
  service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

print("Welcome to GeoCoder!")

while True:
  address = input("Enter location: ")
  if len(address) < 1 or address == "q": break

  # Parameters for the geocode search query 
  params = {}
  params["address"] = address
  params["key"] = api_key

  # urlencode() converts an object of key-value pairs to a percent-encoded ASCII test strings.
  url = service_url + urllib.parse.urlencode(params)

  # Shows the url
  print("Retrieving", url)

  # Sends a GET request
  u_handle = urllib.request.urlopen(url)
  json_data = u_handle.read().decode()

  print(json_data)

  # Load the json_data
  try:
    data = json.loads(json_data)
  except:
    data = None

  if data is None or data["status"] != "OK":
    print("Failure to Retrieve Location")
    print(data)
    continue

  # the json has two keys "results" & "status"
  print(f"Status: {data['status']}")

  street_add = data["results"][0]["formatted_address"]
  coords = data["results"][0]["geometry"]["location"]

  print(f"Street Address: {street_add}")
  print(f"Coords: {coords}")

  add_comps = data["results"][0]["address_components"]
  country_code = add_comps[len(add_comps) - 1]["short_name"]

  print(f"Country Code: {country_code}")