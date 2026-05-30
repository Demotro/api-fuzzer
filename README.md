# API Fuzzer & Response Analyzer CLI

A modular Python command-line tool for basic API fuzzing and response analysis. The tool injects payloads into a target URL, sends HTTP requests, measures response time and response size, detects suspicious responses, and supports JSON report export.

## Features

- Replaces the `FUZZ` marker in a target URL with payloads
- Loads payloads from a text file
- Sends HTTP GET requests
- Measures response time
- Measures response size
- Detects suspicious HTTP status codes
- Detects slow responses
- Detects large responses
- Uses multithreading for faster scanning
- Supports custom payload file, thread count, and timeout
- Exports results to a JSON report
- Handles timeouts, request errors, invalid thread values, invalid timeout values, and missing payload files

## Project Structure

```text
api-fuzzer/
├── main.py
├── fuzzer.py
├── analyzer.py
├── reporter.py
├── utils.py
├── config.py
├── payloads.txt
├── requirements.txt
├── README.md
└── report.json
```

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

On Windows:

```bash
py -m pip install -r requirements.txt
```

## Usage

Basic scan:

```bash
python main.py "https://httpbin.org/get?q=FUZZ"
```

On Windows:

```bash
py main.py "https://httpbin.org/get?q=FUZZ"
```

Scan with JSON export:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --json report.json
```

Scan with custom thread count:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --threads 5
```

Scan with custom timeout:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --timeout 10
```

Use a custom payload file:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --payloads payloads.txt
```

## Example Output

```text
API Fuzzer & Response Analyzer CLI
----------------------------------
Target: https://httpbin.org/get?q=FUZZ
Payload file: payloads.txt
Threads: 10
Timeout: 5s

[200] Payload: test | Size: 334 B | Time: 1.423s
[200] Payload: admin | Size: 336 B | Time: 1.346s
[200] Payload: 123 | Size: 332 B | Time: 1.413s

----------------------------------
Scan finished
Tested payloads: 16
Suspicious responses: 0
```

## Findings

The analyzer can mark responses with the following findings:

```text
SUSPICIOUS_STATUS_CODE
SLOW_RESPONSE
LARGE_RESPONSE
TIMEOUT
REQUEST_ERROR
```

## Example JSON Report

The tool can export scan results into a JSON file:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --json report.json
```

The report contains information such as the target URL, payload file, thread count, timeout, tested payloads, suspicious response count, status codes, response sizes, response times, findings, and errors.

## Technologies Used

- Python
- requests
- argparse
- concurrent.futures
- JSON
- HTTP
- API testing
- Modular project structure

## Disclaimer

This tool is intended for educational purposes and basic API security testing only.