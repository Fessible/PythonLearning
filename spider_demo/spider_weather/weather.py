# 爬取中国天气网中全国个城市，最低气温排名前10的城市，并使用图表显示
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts

headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

BASE_URL = 'http://www.weather.com.cn'

ALL_DATA = []


def parse_page(url):
    response = requests.get(url, headers)
    # 由于天气网在港澳台那个模块中的格式错误，需要靠html5lib来进行格式化
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html5lib')
    # 通过解析页面，获取第一个class属性为conMidtab的内容，即获得今天的天气
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]

            min_temp_td = tds[-2]
            city_name = list(city_td.stripped_strings)[0]

            min_temp = min_temp_td.string
            print({'city': city_name, 'min_temp': min_temp})
            ALL_DATA.append({'city': city_name, 'min_temp': min_temp})
        print("-" * 50)


def main():
    # 获取各模块中的url，然后分别请求解析
    urls = get_url()
    for url in urls:
        parse_page(url)

    # 筛选温度最低的前10个城市，指定通过min_temp来进行排序
    ALL_DATA.sort(key=lambda x: int(x['min_temp']))
    # print(ALL_DATA)
    data = ALL_DATA[0:10]
    # 分别获取city列表和min_temp列表
    cities = list(map(lambda x: x['city'], data))
    min_temp = list(map(lambda x: x['min_temp'], data))

    # 绘制图表
    bar = (
        Bar()
            .add_xaxis(cities)
            .add_yaxis("", min_temp)
            .set_global_opts(title_opts=opts.TitleOpts(title='全国最低气温排名前10的城市'))
    )
    bar.render('weather.html')


# 获取url
def get_url():
    base_url = 'http://www.weather.com.cn/textFC/hb.shtml'
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
    urls = soup.find('ul', class_='lq_contentboxTab2').find_all('a')
    return map(lambda x: BASE_URL + x['href'], urls)


if __name__ == '__main__':
    main()
