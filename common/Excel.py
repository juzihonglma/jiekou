import openpyxl
import os
from data.Get_data import getdata
from common.log import Log
from openpyxl.styles import Font,Border

class Excel:
    def __init__(self):
        self.get_data = getdata()

        self.filename = os.path.abspath(os.path.join(os.getcwd(),'..','data','test.xlsx'))
        #打开工作簿
        self.table = openpyxl.load_workbook(self.filename)
        #获取表单
        self.workBook = self.table.active
        #关闭工作簿
        self.close = self.table.close()


    def write_excel(self,value):
        #成功或者失败的单元格的样式
        ft1 = Font(name='微软雅黑', color='FF00FF00', size=12, b='True')#name字体名称,color颜色通常是RGB或aRGB十六进制值,b(bold):加粗
        fy2 = Font(name='微软雅黑', color='FFFF0000',size=12, b='True')
        # success = Border(font = ft1)
        # fail = Border(font=fy2)
        #信息写入
        token_rowsNum = self.get_data.get_case_lines()
        for i in range(3,token_rowsNum+1):
            self.workBook.cell(i,self.get_data.token_col).value=value
        self.table.save(self.filename)





if __name__ == '__main__':
    #直接读取Excel时调用ReadExcel类
    # test = ReadExcel()
    # test.read_excel()
    Excel().write_excel()
    # test.write_excel()
    # test.get_cell_value(2,5)
    # # res = test.read_excel()
    # # print(res[0]["value"])
    # test = ReadExcel.read_excel('Sheet')