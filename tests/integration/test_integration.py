from etd.worker import Worker


class TestWorkerIntegrationClass():

    def test_api(self):
        expected_msg = "REST api is running."
        worker = Worker()
        msg = worker.call_api()
        assert msg == expected_msg
