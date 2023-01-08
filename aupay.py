import time
from Info import Info
from setdriver import SetDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def DLfromAuPay():

    driver = SetDriver()
    info = Info()
    URL = info.get('AU_PAY', 'URL_AUPAY')
    ID = info.get('AU_PAY', 'MY_ID')
    PASS = info.get('AU_PAY', 'PASS')

    driver.get(URL)
    # 1秒待機
    time.sleep(1)
    try:
        login_num = driver.find_element(By.XPATH, "/html/body/div/header/div[2]/div[2]/dl/dd")
    except NoSuchElementException:
        pass
        # ログインIDを入力
        login_id = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/div/form/input[23]")
        login_id.clear()
        login_id.send_keys(ID)
        # 0.5秒待機
        time.sleep(0.5)
        # 次へボタンをクリック
        next_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/div/form/button[1]")
        next_btn.click()
        # 0.5秒待機
        time.sleep(0.5)
        # パスワードを入力
        password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/div/form/input[24]")
        password.send_keys(PASS)
        # 0.5秒待機
        time.sleep(0.5)
        # 次へボタンをクリック
        next_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/div/form/button[4]")
        next_btn.click()
        # 2秒待機
        # time.sleep(20)
        time.sleep(2)
        try:
            login_num = driver.find_element(By.XPATH, '/html/body/div/header/div[2]/div[2]/dl/dd')
        except NoSuchElementException:
            pass
            driver.quit()

            return False
    
    if login_num.text != ID:
        driver.quit()

    dropdown = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form[1]/div/select[1]')
    select = Select(dropdown)
    select.select_by_index(1)
    # 1秒待機
    time.sleep(1)
    # ダウンロードボタンをクリック
    nablarch_form2_2_btn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form[3]/span/a")
    nablarch_form2_2_btn.click()
    # 3秒待機
    time.sleep(3)
    # ログアウトをクリック
    nablarch_form5_1 = driver.find_element(By.XPATH, "/html/body/div/footer/div/nav/ul/li[4]/a")
    nablarch_form5_1.click()
    # 1秒待機
    time.sleep(1)

    driver.quit()
    return True