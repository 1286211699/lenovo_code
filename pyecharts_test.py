# @Time : 2021/4/8 14:24 
# @Author : Smile_Mr
# @File : pyecharts_test.py 
# @Software: PyCharm

# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis([1,2,3])
# bar.add_yaxis('12',[3,4,5])
#
# bar.render()
import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

# 世界地图数据
value = [6000, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]
m = Map()
m.add("", list(zip(attr,value)),
      maptype="world",
      is_map_symbol_show=False)

m.set_global_opts(title_opts=opts.TitleOpts(title="各国现有确诊人数地图"),
                   visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                     pieces=[{
                                                         "min": 5000,
                                                         "label": '>5000',
                                                         "color": "#893448"
                                                     }, {
                                                         "min": 1000,
                                                         "max": 4999,
                                                         "label": '1000-4999',
                                                         "color": "#ff585e"
                                                     }, {
                                                         "min": 500,
                                                         "max": 999,
                                                         "label": '500-1000',
                                                         "color": "#fb8146"
                                                     }, {
                                                         "min": 101,
                                                         "max": 499,
                                                         "label": '101-499',
                                                         "color": "#ffA500"
                                                     }, {
                                                         "min": 10,
                                                         "max": 100,
                                                         "label": '10-100',
                                                         "color": "#ffb248"
                                                     }, {
                                                         "min": 0,
                                                         "max": 9,
                                                         "label": '0-9',
                                                         "color": "#fff2d1"
                                                     }]))
"""取消显示国家名称"""
m.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
m.render('test.html')
