import json


def print_report(result):
    if result is None:
        return

    print("API Fuzzer & Response Analyzer CLI")
    print("----------------------------------")
    print("Target:", result["target_url"])
    print("Payload file:", result["payload_file"])
    print("Threads:", result["threads"])
    print("Timeout:", str(result["timeout"]) + "s")
    print()

    for item in result["results"]:
        status_code = item["status_code"]
        payload = item["payload"]
        response_size = item["response_size"]
        response_time = item["response_time"]
        findings = item["findings"]
        error = item["error"]

        if error:
            print(f"[ERROR] Payload: {payload} | Error: {error}")
            continue

        finding_text = ""

        if findings:
            finding_text = " [" + ", ".join(findings) + "]"

        print(
            f"[{status_code}] "
            f"Payload: {payload} | "
            f"Size: {response_size} B | "
            f"Time: {response_time}s"
            + finding_text
        )

    print()
    print("----------------------------------")
    print("Scan finished")
    print("Tested payloads:", result["tested_payloads"])
    print("Suspicious responses:", result["suspicious_count"])


def save_json_report(result, filename):
    if result is None:
        return

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    print()
    print(f"[INFO] JSON report saved to {filename}")