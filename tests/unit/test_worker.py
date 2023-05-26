from etd.worker import Worker
import requests
import requests_mock


class TestWorkerClass():

    def test_version(self):
        expected_version = "0.0.1"
        worker = Worker()
        version = worker.get_version()
        assert version == expected_version

    def test_api(requests_mock):
        expected_msg = "REST api is running."
        url = "https://dash.harvard.edu/rest/test"
        requests_mock.get(url, text="REST api is NOT running.")
        worker = Worker()
        msg = worker.call_api()
        print(msg)
        assert msg == expected_msg
