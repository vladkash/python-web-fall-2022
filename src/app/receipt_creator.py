from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import grpc
from generated.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server
import generated.service_pb2 as service__pb2


class Service(TestServiceServicer):
    def CreateReceipt(self, request, context):
        return service__pb2.ReceiptResponse(message=f"Successful consumption from card {request.card_number}")


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
