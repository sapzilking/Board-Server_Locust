from locust import HttpUser, task, between
import random


class BoardServer(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId": "topojs15",
                                                 "password": "1234"})

    @task
    def view_search(self):
        sortStatus = random.choice(["CATEGORY", "NEWEST", "OLDEST"])
        categoryId = random.randint(1, 10)
        name = '테스트 게시글' + str(random.randint(1, 10000))
        headers = {'Content-Type': 'application/json'}
        data = {"sortStatus": sortStatus,
                "categoryId": categoryId,
                "name": name}
        self.client.post("/search", json=data, headers=headers)