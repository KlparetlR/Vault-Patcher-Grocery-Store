"""
*-*<适配版本：1.2.10+>*-*
项目地址：https://github.com/KlparetlR/Vault-Patcher-Grocery-Store/blob/main/VPtool%E7%BC%96%E5%86%99%E5%B7%A5%E5%85%B7/
专门为VP模组而生的配置编写工具（https://github.com/3093FengMing/VaultPatcher ）
作者及版权方：晴笙墨染（莫安）、KlparetlR、捂脸Wulian, 技术辅助：XDawned
Fabric通用（https://github.com/LocalizedMC/HardcodeTextPatcher-Fabric ）
弹窗使用https://github.com/rdbende/Sun-Valley-messageboxes
"""

from tkinter import filedialog, StringVar, Tk, ttk
from tkinter.ttk import Button, Label, Entry,Combobox
import os,codecs,copy,json,dialogs,sys,subprocess,re,sv_ttk,ctypes,LANG
from LANG import zhlangtext,zdyconfig,zdylangtext

if __name__ == "__main__":
    vaulelang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
    def updateGui():
        file_lb.config(text=a1)
        savelangButton.config(text=a15)
        saveButton.config(text=a16)
        mods_lb.config(text=a14)
        desc_lb.config(text=a13)
        name_lb.config(text=a12)
        authors_lb.config(text=a11)
        packButton.config(text=a10)
        icon_lb.config(text=a9)
        IconButton.config(text=a10)
        cGuilang_lb.config(text=a8)
        mods_vaule.set(a4)
        desc_vaule.set(a4)
        name_vaule.set(a4)
        authors_vaule.set(a4)
        icon_var.set(a3)
        FileGUI.set(a3)
    def runlangGui():
        global zdy,a0,info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,vp1,vp2,vp3,vp4,vp5,vp6,langcurrent
        zdy,a0 = zdyconfig()
        if vaulelang == "0x804":
           info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,vp1,vp2,vp3,vp4,vp5,vp6 = zhlangtext()
           def langcurrent():
               cGuilang_entry.current(0)
        if vaulelang == f"{a0}":
           info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,vp1,vp2,vp3,vp4,vp5,vp6 = zdylangtext()
           def langcurrent():
               cGuilang_entry.current(2)
    runlangGui()
    def runclangGui():
        global zdy,a0,info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,vp1,vp2,vp3,vp4,vp5,vp6
        zdy,a0 = zdyconfig()
        if cGuilang_entry.get() == "中文简体":
            info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,vp1,vp2,vp3,vp4,vp5,vp6 = zhlangtext()
        if cGuilang_entry.get() == f"{zdy}":
            info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,vp1,vp2,vp3,vp4,vp5,vp6 = zdylangtext()
        updateGui()
        root.update()
    def browseStruct():
        FileGUI.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.txt *.TXT"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
    def browseIcon():
        icon_var.set(filedialog.askdirectory(title="%s" % (a2),initialdir=os.path.abspath(os.path.dirname(__file__))))
    def box_checked():
        saveButton.grid_forget()
        r = 0
        cGuilang_lb.grid(row=r, column=0,pady=5)
        langcurrent()
        cGuilang_entry.grid(row=r, column=1,pady=5)
        savelangButton.grid(row=r, column=2,pady=5,padx=20)
        r += 1
        empty_lb.grid(row=r, column=1,pady=5)
        r += 1
        file_lb.grid(row=r, column=0,pady=5)
        file_entry.grid(row=r, column=1,pady=5)
        packButton.grid(row=r, column=2,pady=5)
        r += 1
        icon_lb.grid(row=r, column=0,pady=5,padx=20)
        icon_entry.grid(row=r, column=1,pady=5)
        IconButton.grid(row=r, column=2,pady=5,padx=20)
        r += 1
        authors_lb.grid(row=r, column=0,pady=5,padx=20)
        authors_entry.grid(row=r, column=1,pady=5,padx=20)
        r += 1
        name_lb.grid(row=r, column=0,pady=5,padx=20)
        name_entry.grid(row=r, column=1,pady=5,padx=20)
        r += 1
        desc_lb.grid(row=r, column=0,pady=5,padx=20)
        desc_entry.grid(row=r, column=1,pady=5,padx=20)
        r += 1
        mods_lb.grid(row=r, column=0,pady=5,padx=20)
        mods_entry.grid(row=r, column=1,pady=5,padx=20)
        r += 1
        saveButton.grid(row=r, column=2,pady=5,padx=20)
        r += 1
    def runFromGui():
        if FileGUI.get() and icon_var.get() == "%s" % (a3) or len(FileGUI.get() and icon_var.get()) == 0:
            dialogs.show_message("ERROR", "%s" % (a5))
        else:
            if FileGUI.get() == "%s" % (a3) or len(FileGUI.get()) == 0:
                dialogs.show_message("ERROR", "%s" % (a6))
            if icon_var.get() == "%s" % (a3) or len(icon_var.get()) == 0:
                dialogs.show_message("ERROR", "%s" % (a7))
        vp()
    root = Tk()
    root.title("VPtool 2.11")
    cGuilang_lb = Label(root, text="%s" % (a8))
    combo_list = ["中文简体",f"{zdy}"]
    empty_lb = Label(root, text="")
    cGuilang_entry = Combobox(root,state="readonly", values=combo_list)
    FileGUI = StringVar(value="%s" % (a3))
    icon_var = StringVar(value="%s" % (a3))
    authors_vaule = StringVar(value="%s" % (a4))
    name_vaule = StringVar(value="%s" % (a4))
    desc_vaule = StringVar(value="%s" % (a4))
    mods_vaule = StringVar(value="%s" % (a4))
    file_entry = Entry(root, textvariable=FileGUI)
    icon_lb = Label(root, text="%s" % (a9))
    icon_entry = Entry(root, textvariable=icon_var)
    IconButton = Button(root, text="%s" % (a10), command=browseIcon)
    file_lb = Label(root, text="%s" % (a1))
    packButton = Button(root, text="%s" % (a10), command=browseStruct)
    authors_lb = Label(root, text="%s" % (a11))
    authors_entry = Entry(root, textvariable=authors_vaule)
    name_lb = Label(root, text="%s" % (a12))
    name_entry = Entry(root, textvariable=name_vaule)
    desc_lb = Label(root, text="%s" % (a13))
    desc_entry = Entry(root, textvariable=desc_vaule)
    mods_lb = Label(root, text="%s" % (a14))
    mods_entry = Entry(root, textvariable=mods_vaule)
    saveButton = Button(root, text="%s" % (a16), command=runFromGui)
    savelangButton = Button(root, text="%s" % (a15), command=runclangGui)
    box_checked()
    sv_ttk.use_light_theme()
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2) - 200
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    root.resizable(False, False)
    dialogs.show_message('VPtool-welcome',info)
    def vp():
        # 文件地址
        filePath = FileGUI.get()
        folderpath = icon_var.get()+'/%s/' % (vp1)
        fileName = os.path.basename(os.path.splitext(filePath)[0])
        # 文件初始内容
        fileTxtList = []
        # 1号下标
        index = 3
        # 类匹配开关
        isClass = False
        # 类名
        className = ''
        tempclassName = ' '
        # 堆键
        Reactordepth = ''
        # 包名备份
        packname = ''
        # 汉化占位基础文本
        valueTxt = ''
        # 基础字典模板
        placeholder = {"authors": f"{authors_vaule}", "name": f"{name_vaule}", "desc": f"{desc_vaule}", "mods": f"{mods_vaule}"}
        targetClass = {'name': 'nametype', 'method': 'method', 'stack_depth': -1}
        # 最终结果输出
        resultList = []
        resultList2 = {}
        # 重启tool
        def restart():
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()
        # 获取文件行内容
        with open(filePath, 'r', encoding='utf8') as f:
            # 逐行读取加入列表
            fileTxtList = f.read().splitlines()
        # nametype
        packname = fileTxtList[0]
        # value基础值
        valueTxt = fileTxtList[1]
        # 起始值
        valueIndex = int(fileTxtList[2])
        # 遍历文本内容
        for _ in range(len(fileTxtList) - 3):
            resultDictionaries = {}
            # 获取当前临时文本
            tempFileTxt = fileTxtList[index]
            # 基础字典模板
            txtResult = {'key': "测试被汉化文本", 'value': '测试汉化文本'}
            # 判断开始
            print(tempFileTxt)
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
                        print ("ERROR for <"+tempclassName+">")
                        dialogs.show_message('VPtool',f'{vp2}' % (tempclassName))
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
               print ("ERROR for <&"+methoddata+";>")
               yan1 = dialogs.ask_yes_no('VPtool',f'{vp3}' % (methoddata))
               if yan1 == True:
                   tempFileTxt = tempFileTxt.replace("&"+methoddata+";","")
                   methoddata = ""
               else:
                   restart()
            # 判断 堆键深度有没有
            Reactordata = "".join(re.findall(r":(.+?);",tempFileTxt))
            if Reactordata != "" and isClass != False:
               tempFileTxt = tempFileTxt.replace(":"+Reactordata+";","")
            if Reactordata != "" and isClass == False:
               print ("ERROR for <:"+Reactordata+";>")
               yan1 = dialogs.ask_yes_no('VPtool',f'{vp6}' % (Reactordata))
               if yan1 == True:
                   tempFileTxt = tempFileTxt.replace(":"+Reactordata+";","")
                   Reactordata = ""
               else:
                   restart()
            # 开启包名 和 半匹配 和 有类匹配(优先)
            if "@bm;" in tempFileTxt and "@;" in tempFileTxt and isClass:
                txtResult['key'] = tempTxt = tempFileTxt.split(';')[2]
                txtResult['value'] = tempTxt2 = "@" + valueTxt + str(valueIndex)
                targetClass['name'] = className
                tempTxt3 = valueTxt + str(valueIndex)
                tempTargetClass = copy.deepcopy(targetClass)
                resultDictionaries = {'target_class': tempTargetClass}
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt3] = tempTxt
            # 开启包名 和 半匹配 和 无类匹配
            elif "@bm;" in tempFileTxt and "@;" in tempFileTxt and isClass != True:
                targetClass['name'] = packname
                txtResult['key'] = tempTxt = tempFileTxt.split(';')[2]
                txtResult['value'] = tempTxt2 = "@" + valueTxt + str(valueIndex)
                tempTxt3 = valueTxt + str(valueIndex)
                tempTargetClass = copy.deepcopy(targetClass)
                resultDictionaries = {'target_class': tempTargetClass}
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt3] = tempTxt
            # 开启包名 和 有类匹配 类匹配优先
            elif "@bm;" in tempFileTxt and "@;" not in tempFileTxt and isClass:
                txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
                txtResult['value'] = tempTxt2 = valueTxt + str(valueIndex)
                targetClass['name'] = className
                tempTargetClass = copy.deepcopy(targetClass)
                resultDictionaries = {'target_class': tempTargetClass}
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt2] = tempTxt
            # 开启包名 和 无类匹配
            elif "@bm;" in tempFileTxt and "@;" not in tempFileTxt and isClass != True:
                targetClass['name'] = packname
                txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
                txtResult['value'] = tempTxt2 = valueTxt + str(valueIndex)
                tempTargetClass = copy.deepcopy(targetClass)
                resultDictionaries = {'target_class': tempTargetClass}
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt2] = tempTxt
            # 开启半匹配 和 有类匹配
            elif "@;" in tempFileTxt and "@bm;" not in tempFileTxt and isClass:
                txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
                txtResult['value'] = tempTxt2 = "@" + valueTxt + str(valueIndex)
                targetClass['name'] = className
                tempTxt3 = valueTxt + str(valueIndex)
                tempTargetClass = copy.deepcopy(targetClass)
                resultDictionaries = {'target_class': tempTargetClass}
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt3] = tempTxt
            # 开启半匹配 和 无类匹配
            elif "@;" in tempFileTxt and "@bm;" not in tempFileTxt and isClass != True:
                txtResult['key'] = tempTxt = tempFileTxt.split(';')[1]
                txtResult['value'] = tempTxt2 = "@" + valueTxt + str(valueIndex)
                tempTxt3 = valueTxt + str(valueIndex)
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt3] = tempTxt
            # 纯类匹配
            elif '@;' and '@bm' not in tempFileTxt and isClass:
                txtResult['key'] = tempTxt = tempFileTxt
                txtResult['value'] = tempTxt2 = valueTxt + str(valueIndex)
                targetClass['name'] = className
                tempTargetClass = copy.deepcopy(targetClass)
                resultDictionaries = {'target_class': tempTargetClass}
                resultDictionaries.update(txtResult)
                resultList.append(resultDictionaries)
                resultList2[tempTxt2] = tempTxt
            # 什么都不开 正常填入
            else:
                txtResult['key'] = tempTxt = tempFileTxt
                txtResult['value'] = tempTxt2 = valueTxt + str(valueIndex)
                resultDictionaries.update(txtResult)
                resultList.append(txtResult)
                resultList2[tempTxt2] = tempTxt
            targetClass['method'] = methoddata
            targetClass['stack_depth'] = Reactordata
            methoddata = ""
            Reactordata = ""
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
        resultDicJson = resultDicJson.replace(r"\\n", r"\n").replace(r"\\u", r"\u")
        resultList2 = resultList2.replace(r"\\n", r"\n").replace(r"\\u", r"\u")
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
    root.mainloop()