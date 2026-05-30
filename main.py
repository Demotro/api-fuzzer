import argparse

from config import DEFAULT_PAYLOAD_FILE, DEFAULT_THREADS, DEFAULT_TIMEOUT
from fuzzer import run_fuzzer
from reporter import print_report, save_json_report
from utils import validate_target_url


def main():
    parser = argparse.ArgumentParser(
        description="API Fuzzer & Response Analyzer CLI"
    )

    parser.add_argument(
        "target",
        help="Target URL containing FUZZ marker, for example https://httpbin.org/get?q=FUZZ"
    )

    parser.add_argument(
        "--payloads",
        default=DEFAULT_PAYLOAD_FILE,
        help="Path to payload file, default is payloads.txt"
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=DEFAULT_THREADS,
        help="Number of threads, default is 10"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="Request timeout in seconds, default is 5"
    )

    parser.add_argument(
        "--json",
        help="Save scan result to a JSON file, for example report.json"
    )

    args = parser.parse_args()

    if not validate_target_url(args.target):
        print("[ERROR] Target URL must contain FUZZ marker.")
        print("Example: https://httpbin.org/get?q=FUZZ")
        return

    if args.threads < 1:
        print("[ERROR] Number of threads must be at least 1.")
        return

    if args.timeout < 1:
        print("[ERROR] Timeout must be at least 1 second.")
        return

    result = run_fuzzer(
        args.target,
        args.payloads,
        args.threads,
        args.timeout
    )

    print_report(result)

    if args.json:
        save_json_report(result, args.json)


if __name__ == "__main__":
    main()