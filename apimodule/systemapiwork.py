"""
Module for requests to the system api
"""
from logsource.logconfig import logger
import requests
import json

import config


class SystemApiRequests:

    def __init__(self, individual_id: int):
        self.api_url = config.MAIN_API_URL
        self.url_next_task = config.NEXT_TASK_URL
        self.url_task_done = config.TASK_RESULT_DONE
        self.url_task_fail = config.TASK_RESULT_FAIL
        self.individual_bot_id = individual_id

    def get_new_task(self) -> dict:
        """
        Get params for new task
        :return: dict
        """
        uri = self.url_next_task.replace("id", str(self.individual_bot_id))
        url = self.api_url + uri
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"], "error": False, "task_name": data['task_name'],
                        "task_id": data['task_id']}

        return {"status": False, "error": False}

    def task_report(self, task_id: int, data_result: dict) -> bool:
        """
        Report about task results
        :param data_result: dict
        :param task_id: int
        :return: dict
        """
        if data_result["status"]:
            uri = self.url_task_done.replace("id", str(self.individual_bot_id)).replace("ib", str(task_id))
        else:
            uri = self.url_task_fail.replace("id", str(self.individual_bot_id)).replace("ib", str(task_id))

        url = self.api_url + uri
        try:
            response = requests.post(url)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return False

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return True

        return False


if __name__ == "__main__":
    req = SystemApiRequests(1)
    req.get_new_task()
