import requests


def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Error: Received status code", response.status_code)
            return None

        users = response.json()

        for user in users[:num_users]:
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"City: {city}")
                print("-" * 30)

            except KeyError:
                print("Error: Unexpected JSON structure.")
                return None

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None


# Example call
fetch_and_display_users(3)