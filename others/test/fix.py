import re
from text_mgt import *
rev = '[CQ:json,data={"app":"com.tencent.structmsg"&#44;"config":{"ctime":1651759603&#44;"forward":true&#44;"token":"6172db8cadaeef4a4678290a6b7efeb3"&#44;"type":"normal"}&#44;"desc":"新闻"&#44;"extra":{"app_type":1&#44;"appid":1103188687&#44;"uin":291526525}&#44;"meta":{"news":{"action":""&#44;"android_pkg_name":""&#44;"app_type":1&#44;"appid":1103188687&#44;"ctime":1651759603&#44;"desc":"点击上方蓝字发现更多精彩一，Nagios监控简介生活中大家应该对监控已司空见惯了…"&#44;"jumpUrl":"http://mp.weixin.qq.com/s?__biz=MzkyNDMzNDUyNA==&amp;mid=2247484484&amp;idx=1&amp;sn=7d08ddcf707747401752dd0029e5575d&amp;chksm=c1d62497f6a1ad81391cce28d7a34165259213199e22fcabef12bbebbc3985986e2f8b1305bd&amp;mpshare=1&amp;scene=23&amp;srcid=0505rddsMNYs7XeeyhHAuE1c&amp;sharer_sharetime=1651759581808&amp;sharer_shareid=098103f9faf960fc6cff73d3c64dfa9a#rd"&#44;"preview":"https://mmbiz.qlogo.cn/mmbiz_jpg/vNjNx7dezFId8vZu8euaWKSG3wkw6cRiaEd84CyyVFIpUFDC2aU7ADjdDYrLicT450Cbsu9VPQ5kJ2egxzvjy61w/300?wx_fmt=jpeg&amp;wxfrom=7"&#44;"source_icon":"https://i.gtimg.cn/open/app_icon/03/18/86/87/1103188687_100_m.png"&#44;"source_url":""&#44;"tag":"微信"&#44;"title":"【干货】企业级监控Nagios实践（上）"&#44;"uin":291526525}}&#44;"prompt":"&#91;分享&#93;【干货】企业级监控Nagios实践（上）"&#44;"ver":"0.0.0.1"&#44;"view":"news"}]'
end = re.compile('[^A-Z^a-z^\u4e00-\u9fa5]').sub('', rev)
bad_word = Text_Mgt.List_Read_Text('settings/word/bad_word.txt', '#')
print(len(bad_word))
#print(end)
for TEMP0 in bad_word:  # 逐一匹配广告词库
    if TEMP0 in end:  # 如果检测到了广告
        print(TEMP0)
else:
    print('no')