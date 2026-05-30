from config import FUZZ_MARKER


def validate_target_url(target_url):
    return FUZZ_MARKER in target_url


def load_payloads(payload_file):
    try:
        with open(payload_file, "r", encoding="utf-8") as file:
            payloads = file.read().splitlines()

    except FileNotFoundError:
        print(f"[ERROR] Payload file not found: {payload_file}")
        return None

    cleaned_payloads = []

    for payload in payloads:
        payload = payload.strip()

        if payload:
            cleaned_payloads.append(payload)

    return cleaned_payloads


def build_fuzzed_url(target_url, payload):
    return target_url.replace(FUZZ_MARKER, payload)