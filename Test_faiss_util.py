import sys
from nlp import ChatCleaner
from nlp.Faiss_Util import FaissSearch

# 创建 Faiss 实例
faiss_util = FaissSearch()

 # 添加数据
faiss_util.add_data("如何申请退款？", "您可以在订单详情页申请退款。")
faiss_util.add_data("如何联系客服？", "您可以拨打客服电话或在线联系。")
faiss_util.add_data("订单多久发货？", "订单一般会在 24 小时内发货。")
faiss_util.add_data("如何使用优惠券？", "在结算页面输入优惠券代码即可使用。")


results = faiss_util.search("没听明白")
print(results)

