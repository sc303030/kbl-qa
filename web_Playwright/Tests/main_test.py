import os

import pytest
from playwright.sync_api import sync_playwright, Page
from web_Playwright.Pages.home_page import HomePage
from web_Playwright.Pages.draw_page import DrawPage
from dotenv import load_dotenv

from web_Playwright.Pages.record_page import RecordPage

load_dotenv()


def test_login_success(page: Page):
    home_page = HomePage(page)
    record_page = RecordPage(page)
    home_page.goto("https://kbl.or.kr/")

    home_page.click_menu("link", "기록")
    record_page.click_sub_menu("link", "팀기록")
