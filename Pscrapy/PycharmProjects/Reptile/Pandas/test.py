import re

import execjs
import requests
url = 'http://www.66ip.cn/1228.html'

header = {
# 'Cookie': '__jsluid=cbfffb32c3181e2d8a04bf2ad00ef041; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1560843572; __jsl_clearance=1560847785.481|0|fuDiD0ZRORlV6vMks29qNjj66JI%3D; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1560848231',

# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
r = requests.get('https://www.seebug.org/vuldb/ssvid-92666', headers=header)

print('Getting result', url, r.status_code)
print(r.cookies.get_dict())
# {'__jsluid': '644664d1b1a280cfd4aa856166f8c986'}

print(r.text)
# <script>var x="return@@@attachEvent@@cookie@e@@function@F@Path@g@50@0@@__jsl_clearance@@i@charCodeAt@onreadystatechange@@@location@innerHTML@setTimeout@@eval@catch@pathname@if@27@@ugJMWU@DOMContentLoaded@parseInt@@19@@JgSe0upZ@@split@a@chars@firstChild@6@@RegExp@try@7@join@1560995427@@@@@substr@@captcha@challenge@@@Jun@36@@else@1@@addEventListener@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@replace@@@0xEDB88320@f@8@3D@@1500@2@var@d@@toLowerCase@false@window@@Expires@@972@@Thu@fromCharCode@@div@@@Y@@reverse@@@@String@@20@toString@02@charAt@@match@@for@Array@search@DROxqoT@createElement@while@@GMT@length@@wiS5@document@@0xFF@https@new@href".replace(/@*$/,"").split("@"),y="2a 2c=9(){p('n.3n=n.t+n.39.20(/[\\?|&]1n-1o/,\\'\\')',28);3i.6='g=1g.2j|e|'+(9(){2a 2k=[9(2c){1 2c},9(2k){1 2k},9(2c){37(2a 2k=e;2k<2c.3f;2k++){2c[2k]=10(2c[2k]).31(1s)};1 2c.1f('')}],2c=[(1a+[]),((+!-[])+[])+[29+29],(1e+[[]][e]),[29+29],(-~[]+(+!-[])+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])+((-~{}<<-~{}))*[(-~{}<<-~{})]+[]+[]),(-~-~{}+[[]][e]),((+!-[])+[])+((-~{}|-~[]-~[])+[]+[]),((+!-[])+[])+((+!-[])+[]),((+!-[])+[]),((-~[]<<(-~{}|-~[]-~[]))+[[]][e]),((-~{}|-~[]-~[])+[]+[]),[~~''],[29+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])],((+!-[])+[])+[~~''],((+!-[])+[])+(-~-~{}+[[]][e])];37(2a 2s=e;2s<2c.3f;2s++){2c[2s]=2k[[1v,29,1v,29,1v,29,1v,29,1v,29,1v,e,1v,29,1v][2s]]([(-~-~{}+[[]][e]),'3h',[((+!-[])+[])+((-~{}|-~[]-~[])+[]+[])],'2r%',[((+!-[])+[])+((+!-[])+[])],'a','3a','i',[(-~-~{}+[[]][e])+((+!-[])+[])],'x',[(-~-~{}+[[]][e])+((-~[]<<(-~{}|-~[]-~[]))+[[]][e])],[(-~-~{}+[[]][e])+((+!-[])+[])],'%26','2b',[((+!-[])+[])+[~~'']]][2c[2s]])};1 2c.1f('')})()+';2h=2l, 30-1r-12 32:d:v 3e;b=/;'};u((9(){1d{1 !!2f.1x;}s(7){1 2e;}})()){3i.1x('y',2c,2e)}1u{3i.4('k',2c)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}</script>

txt_521 = ''.join(re.findall('<script>(.*?)</script>', r.text))
print(txt_521)
# var x="return@@@attachEvent@@cookie@e@@function@F@Path@g@50@0@@__jsl_clearance@@i@charCodeAt@onreadystatechange@@@location@innerHTML@setTimeout@@eval@catch@pathname@if@27@@ugJMWU@DOMContentLoaded@parseInt@@19@@JgSe0upZ@@split@a@chars@firstChild@6@@RegExp@try@7@join@1560995427@@@@@substr@@captcha@challenge@@@Jun@36@@else@1@@addEventListener@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@replace@@@0xEDB88320@f@8@3D@@1500@2@var@d@@toLowerCase@false@window@@Expires@@972@@Thu@fromCharCode@@div@@@Y@@reverse@@@@String@@20@toString@02@charAt@@match@@for@Array@search@DROxqoT@createElement@while@@GMT@length@@wiS5@document@@0xFF@https@new@href".replace(/@*$/,"").split("@"),y="2a 2c=9(){p('n.3n=n.t+n.39.20(/[\\?|&]1n-1o/,\\'\\')',28);3i.6='g=1g.2j|e|'+(9(){2a 2k=[9(2c){1 2c},9(2k){1 2k},9(2c){37(2a 2k=e;2k<2c.3f;2k++){2c[2k]=10(2c[2k]).31(1s)};1 2c.1f('')}],2c=[(1a+[]),((+!-[])+[])+[29+29],(1e+[[]][e]),[29+29],(-~[]+(+!-[])+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])+((-~{}<<-~{}))*[(-~{}<<-~{})]+[]+[]),(-~-~{}+[[]][e]),((+!-[])+[])+((-~{}|-~[]-~[])+[]+[]),((+!-[])+[])+((+!-[])+[]),((+!-[])+[]),((-~[]<<(-~{}|-~[]-~[]))+[[]][e]),((-~{}|-~[]-~[])+[]+[]),[~~''],[29+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])],((+!-[])+[])+[~~''],((+!-[])+[])+(-~-~{}+[[]][e])];37(2a 2s=e;2s<2c.3f;2s++){2c[2s]=2k[[1v,29,1v,29,1v,29,1v,29,1v,29,1v,e,1v,29,1v][2s]]([(-~-~{}+[[]][e]),'3h',[((+!-[])+[])+((-~{}|-~[]-~[])+[]+[])],'2r%',[((+!-[])+[])+((+!-[])+[])],'a','3a','i',[(-~-~{}+[[]][e])+((+!-[])+[])],'x',[(-~-~{}+[[]][e])+((-~[]<<(-~{}|-~[]-~[]))+[[]][e])],[(-~-~{}+[[]][e])+((+!-[])+[])],'%26','2b',[((+!-[])+[])+[~~'']]][2c[2s]])};1 2c.1f('')})()+';2h=2l, 30-1r-12 32:d:v 3e;b=/;'};u((9(){1d{1 !!2f.1x;}s(7){1 2e;}})()){3i.1x('y',2c,2e)}1u{3i.4('k',2c)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}

def fixed_fun(txt_521):
    func_return = txt_521.replace('eval','return')
    content = execjs.compile(func_return)    # 获取代码编译完成后的对象
    evaled_func = content.call('f')     # 调用js函数F,有参数需要传入参数
                                        # content.call("f", 1, 2)  # 调用js函数add，并传入它的参数
                                        # content.eval("f({0}, {1})").format(1, 2)  # 使用eval的写法同上，但是在传入字符串或者其他类型的数据时需要添加对应的格式,如下所示，具体可在程序中debug
                                        # content.eval('f("{0}", "{1}")').format("1", "2")
    print(evaled_func)
    # var _2c=function(){setTimeout('location.href=location.pathname+location.search.replace(/[\?|&]captcha-challenge/,\'\')',1500);document.cookie='__jsl_clearance=1560995427.972|0|'+(function(){var _2k=[function(_2c){return _2c},function(_2k){return _2k},function(_2c){for(var _2k=0;_2k<_2c.length;_2k++){_2c[_2k]=parseInt(_2c[_2k]).toString(36)};return _2c.join('')}],_2c=[(6+[]),((+!-[])+[])+[2+2],(7+[[]][0]),[2+2],(-~[]+(+!-[])+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])+((-~{}<<-~{}))*[(-~{}<<-~{})]+[]+[]),(-~-~{}+[[]][0]),((+!-[])+[])+((-~{}|-~[]-~[])+[]+[]),((+!-[])+[])+((+!-[])+[]),((+!-[])+[]),((-~[]<<(-~{}|-~[]-~[]))+[[]][0]),((-~{}|-~[]-~[])+[]+[]),[~~''],[2+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])],((+!-[])+[])+[~~''],((+!-[])+[])+(-~-~{}+[[]][0])];for(var _2s=0;_2s<_2c.length;_2s++){_2c[_2s]=_2k[[1,2,1,2,1,2,1,2,1,2,1,0,1,2,1][_2s]]([(-~-~{}+[[]][0]),'wiS5',[((+!-[])+[])+((-~{}|-~[]-~[])+[]+[])],'Y%',[((+!-[])+[])+((+!-[])+[])],'F','DROxqoT','i',[(-~-~{}+[[]][0])+((+!-[])+[])],'ugJMWU',[(-~-~{}+[[]][0])+((-~[]<<(-~{}|-~[]-~[]))+[[]][0])],[(-~-~{}+[[]][0])+((+!-[])+[])],'%3D','d',[((+!-[])+[])+[~~'']]][_2c[_2s]])};return _2c.join('')})()+';Expires=Thu, 20-Jun-19 02:50:27 GMT;Path=/;'};if((function(){try{return !!window.addEventListener;}catch(e){return false;}})()){document.addEventListener('DOMContentLoaded',_2c,false)}else{document.attachEvent('onreadystatechange',_2c)}

    return evaled_func



if __name__ == '__main__':
    evaled_func = fixed_fun(txt_521)
    a = re.match(r'var (.*?)=.*', evaled_func).group(1)
    print(a)
    mode_func = evaled_func.replace('document.cookie=','return ').replace(r"setTimeout('location.href=location.pathname+location.search.replace(/[\?|&]captcha-challenge/,\'\')',1500);", '').replace(r";if((function(){try{return !!window.addEventListener;}catch(e){return false;}})()){document.addEventListener('DOMContentLoaded',%s,false)}else{document.attachEvent('onreadystatechange',%s)}" % (a, a), '')
    print(mode_func)
    # var _2c=function(){return '__jsl_clearance=1560995427.972|0|'+(function(){var _2k=[function(_2c){return _2c},function(_2k){return _2k},function(_2c){for(var _2k=0;_2k<_2c.length;_2k++){_2c[_2k]=parseInt(_2c[_2k]).toString(36)};return _2c.join('')}],_2c=[(6+[]),((+!-[])+[])+[2+2],(7+[[]][0]),[2+2],(-~[]+(+!-[])+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])+((-~{}<<-~{}))*[(-~{}<<-~{})]+[]+[]),(-~-~{}+[[]][0]),((+!-[])+[])+((-~{}|-~[]-~[])+[]+[]),((+!-[])+[])+((+!-[])+[]),((+!-[])+[]),((-~[]<<(-~{}|-~[]-~[]))+[[]][0]),((-~{}|-~[]-~[])+[]+[]),[~~''],[2+((-~{}<<-~{})^-~!![[][{}]][-~(+[])])],((+!-[])+[])+[~~''],((+!-[])+[])+(-~-~{}+[[]][0])];for(var _2s=0;_2s<_2c.length;_2s++){_2c[_2s]=_2k[[1,2,1,2,1,2,1,2,1,2,1,0,1,2,1][_2s]]([(-~-~{}+[[]][0]),'wiS5',[((+!-[])+[])+((-~{}|-~[]-~[])+[]+[])],'Y%',[((+!-[])+[])+((+!-[])+[])],'F','DROxqoT','i',[(-~-~{}+[[]][0])+((+!-[])+[])],'ugJMWU',[(-~-~{}+[[]][0])+((-~[]<<(-~{}|-~[]-~[]))+[[]][0])],[(-~-~{}+[[]][0])+((+!-[])+[])],'%3D','d',[((+!-[])+[])+[~~'']]][_2c[_2s]])};return _2c.join('')})()+';Expires=Thu, 20-Jun-19 02:50:27 GMT;Path=/;'}

    c = execjs.compile(mode_func)
    print(c.call(a).split(';')[0])

    # __jsl_clearance=1560995427.972|0|DROxqoTaibugJMWUddlwiS5lY%2Fs%3D