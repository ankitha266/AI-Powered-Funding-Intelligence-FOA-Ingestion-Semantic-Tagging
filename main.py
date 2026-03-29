import argparse
import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# --- CORE LOGIC ---
def scrape_foa(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {
            "foa_id": "ISSR-2026-TEST",
            "title": soup.title.string.strip() if soup.title else "FOA Title",
            "agency": "Foundations/Agencies",
            "description": soup.get_text()[:1000].lower(),
            "source_url": url
        }
        return data
    except Exception as e:
        return None

def apply_tags(text):
    tags = []
    if "health" in text: tags.append("Public Health")
    if "science" in text: tags.append("STEM")
    return tags

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--out_dir", required=True)
    args = parser.parse_args()

    if not os.path.exists(args.out_dir): os.makedirs(args.out_dir)
    
    res = scrape_foa(args.url)
    if res:
        res["tags"] = apply_tags(res["description"])
        # Save JSON
        with open(os.path.join(args.out_dir, "foa.json"), 'w') as f:
            json.dump(res, f, indent=4)
        # Save CSV
        pd.DataFrame([res]).to_csv(os.path.join(args.out_dir, "foa.csv"), index=False)
        print(f"DONE! Files created in {args.out_dir}")

# --- RUNNING THE COMMAND ---
!pip install beautifulsoup4 requests pandas
!python main.py --url "https://www.nsf.gov" --out_dir ./out
