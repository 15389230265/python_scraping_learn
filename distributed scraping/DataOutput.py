# coding:utf-8

import codecs
import time


class DataOutput(object):
    def __init__(self):
        self.filepath = "baike_{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8' /></head>")
        fout.write("<body>")
        fout.write("<table border='1' rules='all'>")
        fout.write("<tr>")
        fout.write("<th>{}</td>".format('url'))
        fout.write("<th>{}</td>".format('title'))
        fout.write("<th>{}</td>".format('summary'))
        fout.write("</tr>")
        fout.close()

    def output_html(self, path):
        fout = codecs.open(path, 'a', encoding='utf-8')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>{}</td>".format(data['url']))
            fout.write("<td>{}</td>".format(data['title']))
            fout.write("<td>{}</td>".format(data['summary']))
            fout.write("</tr>")
            self.datas.remove(data)
        fout.close()

    def output_end(self, path):
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
