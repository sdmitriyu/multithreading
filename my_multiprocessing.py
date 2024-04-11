import multiprocessing
import time

class RequestHandler:
    def __init__(self):
        pass

    def process_request(self, request):
        # Simulate processing a request
        time.sleep(1)
        print(f"Processed request: {request}")

    def handle_requests(self, requests):
        processes = []
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')  # Set the start method to 'spawn' globally
    handler = RequestHandler()
    requests = [1, 2, 3, 4, 5]  # Example requests
    handler.handle_requests(requests)
