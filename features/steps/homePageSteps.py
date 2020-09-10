from behave import given, then
from selenium.webdriver.chrome import webdriver


@given('I navigate to the Standprof web site')
def step_impl(context):
    context.DRIVER.get('https://standprof.co.uk')


@then('the Home page should show a section with the title: "Our top services"')
def step_impl(context):
    el = context.DRIVER.find_elements_by_tag_name("h2")[0].text
    assert el == "OUR TOP SERVICES"

