from selenium import webdriver

def before_all(context):
    context.DRIVER = webdriver.Chrome()
    context.DRIVER.maximize_window()

def after_all(context):
    context.DRIVER.close()
