"""
A profile directory is where the browser stores your data, like:

Login sessions (cookies)

Saved logins

Local storage

Site permissions

Cache

For Edge / Chrome, this is not the browser app itself — it’s a folder on disk.

Your main Edge profile (used by normal Edge):

/Users/anubhavmisra/Library/Application Support/Microsoft Edge


Inside it you’ll see:

Default/
Profile 1/
Profile 2/


Each of those is a profile directory.

created a seperate profile directory because the existing edge profile is used in the opened edge tab and hence chromium blocked
playwright so created deadicated profile just for playwright
"""

from playwright.sync_api import sync_playwright


EDGE_PATH = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
PROFILE = "/Users/anubhavmisra/Project/edge-playwright-profile"

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE,
        executable_path=EDGE_PATH,
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled"
        ]
    )
    page = context.new_page()
    page.goto("https://www.linkedin.com")
    input("Log in manually, then press Enter...")
    context.close()