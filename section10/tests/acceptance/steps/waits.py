from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators


use_step_matcher('re')


@given('I wait for the posts to load')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_all_elements_located(BlogPageLocators.POSTS_SECTION)
    )