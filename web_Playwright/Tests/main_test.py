import os

import pytest
from playwright.sync_api import sync_playwright, Page
from web_Playwright.Pages.home_page import HomePage
from dotenv import load_dotenv

load_dotenv()


def test_login_success(page: Page):
    login_page = HomePage(page)
    login_page.goto("https://kbl.or.kr/")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    login_page.login(email, password)
