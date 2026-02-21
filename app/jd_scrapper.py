from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


KEYWORDS = [
    "job description",
    "about the job",
    "about the role",
    "role overview",
    "responsibilities",
    "what you'll do",
    "what you will do",
    "position summary",
]


def extract_job_description(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_load_state("networkidle")

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "lxml")
    print(soup)

    # Remove noise
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    # Search for heading tags
    headings = soup.find_all(["h1", "h2", "h3", "h4", "strong"])

    for heading in headings:
        text = heading.get_text(strip=True).lower()

        if any(keyword in text for keyword in KEYWORDS):
            # Collect sibling content after heading
            content = []
            for sibling in heading.find_next_siblings():
                if sibling.name in ["h1", "h2", "h3", "h4"]:
                    break  # Stop at next section
                content.append(sibling.get_text(separator="\n"))

            extracted = "\n".join(content).strip()

            print(extracted)

            if len(extracted) > 300:
                return extracted

    # Fallback if no heading match
    #return soup.get_text(separator="\n").strip()

extract_job_description("https://www.naukri.com/job-listings-big-data-engineer-techno-comp-tci-gurugram-bengaluru-7-to-9-years-050226011019?src=jobpromo-showcase")
