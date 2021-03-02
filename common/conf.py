import os
import allure
import datetime

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#报告路径
TEST_CASE_PATH = os.path.join(BASE_PATH,'report','report.html')

#allure相关配置
reslut_path = os.path.join(BASE_PATH,'report','reslut')
allure_html_path = os.path.join(BASE_PATH,'report','report.html')
ALLURE_COMMAND = 'allure generate {} -o {} --clean'.format(reslut_path,allure_html_path)

if __name__ == '__main__':
    print(BASE_PATH)

