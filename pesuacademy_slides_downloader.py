from playwright.sync_api import sync_playwright
import os
import re

def sanitize(name: str):
    return re.sub(r"[^\w\- ]", "", name).strip()


def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Open PESU Academy login page
        page.goto("https://www.pesuacademy.com/Academy/")

        # 2. Enter username and password
        page.fill("#j_scriptusername", username)
        page.fill("input[name='j_password']", password)

        # 3. Click login button
        page.click("button.btn.btn-lg.btn-primary.btn-block")

        # 4. Wait for logged-in UI to load
        page.wait_for_load_state("networkidle")

        # Keep window open a moment
        page.wait_for_timeout(5000)


if __name__ == "__main__":
    main()




