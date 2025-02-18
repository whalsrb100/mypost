#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time, sys, os, clipboard

UserName='root'

#            0            1           2            3
appList = ['itmoeyo','run-linux', 'issues', 'techforlinux']
appName = appList[0]

baseDir = '/root/mj/posts/{}'.format(appName)
post = sys.argv[1]
postDir = "{}/{}".format(baseDir,post)
titleFileName = '{}/title.txt'.format(postDir)
tagsFileName = '{}/tags.txt'.format(postDir)
descriptionFileName = '{}/description.txt'.format(postDir)
linkFileName = '{}/link.txt'.format(postDir)
bodyFileName = '{}/body.txt'.format(postDir)


if os.path.isfile("{}/registerd".format(postDir)):
    print("이미 등록 된 포스팅 입니다.")
    tmpList = []
    with open(linkFileName, 'r') as file_data:
        for line in file_data:  tmpList.append(line)
    myLink = ' '.join(tmpList).strip()
    print("URL: {}".format(myLink))
    tmpList.clear()
    exit()

isTest = False
saveOnly = False

isHeadless = False

# Chrome 브라우저용 옵션 설정 (필요에 따라 조정)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--user-data-dir=/root/.config/google-chrome_mj")
chrome_options.add_argument("--no-sandbox")
if isHeadless:
    chrome_options.add_argument("window-size=1920,1080");
    chrome_options.add_argument("--headless")


# 웹 드라이버 설정
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# 주어진 URL 열기
url_dict = {
    "run-linux":"https://draft.blogger.com/blog/posts/1800034663096054275",
    "issues":"https://draft.blogger.com/blog/posts/3142838807897126089",
    "itmoeyo":"https://draft.blogger.com/blog/posts/556890584458197932",
    "techforlinux":"https://techforlinux.com/wp-admin/post-new.php"
}
url = url_dict[appName]

driver.get(url)
driver.set_window_size(960, 1200)

########## 작업 수행 ##########
time.sleep(2)

if isTest:
    count='01'
    myTitle="test 제목입니다 2025-02-12 " + count
    myTags="태그1,태그2"
    myDescription="TEST 설명글 입니다 2025-02-12 " + count
    myLink="test-link-2025-02-12 " + count
    myBody="""<p><strong>테스트 본문</strong>입니다.<br />
2025-02-12 {} 째 테스트.
</p>""".format(count)
else:
    tmpList = []
    with open(titleFileName, 'r') as file_data:
        for line in file_data:  tmpList.append(line)
    myTitle = ' '.join(tmpList).strip()
    tmpList.clear()

    with open(tagsFileName, 'r') as file_data:
        for line in file_data:  tmpList.append(line)
    myTags = ' '.join(tmpList).strip()
    tmpList.clear()

    with open(descriptionFileName, 'r') as file_data:
        for line in file_data:  tmpList.append(line)
    myDescription = ' '.join(tmpList).strip()
    tmpList.clear()

    with open(linkFileName, 'r') as file_data:
        for line in file_data:  tmpList.append(line)
    myLink = ' '.join(tmpList).strip()
    tmpList.clear()

    with open(bodyFileName, 'r') as file_data:
    #    for line in file_data:  tmpList.append(line)
        myBody = file_data.read()
    #myBody = '\n'.join(tmpList).strip()
    #tmpList.clear()

# 키보드 이벤트로 텍스트 입력
actions = webdriver.ActionChains(driver)
idx = 0

def input_string(strings):
    clipboard.copy(strings)
    #actions.send_keys(strings).perform()
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(0.5)

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
time.sleep(3)

##### BlogSpot Only #####
if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    # 검색창
    myXpath = '/html/body/div[8]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    # 사이드메뉴
    myXpath = '/html/body/div[8]/div[2]/header/div[2]/div[1]/div[1]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    # 새 글 쓰기버튼
    myXpath = '/html/body/div[8]/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[3]/div/div/div[2]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(3)

if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    # 제목
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[1]/div[1]/div[1]/div/div[1]/input'
elif appName == appList[3]:
    # 제목
    myXpath = '//*[@id="inspector-textarea-control-0"]'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(0.2)
##### INPUT #####
input_string(myTitle)

# tags 1
# 라벨 입력창
if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[1]/span/div/div[1]/div[1]/div[2]/textarea'
elif appName == appList[3]:
    myXpath = '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[3]/div/div[1]/div/div'
element = driver.find_element(By.XPATH,myXpath)
xpos=element.location['x']+int(element.size['width']/2)
ypos=element.location['y']+int(element.size['height']/2)
input_click(xpos,ypos)
time.sleep(0.2)
##### INPUT #####
input_string(myTags)

if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    # 위치
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[4]'
    element = driver.find_element(By.XPATH,myXpath)
    for i in range(3):
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
    time.sleep(0.2)
    input_string("Seoul")
    # 돋보기
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[4]/span/div/div[2]/div/div[1]/div/span/div/span/span/span'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)

if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    # 검색 설명
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[5]/div/span/div/div'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    # 검색 설명 입력창
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[5]/span/div/div/div[1]/div[2]/textarea'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    ##### INPUT #####
    input_string(myDescription)
    time.sleep(0.2)
elif appName == appList[3]:
    # 설명 추가 창 열기
    myXpath = '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/div/div[3]/div/button'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(2)
    # 설명 추가 입력
    myXpath = '//*[@id="inspector-textarea-control-1"]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    ##### INPUT #####
    input_string(myDescription)
    time.sleep(0.2)
    # 설명 입력 창 닫기
    myXpath = '/html/body/div[4]/div/div/div[1]/div/button'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    
if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    # 퍼머링크
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/div/span/div/div'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(2)
    # 맞춤 라디오
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/span/div[1]/div[1]/span/div/div[2]/div[1]/div[3]/div/div'
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
    time.sleep(0.5)
elif appName == appList[3]:
    ########################################################################
    # 링크 창 열기
    myXpath = '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/div/div[5]/div/div[3]/div[2]/div/button/span'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(2)
    # 링크 입력
    myXpath = '/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div/div/input'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    input_string(myLink)
    time.sleep(0.2)
    # 링크 입력 창 닫기
    myXpath = '/html/body/div[4]/div/div/div/div[1]/div/button'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    
    # 카테고리 선택: Bash Scripts
    myXpath = '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/label'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    ########################################################################


if appName == appList[0] or appName == appList[1] or appName == appList[2]:
    # input type 2 <UP> <ENTER>
    isHtmlFmt = True
    # 본문 작성 형식 콤보 열기
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[2]/span'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    if isHtmlFmt:
        # HTML 보기
        myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]'
    else:
        # 새글작성 보기
        myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    
    # input Body 1
    # 본문
    #myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span'
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[2]/div/div/div/div[6]/div[1]/div/div/div/div[5]/div/pre'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.1)
    ##### INPUT #####
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    input_string(myBody)
elif appName == appList[3]:
    # 본문 작성
    myXpath = '//*[@id="post-content-0"]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
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
    time.sleep(0.2)
    # 저장
    myXpath = '/html/body/div[8]/c-wiz[2]/div[2]/div/div/span[2]/div[3]/div'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    # 뒤로가기 버튼
    myXpath = '/html/body/div[8]/div[2]/header/div[2]/div[1]/div[2]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
else:
    # 게시 버튼
    myXpath = '/html/body/div[8]/c-wiz[2]/div/c-wiz/div/div[1]/div[2]/div[4]/span'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)
    # 확인 버튼
    myXpath = '/html/body/div[8]/div[4]/div/div[2]/div[3]/div[2]/div[2]'
    element = driver.find_element(By.XPATH,myXpath)
    xpos=element.location['x']+int(element.size['width']/2)
    ypos=element.location['y']+int(element.size['height']/2)
    input_click(xpos,ypos)
    time.sleep(0.2)

with open("{}/registerd".format(postDir), 'w') as file_data:
    file_data.write('')

time.sleep(2)
  
driver.quit()
exit()
