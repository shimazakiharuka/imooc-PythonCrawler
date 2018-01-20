class HtmlOutputer(object):
    def __init__(self):
        self.datas = []   # []表示列表，{}表示字典/键值对

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)   # 这里的data是从html_parser返回的键值对{}

    def output_html(self):   # 输出为html格式
        fout = open('output.html', 'w', encoding='utf-8')    # w表示写模式

        fout.write('<meta charset="utf-8">')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")    # <table>代表表格</table> <tr>代表表格中的一行</tr> <td>代表表格中的一列</td>
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")   # 闭合标签
        fout.write("</body>")
        fout.write("</html>")

        fout.close()