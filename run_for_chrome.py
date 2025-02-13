from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pygetwindow as gw
import time

UserName='root'
# Chrome 브라우저용 옵션 설정 (필요에 따라 조정)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data".format(UserName))

# 웹 드라이버 설정
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# 주어진 URL 열기
url = "https://draft.blogger.com/blog/posts/556890584458197932"
driver.get(url)

########## 작업 수행 ##########

time.sleep(4)

saveOnly = True
count='01'
myTitle="test 제목입니다 2025-02-12 " + count
myTags="태그1,태그2"
myDescription="TEST 설명글 입니다 2025-02-12 " + count
myLink="test-link-2025-02-12 " + count
myBody="""<p><strong>테스트 본문</strong>입니다.<br />
2025-02-12 {} 째 테스트.
</p>""".format(count)

# 키보드 이벤트로 텍스트 입력
actions = webdriver.ActionChains(driver)
idx = 0

def input_string(strings):
    actions.send_keys(strings).perform()
    time.sleep(1)

def input_click(x,y):
    global idx
    #script = f"document.elementFromPoint({x}, {y}).click();"
    #driver.execute_script(script)
    actions.move_by_offset(x, y).click().perform()
    idx += 1
    time.sleep(0.5)
    actions.move_by_offset(-x, -y).perform()
    time.sleep(0.5)

def input_rclick(x,y):
    global idx
    #script = f"document.elementFromPoint({x}, {y}).click();"
    #driver.execute_script(script)
    actions.move_by_offset(x, y).context_click().perform()
    idx += 1
    time.sleep(0.5)
    actions.move_by_offset(-x, -y).perform()
    time.sleep(0.5)

         #side #new #title #tag #loca   #desc     #link   #fmt #body #publish
click_x = [ 36,  85,  47, 726,  726,740, 726,726, 726,720,  23, 256, 900,554 ]
click_y = [ 31, 143, 123, 258,  592,465, 800,524, 335,500, 176, 266, 110,508 ]

# side menu open 1
# 사이드메뉴
time.sleep(5)
myXpath = '/html/body/div[8]/div[2]/header/div[2]/div[1]/div[1]'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)

# new post 1
# 새 글 쓰기버튼
myXpath = '/html/body/div[8]/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[3]/div/div/div[2]'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)

# title 1
# 제목
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[1]/div[1]/div[1]/div/div[1]/input'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)
##### INPUT #####
input_string(myTitle)

# tags 1
# 라벨 입력창
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[1]/span/div/div[1]/div[1]/div[2]/textarea'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)
##### INPUT #####
input_string(myTags)

#글설정버튼# /html/body/div[8]/c-wiz/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[2]/div/div/span/span/span
#if element.is_displayed() and element.is_enabled():

# location 3
# 위치
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[4]'
element = driver.find_element(By.XPATH,myXpath)
for i in range(10):
    if element.is_enabled(): break
    time.sleep(0.5)

xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)

# 위치 입력
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[4]/span/div/div[2]/div/div[1]/div/div[1]/input'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)
input_string("Seoul")

# 돋보기
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[4]/span/div/div[2]/div/div[1]/div/span/div/span/span/span'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(0.5)
##### INPUT #####
actions.send_keys(Keys.ENTER).perform()
time.sleep(0.5)

# Description  2
# 검색 설명
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[5]/div/span/div/div'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)

# 검색 설명 입력창
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[5]/span/div/div/div[1]/div[2]/textarea'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)
##### INPUT #####
input_string(myDescription)
time.sleep(1)

# link 3 <tab> <paste>
# 퍼머링크
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/div/span/div/div'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)

# 맞춤 라디오
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/span/div[1]/div[1]/span/div/div[2]/div[1]/div[3]/div'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(0.5)

# 링크 입력
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/span/div[1]/div[2]/div/div/div[1]/div/div[1]/input'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(0.5)
##### INPUT #####
input_string(myLink)
#actions.send_keys(Keys.TAB).perform()


# input type 2 <UP> <ENTER>
isHtmlFmt = True
# 본문 작성 형식 콤보 열기
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)
if isHtmlFmt:
    # HTML 보기
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/span'
else:
    # 새글작성 보기
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/span'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)

# input Body 1
# 본문
myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[2]/div/div/div/div[6]/div[1]/div/div/div/div[5]/div/pre'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(1)
##### INPUT #####
input_string(myBody)


# 저장만 할 지, 게시할지 의 분기
if saveOnly:
        # 저장하기 메뉴 열기 화살표
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[1]/div[2]/div[3]/span/span/span'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(1)
    # 저장
    myXpath = '/html/body/div[8]/c-wiz[2]/div[2]/div/div/span[2]/div[3]/div'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(1)
    # 뒤로가기 버튼
    myXpath = '/html/body/div[8]/div[2]/header/div[2]/div[1]/div[2]/svg/path'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(1)
else:
    # 게시 버튼
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[1]/div[2]/div[4]/span'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(1)
    # 확인 버튼
    myXpath = '/html/body/div[8]/div[4]/div/div[2]/div[3]/div[2]/div[2]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(1)


  
time.sleep(5)
driver.quit()
exit()
