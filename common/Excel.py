import openpyxl
import os
from common.log import Log
from openpyxl.styles import Font,colors

class ReadExcel:
    def __init__(self):
        self.filename = os.path.abspath(os.path.join(os.getcwd(),'..','data','test.xlsx'))
        #打开工作簿
        self.table = openpyxl.load_workbook(self.filename)
        #获取表单
        self.workBook = self.table.active
        #获取表单数据的总行数
        self.rowNum = self.workBook.max_row
        #获取表单数据的总列数
        self.colNum = self.workBook.max_column
        #关闭工作簿
        self.close = self.table.close()

    #获取某个单元格数据
    def get_cell_value(self,row,col):
        cellValue = self.workBook.cell(row,col).value
        return cellValue

    #读取表格
    def read_excel(self):
        if self.rowNum < 1:
            Log.info('行数小于1')
        else:
            cases = []
            for i in range(1,self.rowNum):
                s = {}
                s['rowNum'] = i+1
                Value = list(self.workBook.rows)
                titles = []
                for t in Value[0]:
                    title = t.value
                    titles.append(title)
                for row in Value:
                    case = []
                    for r in row:
                        case.append(r.value)
                    cases.append(dict(zip(titles,case)))
            self.close
            return cases

    def write_excel(self):
        #单元格样式
        ft = Font(color = '000000',size=14,bold=True)
        # if value in ['fail','error'] or col_n == 9:
        #     self.workBook.cell(row_n,col_n).font = ft
        self.workBook['H2']= 'pass'
        self.table.save('test.xlsx')





if __name__ == '__main__':
    #直接读取Excel时调用ReadExcel类
    test = ReadExcel()
    test.read_excel()
    # test.write_excel()
    # test.get_cell_value(2,5)
    # # res = test.read_excel()
    # # print(res[0]["value"])
    # test = ReadExcel.read_excel('Sheet')