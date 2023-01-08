import time
from Info import Info
from setdriver import SetDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def DLfromAuPayCard():

    driver = SetDriver()
    info = Info()
    URL = info.get('AU_PAY', 'URL_AUPAY_CARD')
    ID = info.get('AU_PAY', 'MY_ID')
    PASS = info.get('AU_PAY', 'PASS')
    NAME = info.get('AU_PAY', 'MY_NAME')

    driver.get(URL)
    # 1秒待機
    time.sleep(1)
    try:
        login_name = driver.find_element(By.XPATH, "/html/body/form[1]/div[2]/div/span[1]")
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
            login_name = driver.find_element(By.XPATH, '//*[@id="idArea"]')
        except NoSuchElementException:
            pass
            driver.quit()

            return False
    
    if login_name.text != NAME + "さま":
        driver.quit()

    # 明細確認ボタンをクリック
    nablarch_form2_2_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[2]/div[1]/p[2]/span/a")
    nablarch_form2_2_btn.click()
    # 1秒待機
    time.sleep(1)
    # ご利用履歴をダウンロードする(CSV)ボタンをクリック
    nablarch_form3_101_btn = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/form/div[12]/div[3]/div[2]/button")
    nablarch_form3_101_btn.click()
    # 3秒待機
    time.sleep(3)
    # ログアウトをクリック
    nablarch_form5_1 = driver.find_element(By.XPATH, "//*[@id='footer']/ul[2]/li[3]/a")
    nablarch_form5_1.click()
    # 1秒待機
    time.sleep(1)

    driver.quit()
    return True