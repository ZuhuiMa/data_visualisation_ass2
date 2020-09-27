# %%
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, GeoType
import pandas as pd
import numpy as np
import math

from pyecharts.options.global_options import LegendOpts

#
# 导入数据集
flight_data = pd.read_csv(
    '/mnt/c/Users/mazuhui/OneDrive - UTS/数据可视化/ass2/flights.csv')

# 构建数据集
flight_routes = (np.array(flight_data[[' From_City ', ' To_City ']].applymap(
    lambda x: x.strip())).tolist())
city_list = flight_data[' From_City '].apply(
    lambda x: x.strip()).unique().tolist()
city_points = list(zip(city_list, [0]*len(city_list)))

geo = Geo(init_opts={"width": "1200px", "height": "800px",
                     "chart_id": "test", "bg_color": "#a4b097"})
# 插入城市
geo.add_coordinate(name="Sydney", longitude=151.2099, latitude=-33.865143)
geo.add_coordinate(name="Canberra", longitude=149.128998, latitude=-35.282001)
geo.add_coordinate(name="Newcastle", longitude=151.75, latitude=-32.916668)
geo.add_coordinate(name="Broken Hill", longitude=141.467773,
                   latitude=-31.956667)
geo.add_coordinate(name="Melbourne", longitude=144.946457, latitude=-37.840935)
geo.add_coordinate(name="Bendigo", longitude=144.278702, latitude=-36.757786)
geo.add_coordinate(name="Adelaide", longitude=138.503052, latitude=-34.846111)
geo.add_coordinate(name="Darwin", longitude=130.841782, latitude=-12.462827)
geo.add_coordinate(name="Alice Springs",
                   longitude=133.882675, latitude=-23.700552)
geo.add_coordinate(name="Perth", longitude=115.857048, latitude=-31.953512)
geo.add_coordinate(name="Albany", longitude=117.881386, latitude=-35.022778)
geo.add_coordinate(name="Kalgoorlie", longitude=121.465836, latitude=-30.74889)
geo.add_coordinate(name="Broome", longitude=117.793221, latitude=-25.042261)
geo.add_coordinate(name="Launceston", longitude=147.157135,
                   latitude=-41.429825)
geo.add_coordinate(name="Hobart", longitude=147.324997, latitude=-42.880554)
geo.add_coordinate(name="Brisbane", longitude=153.021072, latitude=-27.470125)
geo.add_coordinate(name="Mt Isa", longitude=139.497467, latitude=-20.724705)
geo.add_coordinate(name="Rockhampton", longitude=150.511673, latitude=-23.375)
geo.add_coordinate(name="Cairns", longitude=145.75412, latitude=-16.925491)
geo.add_coordinate(name="Pt Augusta", longitude=137.765839, latitude=-32.4925)
# Define schema
geo.add_schema(maptype="world", center=(134.577783, -25.581685), zoom=5)

# Define city labels
city_labels = opts.LabelOpts(is_show=True, formatter='{b}', font_size=12, color='black',
                             font_family='monospace', position='right', distance=10, font_style='bold')

# Draw cities
geo.add('Cities', city_points, type_=GeoType.EFFECT_SCATTER, symbol_size=7, color='#5b5b73',
        label_opts=city_labels,tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on="mousemove",formatter='{b}<br>{c}'))


# Define the class->color dict
flight_class_color = {'A': '#de6a73', 'B': '#5FFF38',
                      'C': '#9071ce', 'D': '#eb895f', 'E': '#41a4ff'}
# Extract prices
prices = flight_data[' Price '].values

def route_formatter(i):
    plane_model = flight_data.loc[i, ' Aircraft Model'].strip()
    engine_model = flight_data.loc[i, ' Engine Model'].strip()
    return '{b} <br> Plane Model: '+plane_model+'<br> Flight Class: '+flight_data.loc[i, ' AirSpace Class'].strip()+'<br> Engine Model: '+engine_model+'<br> Price: '+ str(flight_data.loc[i, ' Price '])


# Draw each route seperately
for i, flight_route in enumerate(flight_routes):
    price = flight_data.loc[i, ' Price ']
    width = (price/(flight_data[' Price '].max() -
                    flight_data[' Price '].min()))*3
    flight_class = flight_data.loc[i, ' AirSpace Class'].strip()
    line_color = flight_class_color[flight_class]

    data_pair = [flight_route]

    geo.add(series_name='Flight class '+flight_class,
            data_pair=data_pair,
            type_=GeoType.LINES, symbol_size=1,
            effect_opts=opts.EffectOpts(color='auto',
                                        symbol='image://plane.png', symbol_size=13,  trail_length=0),
            linestyle_opts=opts.LineStyleOpts(width=width,
                                              curve=0.18, color=line_color),
            label_opts=opts.LabelOpts(is_show=False),
            progressive=600,
            tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on="mousemove",formatter=route_formatter(i))
            )




# 不显示标签
geo.set_global_opts(legend_opts=opts.LegendOpts(pos_left=10,pos_bottom=10, orient='vertical'))
# 直接在notebook里显示图表
# geo.render_notebook()

# 生成html文件，可传入位置参数
geo.render("mychart.html")
# %%
