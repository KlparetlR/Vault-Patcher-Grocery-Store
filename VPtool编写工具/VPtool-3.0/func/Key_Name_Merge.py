import json,os,dialogs
from LANG import zh_func_kmm_text,zdy_func_kmm_text,zdyconfig
def kmm(iscalledbyfunc,save_address_vaule,File_vaule,cGuilang_entry,langFile_vaule):
    def runGui():
        global zdy,a0,kmm1
        zdy,a0 = zdyconfig()
        if cGuilang_entry == "中文简体":
            kmm1 = zh_func_kmm_text()
        if cGuilang_entry == f"{zdy}":
            kmm1 = zdy_func_kmm_text()
    runGui()
    folderpath = save_address_vaule
    filePath = File_vaule
    langPath = langFile_vaule
    fileName = os.path.basename(os.path.splitext(filePath)[0])
    # 打开json文件和lang文件
    with open(filePath, "r", encoding="utf-8") as f1, open(langPath, "r", encoding="utf-8") as f2:
        # 读取json文件和lang文件的内容，并转换为python字典
        json_data = json.load(f1)
        lang_data = json.load(f2)
    # 遍历json文件中的每个对象
    for obj in json_data:
        # 如果对象中有"value"这个键
        if "value" in obj:
            # 获取"value"的值
            value = obj["value"]
            # 判断"value"的值是否以"@"开头
            if value.startswith("@"):
                # 如果是，就去掉"@"，并在lang文件中查找对应的键名
                key = value[1:]
                # 如果找到了，就用lang文件中的键值替换原来的"value"的值，并在前面加上"@"
                if key in lang_data:
                    obj["value"] = "@" + lang_data[key]
            else:
                # 如果不是，就直接在lang文件中查找对应的键名
                key = value
                # 如果找到了，就用lang文件中的键值替换原来的"value"的值
                if key in lang_data:
                    obj["value"] = lang_data[key]
    if iscalledbyfunc == False:
        putFile = folderpath + "/" + fileName + '+langMerge.json'
        fp = open(os.path.join(putFile), 'w+', encoding='utf8')
        fp.write(json.dumps(json_data, indent=4, ensure_ascii=False))
        fp.close()
            # 打开文件资源管理器并选中文件夹
        def open_folder(folderpath):
            if os.path.exists(folderpath):
                os.startfile(folderpath)
        open_folder(folderpath)
        # 成功提示
        dialogs.show_message('VPtool',f'{kmm1}')
    else:
        final_json_data = json.dumps(json_data, indent=4, ensure_ascii=False)
        print(f'{kmm1}')
        return final_json_data