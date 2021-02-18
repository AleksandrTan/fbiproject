"""
Module for requests to the system api
"""
import logging
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
        Get params for new task
        :return: dict
        """
        uri = self.url_next_task.replace("id", str(self.individual_bot_id))
        url = self.api_url + uri
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as error:
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"], "task_name": data['task_name']}

        return {"status": False}


if __name__ == "__main__":
    req = SystemApiRequests(1)
    req.get_next_task()
