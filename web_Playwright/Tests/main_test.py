import os

import pytest
from playwright.sync_api import sync_playwright, Page
from web_Playwright.Pages.home_page import HomePage
from web_Playwright.Pages.draw_page import DrawPage
from dotenv import load_dotenv

load_dotenv()


def test_login_success(page: Page):
    login_page = HomePage(page)
    draw_page = DrawPage(page)
    login_page.goto("https://kbl.or.kr/")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    login_page.login(email, password)
    login_page.click_draw()
    draw_page.select_draw("KBL DRAW 92")
    draw_page.participate_draw()
