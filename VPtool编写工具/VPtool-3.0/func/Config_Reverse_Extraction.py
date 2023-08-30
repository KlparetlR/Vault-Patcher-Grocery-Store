import json,os,dialogs
from .Key_Name_Merge import kmm
from LANG import zh_func_cre_text,zdy_func_cre_text,zdyconfig
def cre(langmode,save_address_vaule,File_vaule,cGuilang_entry,langFile_vaule):
    def runGui():
        global zdy,a0,cre1
        zdy,a0 = zdyconfig()
        if cGuilang_entry == "中文简体":
            cre1 = zh_func_cre_text()
        if cGuilang_entry == f"{zdy}":
            cre1 = zdy_func_cre_text()
    runGui()
    folderpath = save_address_vaule
    filePath = File_vaule
    fileName = os.path.basename(os.path.splitext(filePath)[0])
    resultDictxt = "{#INFO}\nPackname=@<Packname>\nKeyName=VP.modify.<Modid>.\nvalueIndex=1\n"
    if langmode == True:
        txt = kmm(True,folderpath,filePath,cGuilang_entry,langFile_vaule)
        data = json.loads(txt)
    else:
        with open(filePath, "r", encoding='utf-8') as f:
            # 读取json文件内容
            txt = f.read().encode("utf-8")
            data = json.loads(txt)
    # 遍历json文件中的每一项
    tempname = ""
    stack_depth = "-1"
    cut = False
    isclass = False
    obj = data[0]
    authors_entry="authors="
    name_entry="name="
    desc_entry="desc="
    mods_entry="mods="
    if "authors" in obj:
        authors_entry=authors_entry+obj["authors"]
    if "name" in obj:
        name_entry=name_entry+obj["name"]
    if "desc" in obj:
        desc_entry=desc_entry+obj["desc"]
    if "mods" in obj:
        mods_entry=mods_entry+obj["mods"]
    resultDictxt = resultDictxt+authors_entry+"\n"+name_entry+"\n"+desc_entry+"\n"+mods_entry+"\n{#VPCONFIG}"
    for item in data:
        if "key" in item:
            key = str(item["key"])
            if key !=  "" and "value" in item:
                value = item["value"]
                if value.startswith("@"):
                    key = "@;" + key
                if "target_class" in item:
                    target_class = item["target_class"]
                    if "name" in target_class:
                        name = target_class["name"]
                        if name != "":
                            if name.startswith("@"):
                                key = name+";" + key
                                if not tempname.startswith("@") and tempname != "":
                                    resultDictxt = resultDictxt +"\n"+ "#END"
                                    tempname = name
                            if not name.startswith("@"):
                                isclass = True
                                if tempname != name and tempname != "" and not tempname.startswith("@"):
                                    cut = True
                                if tempname != name and tempname != "" and tempname.startswith("@"):
                                    resultDictxt = resultDictxt +"\n#"+ name
                                if tempname == "":
                                    resultDictxt = resultDictxt +"\n#"+ name
                                tempname = name
                            if "method" in target_class:
                                method = target_class["method"]
                                if method != "":
                                    key = "&" + str(method) + ";" + key
                            if "stack_depth" in target_class:
                                stack_depth = target_class["stack_depth"]
                                if stack_depth != "-1" or stack_depth != "":
                                    key = ":" + str(stack_depth) + ";" + key
                            if cut == True:
                                resultDictxt = resultDictxt +"\n"+ "#END"
                                resultDictxt = resultDictxt +"\n#"+ name
                                cut = False
                    if not "name" in target_class and isclass == True:
                        resultDictxt = resultDictxt +"\n"+ "#END"
                        isclass = False
            resultDictxt = resultDictxt + "\n"+repr(key).strip("'").replace(":;","")
    if isclass == True:
        resultDictxt = resultDictxt +"\n"+ "#END"
        isclass = False
    putFile = folderpath + "/" + fileName + '.txt'
    fp = open(os.path.join(putFile), 'w+', encoding='utf8')
    fp.write(resultDictxt)
    fp.close()
        # 打开文件资源管理器并选中文件夹
    def open_folder(folderpath):
        if os.path.exists(folderpath):
            os.startfile(folderpath)
    open_folder(folderpath)
    # 成功提示
    dialogs.show_message('VPtool',f'{cre1}' % (fileName,folderpath))