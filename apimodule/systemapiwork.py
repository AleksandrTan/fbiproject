"""
Module for requests to the system api
"""
import requests
import json

import config


class SystemApiRequests:

    def __init__(self, individual_id: int):
        self.api_url = config.MAIN_API_URL
        self.url_next_task = config.NEXT_TASK_URL
        self.individual_bot_id = individual_id

    def get_next_task(self) -> dict:
        """
        Get info about new task
        :return: dict
        """
        uri = self.url_next_task.replace("id", str(self.individual_bot_id))
        url = self.api_url + uri
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)

            if data["status"]:
                return {"status": data["status"], "task": data['tasks']}

        return {"status": False}


if __name__ == "__main__":
    req = SystemApiRequests(1)
    req.get_next_task()
