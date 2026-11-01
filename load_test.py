import requests
import concurrent.futures
import time

URL = "http://127.0.0.1:8000/order"

payload = {
    "customer_name": "LoadTestUser",
    "product_name": "Mahua Cookies",
    "quantity": 1,
    "price": 150
}

def send_order(order_no):
    start = time.time()

    try:
        response = requests.post(URL, json=payload, timeout=5)
        elapsed = round(time.time() - start, 2)

        return {
            "order": order_no,
            "status_code": response.status_code,
            "response_time": elapsed
        }

    except Exception as e:
        elapsed = round(time.time() - start, 2)

        return {
            "order": order_no,
            "status_code": "FAILED",
            "response_time": elapsed,
            "error": str(e)
        }


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(send_order, range(1, 21)))

for result in results:
    print(result)

total_requests = len(results)

failed_requests = sum(
    1 for result in results
    if result["status_code"] == "FAILED"
)

successful_requests = total_requests - failed_requests

failure_percentage = (
    failed_requests / total_requests
) * 100

print("\n--- Load Test Summary ---")
print("Total Requests:", total_requests)
print("Successful Requests:", successful_requests)
print("Failed Requests:", failed_requests)
print("Failure Percentage:", round(failure_percentage, 2), "%")   