import datetime
import time

from selenium.common.exceptions import NoSuchFrameException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

# this function clicks on the given element
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utilities import base_driver


# this function clicks on the given element
def click(element: WebElement):
    element.click()


# this function sends the given text to the given element
def write_text(element: WebElement, text: str):
    element.send_keys(text)


# this function clears the  given element and send it the given text
def clear_and_write_text(element: WebElement, text: str):
    element.clear()
    element.send_keys(text)


# this function returns the text of the given element
def read_text(element: WebElement):
    return element.text


# this function moves the cursor over the given element
def move_to_element(element):
    action = ActionChains(base_driver.driver)
    action.move_to_element(element).perform()


# this function clicks on the element in the given list with the given value (if exists)
def click_radio_button_or_checkbox(list_elements: list, value: str):
    for elem in list_elements:
        if elem.is_enabled() and value.strip() == elem.get_attribute('value').strip():
            click(elem)


# This method checks if the text is found in the drop down element and only then select it
def select_drop_down_by_text(element: WebElement, text: str):
    select: Select = Select(element)
    options = select.options
    for elem in options:
        if text == elem.text:
            select.select_by_visible_text(text)


# This method checks if the index is valid and only then selects it
def select_drop_down_by_index(element: WebElement, index: int):
    select: Select = Select(element)
    options = select.options
    if 0 <= index < len(options):
        select.select_by_index(index)
    # select.first_selected_option()


# this function accepts the alert popup
def accept_alert():
    try:
        popup = base_driver.driver.switch_to.alert
        popup.accept()
    except NoAlertPresentException as e:
        print(e)


# this function dismisses the alert popup
def dismiss_alert():
    try:
        popup = base_driver.driver.switch_to.alert
        popup.dismiss()
    except NoAlertPresentException as e:
        print(e)


# this function switches focus to the given iframe
# param new_ifram is either iframe_id, iframe_index, or i_frame_element
def switch_to_frame(new_frame):
    try:
        base_driver.driver.switch_to.frame(new_frame)
    except NoSuchFrameException as e:
        print(e)


# this function switches focus to the given iframe
# param iframe_id to switch to
def switch_to_frame_by_id(frame_id: str):
    try:
        base_driver.driver.switch_to.frame(frame_id)
    except NoSuchFrameException as e:
        print(e)


# this function switches focus to the given iframe
# param iframe_index to switch to
def switch_to_frame_by_index(frame_index: int):
    try:
        base_driver.driver.switch_to.frame(frame_index)
    except NoSuchFrameException as e:
        print(e)


# this function switches focus to new window if only 2 windows are open
def switch_to_child_window():
    curr_win_handle = base_driver.driver.current_window_handle
    win_handles = base_driver.driver.window_handles
    for w in win_handles:
        if w != curr_win_handle:
            base_driver.driver.switch_to.window(w)
            break


# this function switches focus to  the newest window opened
# prev_open_windows the windows set before the opening of the new window
def switch_to_new_window(prev_open_windows):
    win_handles = base_driver.driver.window_handles
    for w in win_handles:
        if w not in prev_open_windows:
            base_driver.driver.switch_to.window(w)
            break


# This method sends the RETURN key to a given element.
def send_return_key(element: WebElement):
    element.send_keys(Keys.RETURN)


# returns a WebdriverWait instance
def get_wait_object():
    return WebDriverWait(base_driver.driver, 10)


# waits until the given by object is clickable
# returns a WebdriverWait instance
def wait_for_clickability(by_obj):
    return get_wait_object().until(ec.element_to_be_clickable(by_obj))


# waits until the given by object is visible
# returns a WebdriverWait instance
def wait_for_visibility(by_obj):
    return get_wait_object().until(ec.visibility_of_element_located(by_obj))


# waits until the given by object is clickable and click on the given element
# the given by_obj t is the has the same locator as the given elem
def wait_and_click(elem, by_obj):
    wait_for_clickability(by_obj)
    click(elem)


# sleeps for the given amount of seconds
def wait(seconds):
    time.sleep(seconds)


# This method will click on the element passed to it used by JavascriptExecutor
# param element to be clicked.
def js_click(element):
    base_driver.driver.execute_script("arguments[0].click()", element)


# This method will scroll the page until the element passed to it becomes visible.
def js_scroll_to_element(element):
    base_driver.driver.execute_script("arguments[0].scrollIntoView(true)", element)


# this method scrolls the page up in the given pixels_amount
def scroll_up(pixels_amount):
    script_str = "window.scrollBy(0,-" + str(pixels_amount) + ")"
    base_driver.driver.execute_script(script_str)


# this method scrolls the page up in the given pixels_amount
def scroll_down(pixels_amount):
    script_str = "window.scrollBy(0," + str(pixels_amount) + ")"
    base_driver.driver.execute_script(script_str)


# this method clicks on the first element in the given list with the given text
# example use: select date from a calendar
def select_element_from_list_by_text(elems_list, text):
    for elem in elems_list:
        if elem.is_enabled() and elem.text == text:
            elem.click()
        break


# this method returns the current timestamp as str
def get_time_stamp():
    return str(datetime.datetime.now())


# saves a screenshot as .png file,
# the target save directory should exist beforehand
def take_screen_shot():
    curr_timestamp = get_time_stamp()
    image = "./screen_shots/screen_" + curr_timestamp + ".png"
    base_driver.driver.get_screenshot_as_file(image)
