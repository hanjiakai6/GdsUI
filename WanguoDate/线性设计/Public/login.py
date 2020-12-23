import time
def login(driver,username,password):
    driver.find_element_by_xpath('//*[@placeholder="请输入用户名/手机号/注册邮箱"]').send_keys(username)
    driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="primary-button"]').click()
    time.sleep(1)