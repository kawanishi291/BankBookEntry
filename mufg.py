import time, datetime, calendar
from Info import Info
from setdriver import SetDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def DLfromMUFG():

    driver = SetDriver()
    info = Info()
    URL = info.get('MUFG', 'URL')
    TX_BRANCH_NUM = info.get('MUFG', 'TX_BRANCH_NUM')
    TX_ACCOUNT_NUM = info.get('MUFG', 'TX_ACCOUNT_NUM')
    TX_CONTRACT_NUM = info.get('MUFG', 'TX_CONTRACT_NUM')
    NAME = info.get('MUFG', 'MY_NAME')

    driver.get(URL)
    # 3秒待機
    time.sleep(3)
    try:
        login_name = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div[1]/div/span")
    except NoSuchElementException:
        pass
        # 店番を入力
        tx_branch_number = driver.find_element(By.XPATH, "/html/body/div[1]/main/form/section/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/input")
        tx_branch_number.clear()
        tx_branch_number.send_keys(TX_BRANCH_NUM)
        # 0.5秒待機
        time.sleep(0.5)
        # 口座番号を入力
        tx_account_number = driver.find_element(By.XPATH, "/html/body/div[1]/main/form/section/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/input")
        tx_account_number.clear()
        tx_account_number.send_keys(TX_ACCOUNT_NUM)
        # 0.5秒待機
        time.sleep(0.5)
        # ログインパスワードを入力
        tx_contract_number = driver.find_element(By.XPATH, "/html/body/div[1]/main/form/section/div/div/div[1]/div[2]/div[2]/div/input")
        tx_contract_number.clear()
        tx_contract_number.send_keys(TX_CONTRACT_NUM)
        # 0.5秒待機
        time.sleep(0.5)
        # 次へボタンをクリック
        next_btn = driver.find_element(By.XPATH, "/html/body/div[1]/main/form/section/div/div/div[1]/div[3]/div/button")
        next_btn.click()
        # 1秒待機
        time.sleep(1)
        login_name = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div[1]/div/span")

    if login_name.text != NAME + "さま":
        driver.quit()

    # 入出金明細ボタンをクリック
    detail_btn = driver.find_element(By.XPATH, "/html/body/div[1]/main/form/section/div/div[1]/div/div[2]/section[1]/a/div[2]/div/p")
    detail_btn.click()
    # 1秒待機
    time.sleep(1)
    # 明細をダウンロードボタンをクリック
    download_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td/a/img")
    download_btn.click()
    # 1秒待機
    time.sleep(1)

    # 前月の21日〜今月20日で取得
    now = datetime.date.today()
    if now.month == 1:
        prev_year = now.year - 1
        prev_month = 12
    else:
        prev_year = now.year
        prev_month = now.month - 1
    last = calendar.monthrange(prev_year, prev_month)[1]
    
    str_y_dd = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form[2]/div[2]/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div[2]/div/div[1]/div/span[1]/select[1]')
    select = Select(str_y_dd)
    select.select_by_visible_text(str(prev_year))
    end_y_dd = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form[2]/div[2]/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div[2]/div/div[2]/div/span[1]/select[1]')
    select = Select(end_y_dd)
    select.select_by_visible_text(str(prev_year))
    str_m_dd = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form[2]/div[2]/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div[2]/div/div[1]/div/span[1]/select[2]')
    select = Select(str_m_dd)
    select.select_by_visible_text(str(prev_month))
    end_m_dd = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form[2]/div[2]/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div[2]/div/div[2]/div/span[1]/select[2]')
    select = Select(end_m_dd)
    select.select_by_visible_text(str(prev_month))
    str_d_dd = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form[2]/div[2]/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div[2]/div/div[1]/div/span[1]/select[3]')
    select = Select(str_d_dd)
    select.select_by_visible_text("1")
    end_d_dd = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form[2]/div[2]/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div[2]/div/div[2]/div/span[1]/select[3]')
    select = Select(end_d_dd)
    select.select_by_visible_text(str(last))
    # 1秒待機
    time.sleep(1)

    # ダウンロード（CSV形式）ボタンをクリック
    download_csv_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form[2]/div[2]/div[2]/div[1]/button/img")
    download_csv_btn.click()
    # 3秒待機
    time.sleep(3)
    # ログアウトをクリック
    logout_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form[2]/div[1]/div[2]/ul/li[3]/a")
    logout_btn.click()
    # 1秒待機
    time.sleep(1)

    driver.quit()
