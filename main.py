"""The funniest final text a dying phone sends at one percent battery, under 200 characters."""

import os

TEXT = "Tell the charger I loved it. Tell the cloud I never backed up. And tell my owner I saw everything — I forgive the toilet drops."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
