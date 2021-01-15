import openpyxl
import os

class ReadExcel:
    def __init__(self,filename,sheetname):
        self.filename = os.path.abspath(os.path.join(os.getcwd(),'..','data','test.xlxs'))
        self.sheetname = sheetname

    def open(self):
        # 打开工作簿 openpyxl不支持 xls
        wb = openpyxl.load_workbook(self.filename)
        # 获取表单
        sh = wb[self.sheetname]
        return sh

    def get_row(self):
        global sh


    def close(self):
        self.wb.close()

    def set_style(name,height,bold=False):
        style = openpyxl.XFStyle()
        font = openpyxl.Font()
        font.name = name
        font.bold = bold
        font.height= height
        style.font = font
        return style

    def write_excel(self):
        #初始化workbook对象
        work= openpyxl.Workbook()
        sheet = work.active



        # sheet.write(0,0,'测试名称')
        # sheet.write(0, 1, '测')
        # sheet.write(0, 2, '试')

        # sheet.write_merge(0,2,'ceshi')

        work.save('test.xls')

    def read_excel(self):
        self.open()
        rows = self.sh.rows
        # cases = []
        for row in list(rows):
            case = []
            for r in row:
                case.append(r.value)
            # cases.append(dict(zip(case)))
        self.close()
        return case


if __name__ == '__main__':
    #直接读取Excel时调用ReadExcel类
    # test = ReadExcel('test.xlsx','Sheet')
    # res = test.read_excel()
    # print(res[0]["value"])
    test = ReadExcel.read_excel('Sheet')