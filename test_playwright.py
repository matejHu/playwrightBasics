from playwright.sync_api import Page

def test_button(page: Page):
    page.goto("http://www.uitestingplayground.com/textinput")

    input = page.locator("#newButtonName")

    input.fill("Vyplnění inputu")

    inputText = input.input_value()

    button = page.locator("#updatingButton")

    button.click()

    buttonText = button.inner_text()

    page.wait_for_timeout(2000)

    assert buttonText == inputText

def test_hide(page: Page):
    page.goto("http://www.uitestingplayground.com/visibility")

    button = page.locator("#hideButton")

    button.click()

    button2 = page.locator("#removedButton")

    page.wait_for_timeout(2000)

    assert button2.is_hidden() == True

def test_clicked(page: Page):
    page.goto("http://www.uitestingplayground.com/mouseover")

    clickA = page.locator("body > section > div > div:nth-child(7) > a")

    for i in range(3):
        clickA.click()

    page.wait_for_timeout(2000)

    counter = page.locator("#clickCount")

    assert counter.inner_text() == "3"
    