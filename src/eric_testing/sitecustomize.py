import os
import subprocess
import sys

# Only run this once
MARKER_FILE = os.path.join(os.path.dirname(__file__), ".playwright_installed")
if not os.path.exists(MARKER_FILE):
    print("\n=== Installing Playwright dependencies ===")
    try:
        print("Installing Playwright browsers...")
        subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

        print("\nInstalling Playwright system dependencies...")
        subprocess.run([sys.executable, "-m", "playwright", "install-deps"], check=True)
        print("=== Playwright setup completed successfully ===\n")
        
        # Create marker file to avoid running again
        with open(MARKER_FILE, "w") as f:
            f.write("Playwright dependencies installed")
    except Exception as e:
        print(f"\nError during Playwright setup: {e}", file=sys.stderr)
        print("You may need to run 'playwright install' and 'playwright install-deps' manually after installation")