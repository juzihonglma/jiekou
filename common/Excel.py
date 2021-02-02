import openpyxl
import os
from data.Get_data import getdata
from common.log import Log
from openpyxl.styles import Font,Border

class ReadExcel:
    def __init__(self):
        self.get_data = getdata()

        self.filename = os.path.abspath(os.path.join(os.getcwd(),'..','data','test.xlsx'))
        #打开工作簿
        self.table = openpyxl.load_workbook(self.filename)
        #获取表单
        self.workBook = self.table.active
        #关闭工作簿
        self.close = self.table.close()

    #读取表格
    # def read_excel(self):
    #     if self.rowNum < 1:
    #         Log.info('行数小于1')
    #     else:
    #         cases = []
    #         for i in range(1,self.rowNum):
    #             s = {}
    #             s['rowNum'] = i+1
    #             Value = list(self.workBook.rows)
    #             titles = []
    #             for t in Value[0]:
    #                 title = t.value
    #                 titles.append(title)
    #             for row in Value:
    #                 case = []
    #                 for r in row:
    #                     case.append(r.value)
    #                 cases.append(dict(zip(titles,case)))
    #         self.close
    #         return cases

<<<<<<< HEAD
    def write_excel(self,value):
        #成功或者失败的单元格的样式
        ft1 = Font(name='微软雅黑', color='FF00FF00', size=12, b='True')#name字体名称,color颜色通常是RGB或aRGB十六进制值,b(bold):加粗
        fy2 = Font(name='微软雅黑', color='FFFF0000',size=12, b='True')
        # success = Border(font = ft1)
        # fail = Border(font=fy2)
        #信息写入
        token_rowsNum = self.get_data.get_case_lines()
        for i in token_rowsNum+1:
            self.workBook.cell(i,token_rowsNum).value=value
=======
    def write_excel(self,cookie_value):
        ft1 = Font(name='微软雅黑', color='FF00FF00', size=12, b='True')#name字体名称,color颜色通常是RGB或aRGB十六进制值,b(bold):加粗
        fy2 = Font(name='微软雅黑', color='FFFF0000',size=12, b='True')
        success = Border(font = ft1)
        fail = Border(font=fy2)
        # a1.font = success


>>>>>>> 93d395ba417383cee532c96160998613500f2d7d
        self.table.save(self.filename)





if __name__ == '__main__':
    #直接读取Excel时调用ReadExcel类
    # test = ReadExcel()
    # test.read_excel()
    ReadExcel().write_excel()
    # test.write_excel()
    # test.get_cell_value(2,5)
    # # res = test.read_excel()
    # # print(res[0]["value"])
    # test = ReadExcel.read_excel('Sheet')