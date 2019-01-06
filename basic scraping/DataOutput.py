# coding:utf-8

import codecs


class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('balks.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8' /></head>")
        fout.write("<body>")
        fout.write("<table border='1' rules='all'>")
        fout.write("<tr>")
        fout.write("<th>{}</td>".format('url'))
        fout.write("<th>{}</td>".format('title'))
        fout.write("<th>{}</td>".format('summary'))
        fout.write("</tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>{}</td>".format(data['url']))
            fout.write("<td>{}</td>".format(data['title']))
            fout.write("<td>{}</td>".format(data['summary']))
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
