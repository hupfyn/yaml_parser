from selene import by, browser
from time import sleep


def open_url(element):
    browser.open_url(element)


def check_element(element):
    element = element.popitem()
    browser.element(locator_type[element[0]](element[1])).is_displayed()


def input_data(element):
    value = element.pop('value')
    append = element.pop('append') if 'append' in element.keys() else False
    locator = element.popitem()
    if not append:
        browser.element(locator_type[locator[0]](locator[1])).clear()
    browser.element(locator_type[locator[0]](locator[1])).type(value)


def click_element(element):
    element = element.popitem()
    browser.element(locator_type[element[0]](element[1])).click()


def execute_js(element):
    value = element.pop('value')
    browser.execute_script(value)


def check_is_page_load():
    for _ in range(1200):
        if browser.execute_script('return document.readyState === "complete" && performance.timing.loadEventEnd > 0'):
            break
        sleep(0.1)


locator_type = {
    "xpath": by.xpath,
    "css": by.css,
    "name": by.name,
    "link_text": by.link_text,
    "id": by.id,
    "text": by.text
}
