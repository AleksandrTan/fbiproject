from seleniumwire import webdriver  # Import from seleniumwire
import time

cookie_data = dict()
request_data = dict()


def interceptor(request):
    global cookie_data, request_data
    try:
        new = request.headers["Cookie"].split(';')
        for new_one in new:
            cooka = new_one.split('=')
            cookie_data[cooka[0].strip()] = cooka[1].strip()
    except AttributeError as error:
        pass

    # print(request.response, request.response.headers, 9000)


def cel_test():
    # Create a new instance of the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=10x10")
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    # Go to the Google home page
    driver.get('https://www.instagram.com/')
    time.sleep(10)
    username_field = driver.find_element_by_name('username')
    password_field = driver.find_element_by_name('password')
    submit_elem = driver.find_element_by_tag_name('button')
    username_field.send_keys('Rumych423')
    password_field.send_keys('ufeltfvec')
    submit_elem.click()
    driver.request_interceptor = interceptor
    request = driver.wait_for_request('https://www.instagram.com/accounts/login/ajax/')
    # print('-' * 50)
    # print(request.body, request.headers, request.querystring, 80001)
    # print('-' * 50)
    # print('* response' * 50)
    # print(request.response, request.response.headers, 9000)
    # print('* response' * 50)
    driver.close()


def interceptors(request):
    new = request.split(';')
    for new_one in new:
        cooka = new_one.split('=')
        cookie_data[cooka[0].strip()] = cooka[1].strip()


if __name__ == "__main__":
    cel_test()
    # interceptors('ig_did=B91C7788-E98A-40B2-98AF-724AC3478E66; csrftoken=WR7lYPo8yqKEWm70LIyX3LOweeBCX7Tl; mid=YD-cuwAEAAEWApZhH4MWwDSfq3S1; ig_nrcb=1')
    # interceptors('ig_did = F9F67137-2DA0-4FEB-A833-EEC9D68448A0; mid = YD-IRgAEAAF1UYkqRcwKclovX10N; ig_nrcb = 1; '
    #              'csrftoken = rOED961EwEVQoGAYF3riB8IlceaPcwrT; rur = VLL; ds_user_id = 45540342156; sessionid = 45540342156%3ArqInnVMfB45gbx%3A21')
    print(cookie_data)