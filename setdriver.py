from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def SetDriver():

    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--disable-features=VizDisplayCompositor')
    # プロファイルの保存先を指定
    options.add_argument("--user-data-dir=/Users/kawanishishoutarou/Library/Application Support/Google/Chrome/")
    # 使用するプロファイルを指定
    options.add_argument("--profile-directory=Default")
    # スクリプトが保存されているフォルダ（os.getcwd()）をファイルのダウンロード先に指定
    options.add_experimental_option("prefs", {"download.default_directory": "./data/" })                                              
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    return driver