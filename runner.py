from selenium import webdriver
from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
from scenario_executor import run_scenario
from yaml_parser import parse_section

driver = None


def get_driver():
    global driver
    if not driver:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1360,1020')
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options.to_capabilities())
    browser.set_driver(driver)
    return driver


scenario = parse_section("Scenario")
run_scenario(scenario)
