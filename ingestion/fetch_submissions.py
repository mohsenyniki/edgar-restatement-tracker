import argparse
import sys
from pathlib import Path

from sec_client import SECError, fetch_json, get_user_agent, normalize_cik, save_json

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "data" / "raw" / "submissions"
URL = "https://data.sec.gov/submissions/CIK{cik}.json"
PAGE_URL = "https://data.sec.gov/submissions/{name}"

parser = argparse.ArgumentParser(description="Fetch company submissions from SEC EDGAR")
parser.add_argument("cik", help="CIK of the company to fetch submissions for")
args = parser.parse_args()

# any tool that fails raises; we print its message and exit 1 in one place
try:
    cik = normalize_cik(args.cik)
    user_agent = get_user_agent()
    data = fetch_json(URL.format(cik=cik), user_agent)
    paths = [save_json(data, OUT_DIR / f"CIK{cik}.json")]

    # only the newest ~1,000 filings are in the main file; older ones are in extra pages it lists
    for page in data["filings"]["files"]:
        page_data = fetch_json(PAGE_URL.format(name=page["name"]), user_agent)
        paths.append(save_json(page_data, OUT_DIR / page["name"]))
except (ValueError, SECError) as e:
    print(e, file=sys.stderr)
    sys.exit(1)

for path in paths:
    size_mb = path.stat().st_size / 1_000_000
    print(f"Saved {path.relative_to(REPO_ROOT)} ({size_mb:.1f} MB)")
