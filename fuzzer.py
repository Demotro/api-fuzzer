import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from analyzer import analyze_response
from utils import build_fuzzed_url, load_payloads


def send_request(target_url, payload, timeout):
    fuzzed_url = build_fuzzed_url(target_url, payload)

    start_time = time.perf_counter()

    try:
        response = requests.get(fuzzed_url, timeout=timeout)
        end_time = time.perf_counter()

        response_time = round(end_time - start_time, 3)
        response_size = len(response.content)

        findings = analyze_response(
            response.status_code,
            response_size,
            response_time
        )

        return {
            "payload": payload,
            "url": fuzzed_url,
            "status_code": response.status_code,
            "response_size": response_size,
            "response_time": response_time,
            "findings": findings,
            "error": None
        }

    except requests.exceptions.Timeout:
        return {
            "payload": payload,
            "url": fuzzed_url,
            "status_code": None,
            "response_size": None,
            "response_time": None,
            "findings": ["TIMEOUT"],
            "error": "Request timed out"
        }

    except requests.exceptions.RequestException as error:
        return {
            "payload": payload,
            "url": fuzzed_url,
            "status_code": None,
            "response_size": None,
            "response_time": None,
            "findings": ["REQUEST_ERROR"],
            "error": str(error)
        }


def run_fuzzer(target_url, payload_file, threads, timeout):
    payloads = load_payloads(payload_file)

    if payloads is None:
        return None

    results = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_results = []

        for payload in payloads:
            future = executor.submit(send_request, target_url, payload, timeout)
            future_results.append(future)

        for future in as_completed(future_results):
            result = future.result()
            results.append(result)

    results.sort(key=lambda item: item["payload"])

    suspicious_count = 0

    for result in results:
        if result["findings"]:
            suspicious_count += 1

    return {
        "target_url": target_url,
        "payload_file": payload_file,
        "threads": threads,
        "timeout": timeout,
        "tested_payloads": len(payloads),
        "suspicious_count": suspicious_count,
        "results": results
    }