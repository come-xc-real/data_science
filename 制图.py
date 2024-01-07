import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
data = pd.read_csv("空气质量数据(加工).csv")
data["日期"] = pd.to_datetime(data["日期"])
data = data.loc[data["日期"].dt.year == 2014, :]
unique_level = data["质量等级"].unique()
quarters_list = ["1季度", "2季度", "3季度", "4季度"]
color_map = {'优': 'green', '良': 'darkgreen', '轻度污染': 'orange', '中度污染': 'red', '重度污染': 'purple', '严重污染': 'black', }
color_list = [color for color in color_map.values()]
color_name_list = [color for color in color_map.keys()]
quarterly_counts = data.groupby(['季度', '质量等级']).size().unstack()
bar = Bar()
bar.add_xaxis(quarters_list)
name_list = ["AQI", "PM2.5", "PM10", "SO2", "CO", "NO2", "O3"]
ratio = []
for i in range(len(quarters_list)):
    data_i = data.loc[data["季度"] == quarters_list[i]]
    ratio.append([])
    for j in range(len(name_list)):
        ratio[i].append(round(data_i[name_list[j]].sum() / data[name_list[j]].sum() * 100, 2))
ratio = list(map(list, zip(*ratio)))
for [i, quality], k in zip(enumerate(color_map.keys()), range(len(color_map))):
    y = quarterly_counts[quality].values
    bar.add_yaxis(color_name_list[k], list(y), stack="stack1", color=color_list[-k - 1], label_opts=opts.LabelOpts(is_show=True, position="left", formatter=JsCode(
            "function(x){return Number(x.data).toFixed() + '%';}"), ))
for m in range(len(name_list)):
    bar.add_yaxis(name_list[m], ratio[m], label_opts=opts.LabelOpts(is_show=True, position="top", formatter=JsCode("function(x){return Number(x.data).toFixed() + '%';}"),
                rotate=45, distance=20,))
bar.render("test.html")
