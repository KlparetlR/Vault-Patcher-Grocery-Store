import os,codecs,copy,json,dialogs,sys,subprocess,re
from LANG import zh_func_tc_text,zdy_gui_tc_text,zdyconfig

def tc(File_vaule,save_address_vaule,cGuilang_entry,tempauthors,tempname,tempdesc,tempmods):
    global Packname,KeyName,valueIndex,authors,name,desc,mods
    authors,name,desc,mods = tempauthors,tempname,tempdesc,tempmods
    def runGui():
        global zdy,a0,vp1,vp2,vp3,vp4,vp5,vp6,vp7,vp8_a4
        zdy,a0 = zdyconfig()
        if cGuilang_entry == "中文简体":
            vp1,vp2,vp3,vp4,vp5,vp6,vp7,vp8_a4 = zh_func_tc_text()
        if cGuilang_entry == f"{zdy}":
            vp1,vp2,vp3,vp4,vp5,vp6,vp7,vp8_a4 = zdy_gui_tc_text()
    runGui()
    # 文件地址
    filePath = save_address_vaule
    folderpath = File_vaule+'/%s/' % (vp1)
    fileName = os.path.basename(os.path.splitext(filePath)[0])
    # 文件初始内容
    fileTxtList = []
    # 类匹配开关
    isClass = False
    # 类名
    className = ''
    tempclassName = ' '
    # 包名备份
    Packname = '@<Packname>'
    # 汉化占位基础文本
    KeyName = 'VP.modify.<Modid>.'
    # 基础字典模板
    targetClass = {'name': 'nametype', 'method': 'method', 'stack_depth': -1}
    # 最终结果输出
    resultList = []
    resultList2 = {}
    # 起始值
    valueIndex = 1
    # 重启tool
    def restart():
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    with open(filePath, 'r', encoding='utf8') as f:
        # 逐行读取加入列表
        fileTxtList = f.read().splitlines()
        # 找到{#INFO}和{#VPCONFIG}的位置
        start = fileTxtList.index("{#INFO}")
        end = fileTxtList.index("{#VPCONFIG}")
        # 截取{#INFO}和{#VPCONFIG}之间的内容
        info = "\n".join(fileTxtList[(start+1) : end])
        # 按行分割内容
        lines = info.split("\n")
        # 遍历每一行
        for line in lines:
            # 如果有等号
            if "=" in line:
                # 分割等号前后的内容
                key, value = line.split("=")
                # 去掉空格
                key = key.strip()
                value = value.strip()
                if key in ["Packname", "KeyName", "valueIndex", "authors", "name", "desc", "mods"]:
                    exec(f'globals()["{key}"] = "{value}"')
                    exec(f'locals()["{key}"] = "{value}"')
    if tempauthors != f"{vp8_a4}" and authors != tempauthors:
        authors=tempauthors
    if tempname == f"{vp8_a4}"and name!=tempname:
        name=tempname
    if tempdesc == f"{vp8_a4}"and desc!=tempdesc:
        desc=tempdesc
    if tempmods == f"{vp8_a4}"and mods != tempmods:
        mods = tempmods
    placeholder = {"authors": f"{authors}", "name": f"{name}", "desc": f"{desc}", "mods": f"{mods}"}
    valueIndex = int(valueIndex)
    # nametype
    tempPackname = Packname
    # 1号下标
    index = end+1
    # 遍历文本内容
    for _ in range(len(fileTxtList) - (end+1)):
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
        Reactordata = ""
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
                    print ("ERROR for <"+tempFileTxt+">,line:"+str(index+1))
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
        # 判断 包名有没有
        packdata = "".join(re.findall(r"@(.+?);",tempFileTxt))
        if packdata != "" and packdata != "bm" and not "@bm;" in tempFileTxt:
            tempFileTxt = tempFileTxt.replace("@"+packdata+";","@bm;")
            Packname = "@"+packdata
        # 后判断 method有没有
        methoddata = "".join(re.findall(r"&(.+?);",tempFileTxt))
        if methoddata != "":
            if isClass != False or packdata != "":
               tempFileTxt = tempFileTxt.replace("&"+methoddata+";","")
            if isClass == False and packdata == "":
               print ("ERROR for <&"+methoddata+";>,line:"+str(index))
               yan = dialogs.ask_yes_no('VPtool',f'{vp3}' % (methoddata))
               if yan == True:
                   tempFileTxt = tempFileTxt.replace("&"+methoddata+";","")
                   methoddata = ""
               else:
                   restart()
        # 判断 堆键深度有没有
        Reactordata = "".join(re.findall(r":(.+?);",tempFileTxt))
        if Reactordata != "":
            if isClass != False or packdata != "":
               tempFileTxt = tempFileTxt.replace(":"+Reactordata+";","")
            if isClass == False and packdata == "":
               print ("ERROR for <:"+Reactordata+";>,line:"+str(index))
               yan = dialogs.ask_yes_no('VPtool',f'{vp6}' % (Reactordata))
               if yan == True:
                   tempFileTxt = tempFileTxt.replace(":"+Reactordata+";","")
                   Reactordata = ""
               else:
                   restart()
        # 开启包名 和 半匹配 和 有类匹配(优先)
        if "@bm;" in tempFileTxt and "@;" in tempFileTxt and isClass:
            txtResult['key'] = tempTxt = tempFileTxt.split(';')[2]
            txtResult['value'] = tempTxt2 = "@" + KeyName + str(valueIndex)
            targetClass['name'] = className
            tempTxt3 = KeyName + str(valueIndex)
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt3] = tempTxt
        # 开启包名 和 半匹配 和 无类匹配
        elif "@bm;" in tempFileTxt and "@;" in tempFileTxt and isClass != True:
            targetClass['name'] = Packname
            txtResult['key'] = tempTxt = tempFileTxt.split(';')[2]
            txtResult['value'] = tempTxt2 = "@" + KeyName + str(valueIndex)
            tempTxt3 = KeyName + str(valueIndex)
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt3] = tempTxt
        # 开启包名 和 有类匹配 类匹配优先
        elif "@bm;" in tempFileTxt and "@;" not in tempFileTxt and isClass:
            txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
            txtResult['value'] = tempTxt2 = KeyName + str(valueIndex)
            targetClass['name'] = className
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt2] = tempTxt
        # 开启包名 和 无类匹配
        elif "@bm;" in tempFileTxt and "@;" not in tempFileTxt and isClass != True:
            targetClass['name'] = Packname
            txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
            txtResult['value'] = tempTxt2 = KeyName + str(valueIndex)
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt2] = tempTxt
        # 开启半匹配 和 有类匹配
        elif "@;" in tempFileTxt and "@bm;" not in tempFileTxt and isClass:
            txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
            txtResult['value'] = tempTxt2 = "@" + KeyName + str(valueIndex)
            targetClass['name'] = className
            tempTxt3 = KeyName + str(valueIndex)
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt3] = tempTxt
        # 开启半匹配 和 无类匹配
        elif "@;" in tempFileTxt and "@bm;" not in tempFileTxt and isClass != True:
            txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
            txtResult['value'] = tempTxt2 = "@" + KeyName + str(valueIndex)
            tempTxt3 = KeyName + str(valueIndex)
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt3] = tempTxt
        # 纯类匹配
        elif '@;' and '@bm' not in tempFileTxt and isClass:
            txtResult['key'] = tempTxt = tempFileTxt
            txtResult['value'] = tempTxt2 = KeyName + str(valueIndex)
            targetClass['name'] = className
            tempTargetClass = copy.deepcopy(targetClass)
            resultDictionaries = {'target_class': tempTargetClass}
            resultDictionaries.update(txtResult)
            resultList.append(resultDictionaries)
            resultList2[tempTxt2] = tempTxt
        # 什么都不开 正常填入
        else:
            txtResult['key'] = tempTxt = tempFileTxt
            txtResult['value'] = tempTxt2 = KeyName + str(valueIndex)
            resultDictionaries.update(txtResult)
            resultList.append(txtResult)
            resultList2[tempTxt2] = tempTxt
        targetClass['method'] = methoddata
        targetClass['stack_depth'] = Reactordata
        Packname = tempPackname
        methoddata = ""
        Reactordata = ""
        packdata = ""
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
    resultList2 = resultList2.replace(r"\\n", r"\n").replace(r"\\u", r"\u").replace(r'\\\"', r'\"').replace(r"\\\'", r"\'").replace(r"%", r"%%")
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
