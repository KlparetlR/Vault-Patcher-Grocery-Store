import os,codecs,copy,json,dialogs,sys,subprocess,re
from LANG import zh_func_tc_text,zdy_gui_tc_text,zdyconfig,zh_gui_tca_text,zdy_gui_tca_text

def tca(FileGUI,icon_var,cGuilang_entry,authors_vaule,name_vaule,desc_vaule,mods_vaule):
    def runtcGui():
        global zdy,a0,vp1,vp2,vp3,vp4,vp5,vp6,vp7,vp8
        zdy,a0 = zdyconfig()
        if cGuilang_entry == "中文简体":
            vp1,vp2,vp3,vp4,vp5,vp6,vp7 = zh_func_tc_text()
            vp8 = zh_gui_tca_text()
        if cGuilang_entry == f"{zdy}":
            vp1,vp2,vp3,vp4,vp5,vp6,vp7 = zdy_gui_tc_text()
            vp8 = zdy_gui_tca_text()
    runtcGui()
    # 文件地址
    filePath = icon_var
    folderpath = FileGUI+'/%s/' % (vp1)
    fileName = os.path.basename(os.path.splitext(filePath)[0])
    # 文件初始内容
    fileTxtList = []
    # 1号下标
    index = 2
    # 类匹配开关
    isClass = False
    # 类名
    className = ''
    tempclassName = ' '
    # 汉化占位基础文本
    valueTxt = ''
    # 基础字典模板
    placeholder = {"authors": f"{authors_vaule}", "name": f"{name_vaule}", "desc": f"{desc_vaule}", "mods": f"{mods_vaule}"}
    targetClass = {'name': '', 'method': ''}
    # 最终结果输出
    resultList = []
    resultList2 = {}
    # 重启tool
    def restart():
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    # 获取文件行内容
    try:
        with open(filePath, 'r', encoding='utf8') as f:
            # 逐行读取加入列表
            fileTxtList = f.read().splitlines()
    except TypeError:
        dialogs.show_message('VPtool',f'{vp7}')
        print(f'{vp7}')
    # value基础值
    valueTxt = fileTxtList[0]
    # 起始值
    valueIndex = int(fileTxtList[1])
    # 遍历文本内容
    for _ in range(len(fileTxtList) - 2):
        resultDictionaries = {}
        # 获取当前临时文本
        tempFileTxt = fileTxtList[index]
        # 基础字典模板
        txtResult = {'key': "测试被汉化文本", 'value': '测试汉化文本'}
        # 判断开始
        print(tempFileTxt)
        if tempFileTxt == "":
            index += 1
            continue
        methoddata = ""
        # 先判断 是否启动类匹配开关
        if tempFileTxt[0] == '#' and tempFileTxt[1:4] != 'END':
            if tempclassName == ' ':
                isClass = True
                className = tempFileTxt
                tempclassName = str(tempFileTxt)
                index += 1
                continue
            elif tempclassName != ' ':
                if tempclassName[0] == '#' and tempFileTxt[1:4] != 'END':
                    print ("ERROR for <"+tempFileTxt+">,line:"+str(index))
                    dialogs.show_message('VPtool',f'{vp2}' % (tempFileTxt))
                    restart()
                else:
                    isClass = True
                    className = tempFileTxt
                    tempclassName = str(tempFileTxt)
                    index += 1
                    continue
        elif tempFileTxt[0:4] == '#END':
            isClass = False
            className = ''
            tempclassName = ' '
            index += 1
            continue
        # 后判断 method有没有
        methoddata = "".join(re.findall(r"&(.+?);",tempFileTxt))
        if methoddata != "" and isClass != False:
           tempFileTxt = tempFileTxt.replace("&"+methoddata+";","")
        if methoddata != "" and isClass == False:
           print ("ERROR for <&"+methoddata+";>,line:"+str(index))
           yan1 = dialogs.ask_yes_no('VPtool',f'{vp3}' % (methoddata))
           if yan1 == True:
               tempFileTxt = tempFileTxt.replace("&"+methoddata+";","")
               methoddata = ""
           else:
               restart()
        if isClass:
            txtResult['key'] = tempTxt = tempFileTxt
            txtResult['value'] = tempTxt2 = valueTxt + str(valueIndex)
            targetClass['name'] = className
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt2] = tempTxt
        if not isClass and tempFileTxt[0] != '#':
            print ("ERROR for <"+tempFileTxt+">,line:"+str(index))
            yan2 = dialogs.ask_yes_no('VPtool',f'{vp8}' % (tempFileTxt))
            if yan2 == True:
                index += 1
                continue
            else:
                restart()
        targetClass['method'] = methoddata
        methoddata = ""
        index += 1
        valueIndex += 1
    # 确保目标文件夹存在
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    # 输出 json化的字典数据到 该文件 没有该文件就创建新文件
    putFile = folderpath + fileName + '.json'
    putFile2 = folderpath + fileName + '-zh_cn.json'
    fp = codecs.open(os.path.join(putFile), 'w+', encoding='utf8')
    fp2 = codecs.open(os.path.join(putFile2), 'w+', encoding='utf8')
    # 嵌套字典
    resultList.insert(0, placeholder)
    resultDic = {'list': resultList}
    # 循环输出到文件
    resultDicJson = json.dumps(resultDic, ensure_ascii=False)
    resultList2 = json.dumps(resultList2, ensure_ascii=False)
    resultDicJson = str(resultDicJson[8:len(resultDicJson) - 1])
    resultList2 = str(resultList2)
    resultDicJson = resultDicJson.replace(r"\\n", r"\n").replace(r"\\u", r"\u").replace(r'\\\"', r'\"').replace(r"\\\'", r"\'")
    resultList2 = resultList2.replace(r"\\n", r"\n").replace(r"\\u", r"\u").replace(r'\\\"', r'\"').replace(r"\\\'", r"\'")
    fp.write(resultDicJson)
    fp2.write(resultList2)
    # 关闭文件流
    fp.close()
    fp2.close()
    # 打开文件资源管理器并选中文件夹
    def open_folder(folderpath):
        if os.path.exists(folderpath):
            os.startfile(folderpath)
        else:
            print ("ERROR: File path lost!")
            dialogs.show_message('VPtool',f'{vp4}')
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()
    open_folder(folderpath)
    # 成功提示
    dialogs.show_message('VPtool',f'{vp5}' % (fileName,folderpath))
