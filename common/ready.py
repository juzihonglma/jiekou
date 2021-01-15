from selenium import webdriver

class ready_work():
    def __init__(self,brower):
        if brower == 'chrome' or brower == 'Chrome':
            chromDriverFilePath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
            deriver = webdriver.Chrome(chromDriverFilePath)
        elif brower == 'edge' or brower == 'Edge':
            edgeFilepath = "C:\Program\Files(x86)\Microsoft\Edge\Application\msedgedriver.exe"
            deriver = webdriver.edge(edgeFilepath)
        else:
            raise NameError('只能输入Chrome,Edge')
        self.driver = deriver
    #打开网页
    def open_url(self,url):
        self.driver.get(url)

    #设置窗口
    def set_winsize(self,wide,heigt):
        self.driver.set_window_size(wide,heigt)

    #输写
    def send_key(self,text):
        self.send_key(text)
    #等待
    def wait(self,secs):
        self.driver.implicitly_wait(secs)

    #执行js
    def js(self,sprit):
        self.driver.execute_script(sprit)

if __name__ == '__main__':
    ready_work.open_url(url='172.21.3.20')

# submit = driver.find_element_by_xpath("/2/*[@id='root-master']/div/div[]/div/form/div[4]/div/div/div/button");
# driver.execute_script("arguments[0].click();", submit);