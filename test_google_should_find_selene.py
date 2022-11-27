from selene.support.shared import browser
from selene import have, be


def test_google_search_selene(open_browser):

    browser.element('[name=q').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_search_invalid_request(open_browser):

    browser.element('[name=q').should(be.blank).type('jispdjgisdfjgjghdsgsl').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу jispdjgisdfjgjghdsgsl ничего не найдено.'))
