from config import (
    LARGE_RESPONSE_THRESHOLD,
    SLOW_RESPONSE_THRESHOLD,
    SUSPICIOUS_STATUS_CODES
)


def analyze_response(status_code, response_size, response_time):
    findings = []

    if status_code in SUSPICIOUS_STATUS_CODES:
        findings.append("SUSPICIOUS_STATUS_CODE")

    if response_size >= LARGE_RESPONSE_THRESHOLD:
        findings.append("LARGE_RESPONSE")

    if response_time >= SLOW_RESPONSE_THRESHOLD:
        findings.append("SLOW_RESPONSE")

    return findings