'''
项目地址：https://gist.github.com/KlparetlR/b7aa7c3004852575683ce9b3338db604
专门为VP模组而生的配置编写工具（https://github.com/3093FengMing/VaultPatcher  ）
作者及版权方：晴笙墨染（莫安）、KlparetlR。
提出支持Fabric的是textrue，编写这部分的是KlparetlR（https://github.com/LocalizedMC/HardcodeTextPatcher-Fabric  ）
'''
#基础定义
import codecs,copy,json,os,tkinter
from tkinter import filedialog,messagebox
#文件地址
filePath = filedialog.askopenfilename(title='选择要处理的文件（一个）',initialdir=os.path.abspath(os.path.dirname(__file__)))
folderpath = filedialog.askdirectory(title='选择要保存的文件夹地址',initialdir=os.path.abspath(os.path.dirname(__file__)))+'/硬编码配置/'
fileName = os.path.basename(os.path.splitext(filePath)[0])
#文件初始内容
fileTxtList = []
#1号下标
index = 3
#类匹配开关
isClass = False
#类名
className=''
#包名备份
packName = ''
# 汉化占位基础文本
valueTxt = ''
#模组加载器适配
root = tkinter.Tk()
root.title('VPtool')
tkinter.Label(root,text="选择您要使用的模组加载器格式，\n这将影响你的配置文件适配哪种版本的模组",font=("微软雅黑",11)).place(x=20,y=35)
root.minsize(350,200)
root.attributes("-topmost", True)
def Fabric():
    global loadertype,loadername
    loadertype = 'Intermediaty'
    loadername = 'HardcodePatcher'
    root.quit()
def Forge():
    global loadertype,loadername
    loadertype = 'SRG'
    loadername = 'VaultPatcher'
    root.quit()
btn1 = tkinter.Button(root,text = 'Fabric',command = Fabric,width=8).place(x=95,y=150)
btn2 = tkinter.Button(root,text = 'Forge',command = Forge,width=8).place(x=190,y=150)
root.mainloop()
#基础字典模板
placeholder = {"authors": "(authors)","name": "(name)","desc": "(describe)","mods": "(mods)"}
targetClass = {'name': 'nametype', 'mapping':f'{loadertype}', 'stack_depth': -1}
# 最终结果输出
resultList = []
resultList2 = {}
#获取文件行内容
with open(filePath , 'r', encoding='utf8') as f:
    #逐行读取加入列表
    fileTxtList = f.read().splitlines()
#nametype
packName = fileTxtList[0]
#value基础值
valueTxt = fileTxtList[1]
#起始值
valueIndex = int(fileTxtList[2])

##操作开始##

#遍历文本内容
for _ in range(len(fileTxtList)-3):
    resultDictionaries={}
    #获取当前临时文本
    tempFileTxt = fileTxtList[index]
    # 基础字典模板
    txtResult = {'key': "测试被汉化文本", 'value': '测试汉化文本'}
    #判断开始
    print(tempFileTxt)
    #先判断 是否启动类匹配开关
    if tempFileTxt[0]=='#' and tempFileTxt[1:4]!='END':
        isClass = True
        className = tempFileTxt
        index += 1
        continue
    elif tempFileTxt[0:4]=='#END':
        isClass = False
        index += 1
        continue
    # 开启包名 和 半匹配 和 有类匹配（优先）
    if "@bm;" in tempFileTxt and "@;" in tempFileTxt and isClass:
        txtResult['key'] = tempTxt = tempFileTxt.split(';')[2]
        txtResult['value'] = tempTxt2 = "@"+valueTxt+str(valueIndex)
        targetClass['name'] = className
        tempTxt3 = valueTxt+str(valueIndex)
        tempTargetClass = copy.deepcopy(targetClass)
        resultDictionaries = {'target_class': tempTargetClass}
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt3]=tempTxt
    # 开启包名 和 半匹配 和 无类匹配
    elif "@bm;" in tempFileTxt and "@;" in tempFileTxt and isClass!=True:
        targetClass['name'] = packName
        txtResult['key'] = tempTxt = tempFileTxt.split(';')[2]
        txtResult['value'] = tempTxt2 = "@"+valueTxt+str(valueIndex)
        tempTxt3 = valueTxt+str(valueIndex)
        tempTargetClass = copy.deepcopy(targetClass)
        resultDictionaries = {'target_class': tempTargetClass}
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt3]=tempTxt
    # 开启包名 和 有类匹配 类匹配优先
    elif "@bm;" in tempFileTxt and "@;" not in tempFileTxt and isClass:
        txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
        txtResult['value'] = tempTxt2 = valueTxt+str(valueIndex)
        targetClass['name'] = className
        tempTargetClass = copy.deepcopy(targetClass)
        resultDictionaries = {'target_class': tempTargetClass}
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt2]=tempTxt
    # 开启包名 和 无类匹配
    elif "@bm;" in tempFileTxt and "@;" not in tempFileTxt and isClass!=True:
        targetClass['name'] = packName
        txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
        txtResult['value'] = tempTxt2 = valueTxt+str(valueIndex)
        tempTargetClass = copy.deepcopy(targetClass)
        resultDictionaries = {'target_class': tempTargetClass}
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt2]=tempTxt
    # 开启半匹配 和 有类匹配
    elif "@;" in tempFileTxt and "@bm;" not in tempFileTxt and isClass:
        txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
        txtResult['value'] = tempTxt2 = "@"+valueTxt+str(valueIndex)
        targetClass['name'] = className
        tempTxt3 = valueTxt+str(valueIndex)
        tempTargetClass = copy.deepcopy(targetClass)
        resultDictionaries = {'target_class': tempTargetClass}
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt3]=tempTxt
    # 开启半匹配 和 无类匹配
    elif "@;" in tempFileTxt and "@bm;" not in tempFileTxt and isClass!=True:
        txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
        txtResult['value'] = tempTxt2 = "@"+valueTxt+str(valueIndex)
        tempTxt3 = valueTxt+str(valueIndex)
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt3]=tempTxt
    # 纯类匹配
    elif '@;' and '@bm' not in tempFileTxt and isClass:
        txtResult['key'] = tempTxt = tempFileTxt
        txtResult['value'] = tempTxt2 = valueTxt+str(valueIndex)
        targetClass['name'] = className
        tempTargetClass = copy.deepcopy(targetClass)
        resultDictionaries = {'target_class': tempTargetClass}
        resultDictionaries.update(txtResult)
        resultList.append(resultDictionaries)
        resultList2[tempTxt2]=tempTxt
    # 什么都不开 正常填入
    else:
        txtResult['key'] = tempTxt = tempFileTxt
        txtResult['value'] = tempTxt2 = valueTxt+str(valueIndex)
        resultDictionaries.update(txtResult)
        resultList.append(txtResult)
        resultList2[tempTxt2]=tempTxt
    index += 1
    valueIndex += 1
# 确保目标文件夹存在
if not os.path.exists(folderpath):
    os.makedirs(folderpath)
# 输出 json化的字典数据到 该文件 没有该文件就创建新文件
putFile = folderpath + fileName +'.json'
putFile2 = folderpath + fileName +'-zh_cn.json'
fp = codecs.open(os.path.join(putFile),'w+',encoding='utf8')
fp2 = codecs.open(os.path.join(putFile2),'w+',encoding='utf8')
# 嵌套字典
resultList.insert(0,placeholder)
resultDic = {'list': resultList}
# 循环输出到文件
resultDicJson = json.dumps(resultDic,ensure_ascii=False)
resultList2 = json.dumps(resultList2, ensure_ascii=False)
resultDicJson = str(resultDicJson[8:len(resultDicJson)-1])
resultList2 = str(resultList2)
resultDicJson = resultDicJson.replace(r"\\n",r"\n").replace(r"\\u",r"\u")
resultList2 = resultList2.replace(r"\\n",r"\n").replace(r"\\u",r"\u")
fp.write(resultDicJson)
fp2.write(resultList2)
# 关闭文件流
fp.close()
fp2.close()
# 成功提示（无错误检测）
messagebox.showinfo(title='VPtool', message=f'VPtool成功将{fileName}.txt文件转换为{loadername}模组配置格式。\n并储存在{folderpath} 目录中。')