from selenium import webdriver

# from selenium import webdriver
#
# mobile = {'deviceName': 'iPhone X'}
# # path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobile)
# driver = webdriver.Chrome(options=options)
# driver.get('http://www.baidu.com')
# # driver.find_element_by_css_selector('#index-kw').send_keys('test')

import requests,json

def get_cookies():

    res = requests.session()
    url = "http://10.110.152.175:9104/smart-sso-server/login"
    payload='backUrl=http%3A%2F%2F10.110.152.171%3A30080%2F&random=789&account=testanswer1&password=test_123&captcha=1111'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = res.request("POST", url, headers=headers, data=payload,allow_redirects=False)
    location_data = response.headers['Location']
    param_data = location_data.split('=')[-1]
    req_url = 'http://10.110.152.171:30081/user/login?__vt_param__={}'.format(param_data)
    user_response = res.request('POST',req_url)
    cookies = user_response.headers['Set-Cookie']
    return cookies

if __name__ == '__main__':
    print(get_cookies())





