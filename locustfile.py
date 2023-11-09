"""Defines the locust process"""

# standard lib imports #
import random

# 3rd party imports #
import locust

with open("names/first_names.txt", "r", encoding="utf-8") as file:
    people_names: list[str] = [x.strip() for x in file.readlines()]

with open("names/item_names.txt", "r", encoding="utf-8") as file:
    item_names: list[str] = [x.strip() for x in file.readlines()]


class BasicUser(locust.HttpUser):
    """A user which logs in, then views, adds to basket, and checks out items"""

    wait_time = locust.between(1, 5)  # seconds puase between tasks

    @locust.task(14)
    def view_item(self):
        """call the /view_item/ endpoint"""
        self.client.get(f"/view_item/{random.choice(item_names)}")

    @locust.task(5)
    def add_item_to_basket(self):
        """call the /add_item_to_basket/ endpoint"""
        self.client.post(
            "/add_item_to_basket", json={"item_name": random.choice(item_names)}
        )

    @locust.task(1)
    def check_out(self):
        """call the /check_out/ endpoint"""
        self.client.post("/check_out")

    def on_start(self):
        """Tasks performed by user when they are first spawned"""
        self.user_name = random.choice(people_names)  # choose a name for themselves

        # log in #
        self.client.post(
            "/log_user_in",
            json={"user_name": self.user_name, "password": "password1234"},
        )
