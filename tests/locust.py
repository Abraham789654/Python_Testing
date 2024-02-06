from locust import HttpUser, between, task

class UserBehavior(HttpUser):
    wait_time = between(5, 9)

    @task
    def index(self):
        self.client.get("/")

    @task
    def submit_email(self):
        self.client.post("/showSummary", {"email": "test@example.com"})

    @task
    def book_competition(self):
        self.client.get("/book/Spring%20Festival/Iron%20Temple")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces", {"club": "Iron Temple", "competition": "Spring Festival", "places": 2})
