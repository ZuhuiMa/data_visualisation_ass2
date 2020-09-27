#%%
# 导入Geo包，注意1.x版本的导入跟0.x版本的导入差别
from pyecharts.charts import Geo
# 导入配置项
from pyecharts import options as opts
# ChartType：图标类型，SymbolType：标记点类型
from pyecharts .globals import ChartType, SymbolType

geo = Geo()

# 地图类型，世界地图可换为world
geo.add_schema(maptype="china")
# 添加数据点
geo.add("",[("北京",10),("上海",20),("广州",30),("成都",40),("哈尔滨",50)],type_=ChartType.EFFECT_SCATTER)
# 添加流向，type_设置为LINES，涟漪配置为箭头，提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 
#'diamond', 'pin', 'arrow', 'none'
geo.add("geo-lines",
[("上海","广州"),
("上海","新疆"),
("上海","哈尔滨"),
("成都","北京"),
("哈尔滨","广州")],
type_=ChartType.LINES,
effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,symbol_size=5,color="yellow"),
linestyle_opts=opts.LineStyleOpts(curve=0.2),
    is_large=True)
# 不显示标签
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 设置图标标题，visualmap_opts=opts.VisualMapOpts()为左下角的视觉映射配置项
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(),title_opts=opts.TitleOpts(title="Geo-Lines"))
# 直接在notebook里显示图表
geo.render_notebook()
# 生成html文件，可传入位置参数
geo.render("mychart.html")
#%%