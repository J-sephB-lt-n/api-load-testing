# standard lib imports #
import random

# 3rd party imports #
import locust

with open("names/first_names.txt", "r", encoding="utf-8") as file:
    people_names: list[str] = [x.strip() for x in file.readlines()]

with open("names/item_names.txt", "r", encoding="utf-8") as file:
    item_names: list[str] = [x.strip() for x in file.readlines()]


class BasicUser(locust.HttpUser):
    """docstring TODO"""

    wait_time = locust.between(1, 5)  # seconds puase between tasks

    @locust.task(5)
    def view_item(self):
        """docstring TODO"""
        self.client.get(f"/view_item/{random.choice(item_names)}")

    @locust.task(1)
    def add_item_to_basket(self):
        """docstring TODO"""
        self.client.post(
            "/add_item_to_basket", json={"item_name": random.choice(item_names)}
        )

    def on_start(self):
        """docstring TODO"""
        self.user_name = random.choice(people_names)
        self.client.post(
            "/log_user_in",
            json={"user_name": self.user_name, "password": "password1234"},
        )
