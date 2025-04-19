

from playwright.async_api import expect
import pytest
import time
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.parametrize("email","password",[("sunny@co","123"),("sudfsf@co","1wrfw23")])
def test_first(set_up):

    page=set_up
    # page.pause()
    page.wait_for_load_state('networkidle')
    page.wait_for_load_state('domcontentloaded')
    # expect(page.get_by_text("omayo (QAFox.com)")).to_be_visible()

    # ---------------------



# with sync_playwright() as playwright:
#     run(playwright)
