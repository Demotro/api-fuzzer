# API Fuzzer & Response Analyzer CLI

A modular command-line tool for API fuzzing and response analysis, built with Python.

The project sends test payloads to API endpoints, measures response time and response size, detects suspicious responses, supports multithreaded execution and exports scan results into a JSON report.

## Highlights

- Modular Python project split into multiple files
- Payload-based API endpoint testing
- Response analysis based on status code, response time and response size
- Suspicious response detection
- Multithreaded request execution
- Configurable timeout, payload file and thread count
- Centralized configuration in `config.py`
- JSON report export
- Input validation and error handling

## Features

- Replace the `FUZZ` marker in a target URL with payloads
- Load payloads from a text file
- Send HTTP GET requests
- Measure response time
- Measure response size
- Detect suspicious HTTP status codes
- Detect slow responses
- Detect large responses
- Handle request timeouts and request errors
- Export detailed results to a JSON report

## Technologies

- Python
- requests
- argparse
- concurrent.futures
- JSON
- HTTP
- API testing
- Modular project structure

## Project Structure

- `main.py` - command-line interface and argument handling
- `fuzzer.py` - request sending, payload execution and multithreading
- `analyzer.py` - response analysis and finding detection
- `reporter.py` - terminal output and JSON report export
- `utils.py` - helper functions for payload loading and URL handling
- `config.py` - project configuration and detection thresholds
- `payloads.txt` - test payloads
- `requirements.txt` - project dependencies
- `README.md` - project documentation
- `report.json` - example JSON scan report

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

On Windows:

```bash
py -m pip install -r requirements.txt
```

## How It Works

The tool requires a target URL containing the `FUZZ` marker.

Example:

```bash
py main.py "https://httpbin.org/get?q=FUZZ"
```

The program replaces `FUZZ` with each payload from `payloads.txt`.

For each generated request, the tool records:

- HTTP status code
- response size
- response time
- detected findings
- request errors, if any

Responses are analyzed and marked with findings when they match configured suspicious conditions.

## Findings

The analyzer can mark responses with the following findings:

- `SUSPICIOUS_STATUS_CODE` - response returned a server-side error status code
- `SLOW_RESPONSE` - response time is higher than the configured threshold
- `LARGE_RESPONSE` - response size is higher than the configured threshold
- `TIMEOUT` - request exceeded the configured timeout
- `REQUEST_ERROR` - request failed because of a connection or request error

## Usage

Basic scan:

```bash
py main.py "https://httpbin.org/get?q=FUZZ"
```

Scan with JSON export:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --json report.json
```

Custom thread count:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --threads 5
```

Custom timeout:

```bash
py main.py "https://httpbin.org/get?q=FUZZ" --timeout 10
```

Custom payload file:

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

## JSON Report

The tool can export scan results into a JSON file.

The report includes:

- target URL
- payload file
- thread count
- timeout
- tested payload count
- suspicious response count
- tested payloads
- generated URLs
- HTTP status codes
- response sizes
- response times
- findings
- errors

## Configuration

Detection thresholds and default values are stored in `config.py`.

The project includes configurable values such as:

- `FUZZ` marker
- default payload file
- default timeout
- default thread count
- suspicious status codes
- slow response threshold
- large response threshold

## Disclaimer

This tool is intended for educational purposes and API security testing only.