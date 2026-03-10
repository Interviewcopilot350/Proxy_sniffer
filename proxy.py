from mitmproxy import http
import json

# --- NOVA BOTS: API DISCOVERY ENGINE ---
# Use Case: Finding hidden API endpoints in mobile apps 
# during the Reverse Engineering phase.

class TrafficSniffer:
    def __init__(self):
        self.target_keyword = "api" # Filter for API calls only
        print("[*] Nova Sniffer Active. Intercepting traffic...")

    def request(self, flow: http.HTTPFlow) -> None:
        # Check if the URL contains our target keyword
        if self.target_keyword in flow.request.pretty_url:
            print(f"\n[+] INTERCEPTED: {flow.request.method} {flow.request.pretty_url}")
            
            # Print Headers - This is where the 'Secret' Auth keys are hidden
            if "Authorization" in flow.request.headers:
                print(f" [!] AUTH KEY FOUND: {flow.request.headers['Authorization'][:30]}...")

    def response(self, flow: http.HTTPFlow) -> None:
        # If the response is JSON, we log it to analyze the data structure
        if "application/json" in flow.response.headers.get("Content-Type", ""):
            try:
                data = json.loads(flow.response.get_text())
                print(f" [✓] DATA STRUCTURE: {list(data.keys())}")
            except Exception:
                pass

addons = [TrafficSniffer()]
