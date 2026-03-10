# 🔍 Mobile API Recon Engine (NovaSniffer)

A high-performance traffic interception tool designed for Reverse Engineering mobile applications. It automates the discovery of private API endpoints and hidden authentication signatures that are often bypassed by traditional web scrapers.



## 🛠️ Key Features
* **Live Interception:** Captures real-time HTTP/HTTPS traffic using `mitmproxy` architecture.
* **Auth-Token Sniffing:** Automatically identifies and logs `Authorization`, `X-API-Key`, and custom session headers.
* **Payload Analysis:** Parses JSON responses on-the-fly to reconstruct API documentation for bot development.
* **Filter Logic:** Specialized keyword filtering (e.g., 'api', 'v1', 'graphql') to eliminate background noise.

## 📈 Use Cases
- **Bot Development:** Finding the "hidden" mobile APIs for sites like Fragment, Instagram, or Telegram.
- **Security Auditing:** Analyzing app traffic for data leaks or insecure endpoint exposure.
- **Competitive Intel:** Understanding how third-party apps structure their data requests.

## 🚀 Setup & Usage
```bash
pkg install python-cryptography
pip install mitmproxy
mitmdump -s proxy_sniffer.py
