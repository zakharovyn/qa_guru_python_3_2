from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function')
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://www.google.com/')
    yield
    browser.quit()
