from playwright.sync_api import sync_playwright

EDGE_PATH = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
EDGE_PROFILE = "/Users/anubhavmisra/Project/edge-playwright-profile"

JD_SELECTORS = [
    "div.jobs-box__html-content",     # ✅ NEW LinkedIn layout (your screenshot)
    "section.jobs-description",       # fallback
    "div.jobs-description__content",  # old layout
]

def fetch_linkedin_jd(url: str) -> str:
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=EDGE_PROFILE,
            executable_path=EDGE_PATH,
            headless=False,
        )

        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Let React hydrate
        page.wait_for_timeout(3000)

        for selector in JD_SELECTORS:
            try:
                page.wait_for_selector(selector, timeout=5000)
                text = page.inner_text(selector)
                #print(text)
                if text and len(text) > 200:
                    context.close()
                    return text
            except:
                pass

        context.close()
        raise RuntimeError(
            "❌ Could not locate job description. "
            "Make sure you are logged into LinkedIn."
        )
    
#fetch_linkedin_jd("https://www.linkedin.com/jobs/view/4355340409/?trk=eml-email_job_alert_digest_01-primary_job_list-0-jobcard_body_1736776066&refId=cvMTV1nGzT2U4RmHRWY4NA%3D%3D&trackingId=n%2BIq1%2Fh1t%2BOxSHnCnX5pjQ%3D%3D")