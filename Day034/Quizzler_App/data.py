import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
questions = response.json()
question_data = questions["results"]
