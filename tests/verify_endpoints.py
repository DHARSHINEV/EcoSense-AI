import urllib.request
import json
import sys

endpoints = [
    '/health',
    '/api/building/summary',
    '/api/zones',
    '/api/energy',
    '/api/occupancy',
    '/api/forecast',
    '/api/recommendations',
    '/api/comparison',
    '/api/deployment'
]

frontend_routes = [
    '/',
    '/dashboard',
    '/zones',
    '/scenarios',
    '/simulation',
    '/deployment',
    '/limitations'
]

print("=== VERIFYING FASTAPI BACKEND (http://127.0.0.1:8000) ===")
backend_failures = 0
for ep in endpoints:
    url = f"http://127.0.0.1:8000{ep}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=5) as response:
            status = response.getcode()
            body = response.read().decode('utf-8')
            data = json.loads(body)
            preview = list(data.keys()) if isinstance(data, dict) else f"list({len(data)})"
            print(f"PASS [{status}] {ep} -> {preview}")
    except Exception as e:
        print(f"FAIL {ep} -> {e}")
        backend_failures += 1

print("\n=== VERIFYING FRONTEND ROUTES (http://localhost:3000) ===")
frontend_failures = 0
for route in frontend_routes:
    url = f"http://localhost:3000{route}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as response:
            status = response.getcode()
            print(f"PASS [{status}] {route}")
    except Exception as e:
        print(f"FAIL {route} -> {e}")
        frontend_failures += 1

print(f"\nSummary: Backend failures: {backend_failures}, Frontend failures: {frontend_failures}")
sys.exit(backend_failures + frontend_failures)
