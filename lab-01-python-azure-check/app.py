import sys
import datetime
import urllib.request
import json

def check_azure_status():
    """Fetches public status info or performs a lightweight connectivity check."""
    print("==================================================")
    print("      Azure Cloud Health & Automation Check       ")
    print("==================================================")
    print(f"Timestamp: {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    
    target_url = "https://status.azure.com"
    
    try:
        req = urllib.request.Request(
            target_url, 
            headers={'User-Agent': 'Python-Cloud-Monitor/1.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()
            print(f"[SUCCESS] Azure Status Page Ping: HTTP {status_code}")
            print(f"[INFO] Endpoint reachable: {target_url}")
            return True
    except Exception as e:
        print(f"[ERROR] Failed to reach Azure status endpoint: {e}")
        return False

def generate_report(status_ok):
    """Outputs a clean summary dictionary representing automated health checks."""
    report = {
        "environment": "Dev/Local",
        "service": "Azure Connectivity Monitor",
        "status": "PASS" if status_ok else "FAIL",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    }
    
    print("\nGenerated Execution Report:")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    success = check_azure_status()
    generate_report(success)
    sys.exit(0 if success else 1)