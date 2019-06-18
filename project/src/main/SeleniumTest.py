"""
    Selenium
    自动测试工具，支持多种浏览器。爬虫中主要用来解决javascript渲染问题

    https://selenium-python.readthedocs.io/api.html
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait  import WebDriverWait
import time
from selenium.webdriver import  ActionChains

brower = webdriver.Chrome()
# 基本使用
if 1==0:
    try:
        brower.get('http://www.baidu.com')
        input = brower.find_element_by_id('kw')
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(brower, 10)
        wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
        
        print(brower.current_url)
        print(brower.get_cookies())
        print(brower.page_source)
    finally:
        brower.close()
    
# 声明浏览器对象
if 1==0:
    brower = webdriver.Chrome()
    brower = webdriver.Firefox()
    brower = webdriver.Edge()
    brower = webdriver.PhantomJS()
    brower = webdriver.Opera()

# 访问页面
if 1==0:
    brower.get('http://bilibili.com')
    print(brower.page_source)
    brower.close()

# 查找元素



# 单个元素
if 1==0:
    brower.get('http://www.taobao.com')
    input_first = brower.find_element_by_id('q')
    input_second = brower.find_element_by_css_selector('#q')
    input_third = brower.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)

    # 通用方法,指定查找的方式
    input = brower.find_element(By.ID, 'q')
    print(input)

    brower.close()

# 多个元素
if 1==0:
    brower.get('http://www.taobao.com')
    lis = brower.find_elements_by_css_selector('.service-bd li')
    lis = brower.find_elements(By.CSS_SELECTOR, '.service-bd li')
    print(lis)
    brower.close()

'''
    元素交互操作
    对获取的元素调用交互方法
'''
if 1==0:
    brower.get('http://www.taobao.com')
    input = brower.find_element_by_id('q')
    input.send_keys('mi')
    time.sleep(1)
    input.clear()
    input.send_keys('pad')
    button =brower.find_element_by_class_name('btn-search')
    button.click()

# api文档 https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement

'''
    交互动作
    将动作附加到动作链中串行执行
'''
if 1==0:
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    brower.get(url)
    # 选择指定iframe
    brower.switch_to.frame('iframeResult')
    source = brower.find_element_by_css_selector('#draggable')
    target = brower.find_element_by_css_selector('#droppable')
    # 声明动作链
    actions = ActionChains(brower)
    # 声明拖拽对象
    actions.drag_and_drop(source, target)
    # 执行动作
    actions.perform()

# 执行Javascript
if 1==0:
    brower.get('http://www.zhihu.com/explore')
    brower.execute_script('window.scrollTo(100, 500)')
    brower.execute_script('alert("Scroll To loaction")')

    time.sleep(2)

# 获取元素信息

if 1==0:
    url = 'http://www.zhihu.com/explore'
    brower.get(url)
    # 获取属性
    logo = brower.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))

    # 获取文本值
    input = brower.find_element_by_id('zu-top-add-question')
    print(input.text)

    # 获取ID、位置、标签名、大小
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)

# Frame
from  selenium.common.exceptions import NoSuchElementException
if 1==0:
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    brower.get(url)
    # 选择指定iframe
    brower.switch_to.frame('iframeResult')
    source = brower.find_element_by_css_selector('#draggable')
    print(source)
    try:
        # 子frame不能查找父frame
        logo = brower.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('no logo')
    # 选择回父frame
    brower.switch_to.parent_frame()
    logo = brower.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)

# 等待

# 隐形等待
#   当使用隐形等待执行测试时，如果WebDriver没有在DOM中找到元素，将继续等待，超出指定时间后则抛出异常
if 1==0:
    brower.implicitly_wait(2)
    brower.get('https://www.zhihu.com/explore')
    input = brower.find_element_by_class_name('zu-top-add-question')
    print(input)

# 显示等待
#  在等待时间内找到元素，则不再等待
if 1==0:
    brower.get('http://www.taobao.com')
    wait = WebDriverWait(brower, 10)
    # 直到有id为q的元素
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

# 前进后退
if 1==0:
    brower.get('http://bilibili.com')
    brower.get('http://www.taobao.com')
    brower.back()
    time.sleep(1)
    brower.forward()
    brower.close()

# Cookies
if 1==0:
    brower.get('http://www.zhihu.com/explore')
    print(brower.get_cookies())
    brower.add_cookie({'name': 'lov', 'domain': 'www.zhihu.com', 'value': 'ge'})
    print(brower.get_cookies())
    brower.delete_all_cookies()
    print(brower.get_cookies())

# 选项卡管理（浏览器标签页）
if 1==1:
    brower.execute_script('window.open()')
    print(brower.window_handles)
    brower.switch_to_window(brower.window_handles[1])
    brower.get('http://www.taobao.com')
    time.sleep(1)
    brower.switch_to_window(brower.window_handles[0])
    brower.get('http://python.org')


# 异常处理
