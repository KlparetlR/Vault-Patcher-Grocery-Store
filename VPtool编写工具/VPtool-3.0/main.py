"""
*-*<适配版本：1.2.10+>*-*
项目地址：https://github.com/KlparetlR/Vault-Patcher-Grocery-Store/blob/main/VPtool%E7%BC%96%E5%86%99%E5%B7%A5%E5%85%B7/
专门为VP模组而生的配置编写工具（https://github.com/3093FengMing/VaultPatcher ）
作者及版权方：晴笙墨染（莫安）、KlparetlR、捂脸Wulian、3093FengMing, 技术辅助：XDawned
Fabric通用（https://github.com/LocalizedMC/HardcodeTextPatcher-Fabric ）
弹窗使用https://github.com/rdbende/Sun-Valley-messageboxes
"""
from tkinter import filedialog,StringVar,Tk
from tkinter.ttk import Button,Label,Entry,Combobox
import os,dialogs,sv_ttk,ctypes,sys
from LANG import zhguitext,zdyconfig,zdyguitext
from func import tca,lse,tc,cre,kmm

if __name__ == "__main__":
    vaulelang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
    def runlangGui():
        global zdy,a0,info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,langcurrent
        zdy,a0 = zdyconfig()
        info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24 = zhguitext()
        def langcurrent():
            cGuilang_entry.current(0)
        if vaulelang == f"{a0}":
           info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24 = zdyguitext()
           def langcurrent():
               cGuilang_entry.current(1)
    runlangGui()
    def Vwo50xiexie():
        if len(File_vaule.get()) != 0 or File_vaule.get() != "":
            with open(File_vaule.get(), 'r', encoding='utf8') as f:
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
                        if key == "authors":
                            authors_vaule.set(value)
                        if key == "name":
                            name_vaule.set(value)
                        if key == "desc":
                            desc_vaule.set(value)
                        if key == "mods":
                            mods_vaule.set(value)
    def browseStruct():
        File_vaule.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.txt *.TXT"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
        Vwo50xiexie()
    def browselang():
        langFile_vaule.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.json"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
    def browseaddress():
        save_address_vaule.set(filedialog.askdirectory(title="%s" % (a2),initialdir=os.path.abspath(os.path.dirname(__file__))))
    def box_checked():
        global r
        r = 0
        cGuilang_lb.grid(row=r, column=0,pady=5)
        langcurrent()
        cGuilang_entry.grid(row=r, column=1,pady=5)
        r = 1
        sv_ttk_theme_lb.grid(row=r, column=0,pady=5)
        sv_ttk_theme_entry.current(0)
        sv_ttk_theme_entry.grid(row=r, column=1,pady=5)
        r = 2
        func_lb.grid(row=r, column=0,pady=5)
        func_entry.current(0)
        func_entry.grid(row=r, column=1,pady=5)
        r = 3
        empty_lb.grid(row=r, column=1,pady=5)
        r = 4
        save_address_lb.grid(row=r, column=0,pady=5,padx=20)
        save_address_entry.grid(row=r, column=1,pady=5)
        save_address_Button.grid(row=r, column=2,pady=5,padx=20)
        r += 1
        file_lb.grid(row=r, column=0,pady=5)
        file_entry.grid(row=r, column=1,pady=5)
        packButton.grid(row=r, column=2,pady=5)
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
        r = 11
        empty2_lb.grid(row=r, column=1,pady=10)
    def on_Guilang_select(event):
        global func_list_data,zdy,a0,info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24
        zdy,a0 = zdyconfig()
        if cGuilang_entry.get() == "中文简体":
            info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24 = zhguitext()
        if cGuilang_entry.get() == f"{zdy}":
            info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24 = zdyguitext()
        func_list_data =[f"{a17}",f"{a18}",f"{a19}",f"{a23}",f"{a15}"]
        file_lb.config(text=a1)
        saveButton.config(text=a16)
        mods_lb.config(text=a14)
        desc_lb.config(text=a13)
        name_lb.config(text=a12)
        authors_lb.config(text=a11)
        packButton.config(text=a10)
        save_address_lb.config(text=a9)
        save_address_Button.config(text=a10)
        save_address_vaule.set(a3)
        cGuilang_lb.config(text=a8)
        func_lb.config(text=a21)
        mods_vaule.set(a4)
        desc_vaule.set(a4)
        name_vaule.set(a4)
        authors_vaule.set(a4)
        File_vaule.set(a3)
        func_entry.configure(values=func_list_data)
        func_entry.current(0)
        GUIupdate()
    def on_sv_ttk_theme_select(event):
        if sv_ttk_theme_entry.get() == "Light":
            sv_ttk.use_light_theme()
        if sv_ttk_theme_entry.get() == "Dark":
            sv_ttk.use_dark_theme()
    def on_func_select(event):
        global r,packButton
        r=4
        file_entry.grid_forget()
        file_lb.grid_forget()
        packButton.grid_forget()
        langfile_entry.grid_forget()
        langfile_lb.grid_forget()
        langpackButton.grid_forget()
        authors_lb.grid_forget()
        authors_entry.grid_forget()
        name_lb.grid_forget()
        name_entry.grid_forget()
        desc_lb.grid_forget()
        desc_entry.grid_forget()
        mods_lb.grid_forget()
        mods_entry.grid_forget()
        saveButton.grid_forget()
        if func_entry.get() == f"{a17}" or func_entry.get() == f"{a18}":
            def browseStruct():
                File_vaule.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.txt *.TXT"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
                Vwo50xiexie()
            packButton = Button(root, text="%s" % (a10), command=browseStruct)
            r += 1
            file_lb.grid(row=r, column=0,pady=5)
            file_entry.grid(row=r, column=1,pady=5)
            packButton.grid(row=r, column=2,pady=5)
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
        if func_entry.get() == f"{a19}":
            def browseStruct():
                File_vaule.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.jar"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
            packButton = Button(root, text="%s" % (a10), command=browseStruct)
            r += 1
            file_lb.grid(row=r, column=0,pady=5)
            file_entry.grid(row=r, column=1,pady=5)
            packButton.grid(row=r, column=2,pady=5)
            r += 1
            saveButton.grid(row=r, column=2,pady=5,padx=20)
        if func_entry.get() == f"{a23}" or func_entry.get() == f"{a15}":
            global langmode
            if func_entry.get() == f"{a15}" and langFile_vaule.get() == f"{a4}":
                langFile_vaule.set(a3)
            if func_entry.get() == f"{a23}" and langFile_vaule.get() == f"{a3}":
                langFile_vaule.set(a4)
                langmode = False
            def browseStruct():
                File_vaule.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.json"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
            packButton = Button(root, text="%s" % (a10), command=browseStruct)
            r += 1
            file_lb.grid(row=r, column=0,pady=5)
            file_entry.grid(row=r, column=1,pady=5)
            packButton.grid(row=r, column=2,pady=5)
            r += 1
            langfile_lb.grid(row=r, column=0,pady=5)
            langfile_entry.grid(row=r, column=1,pady=5)
            langpackButton.grid(row=r, column=2,pady=5)
            r += 1
            saveButton.grid(row=r, column=2,pady=5,padx=20)
        GUIupdate()
    def GUIupdate():
        root.update()
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2) - 200
        root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
        root.update_idletasks()
        root.update()
    root = Tk()
    root.title("VPtool 3.0")
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    elif __file__:
        application_path = os.path.dirname(__file__)
    root.iconbitmap(default=os.path.join(application_path, '000.ico'))
    empty_lb = Label(root, text=" ✿－＿＾)✧  ✧(＾＿－✿ ")
    empty2_lb = Label(root, text="")
    # 处理的文件（txt配置、模组jar）
    File_vaule = StringVar(value="%s" % (a3))
    file_entry = Entry(root, textvariable=File_vaule)
    file_lb = Label(root, text="%s" % (a1))
    packButton = Button(root, text="%s" % (a10), command=browseStruct)
    # 附加处理文件（lang文件）
    langFile_vaule = StringVar(value="%s" % (a4))
    langfile_entry = Entry(root, textvariable=langFile_vaule)
    langfile_lb = Label(root, text="lang文件")
    langpackButton = Button(root, text="%s" % (a10), command=browselang)
    # 保存地址
    save_address_vaule = StringVar(value="%s" % (a3))
    save_address_lb = Label(root, text="%s" % (a9))
    save_address_entry = Entry(root, textvariable=save_address_vaule)
    save_address_Button = Button(root, text="%s" % (a10), command=browseaddress)
    # 作者
    authors_vaule = StringVar(value="%s" % (a4))
    authors_lb = Label(root, text="%s" % (a11))
    authors_entry = Entry(root, textvariable=authors_vaule)
    # 硬编码汉化名
    name_vaule = StringVar(value="%s" % (a4))
    name_lb = Label(root, text="%s" % (a12))
    name_entry = Entry(root, textvariable=name_vaule)
    # 描述
    desc_vaule = StringVar(value="%s" % (a4))
    desc_lb = Label(root, text="%s" % (a13))
    desc_entry = Entry(root, textvariable=desc_vaule)
    # 汉化的模组
    mods_vaule = StringVar(value="%s" % (a4))
    mods_lb = Label(root, text="%s" % (a14))
    mods_entry = Entry(root, textvariable=mods_vaule)
    # Gui语言
    cGuilang_lb = Label(root, text="%s" % (a8))
    Guilang_list = ["中文简体",f"{zdy}"]
    cGuilang_entry = Combobox(root,state="readonly", values=Guilang_list)
    cGuilang_entry.bind("<<ComboboxSelected>>", on_Guilang_select)
    # GUI主体
    sv_ttk_theme_lb = Label(root, text="%s" % (a22))
    sv_ttk_theme_list = ["Light","Dark"]
    sv_ttk_theme_entry = Combobox(root,state="readonly", values=sv_ttk_theme_list)
    sv_ttk_theme_entry.bind("<<ComboboxSelected>>", on_sv_ttk_theme_select)
    # 功能选择
    func_lb = Label(root, text="%s" % (a21))
    func_list = [f"{a17}",f"{a18}",f"{a19}",f"{a23}",f"{a15}"]
    func_entry = Combobox(root,state="readonly", values=func_list)
    func_entry.bind("<<ComboboxSelected>>", on_func_select)
    # 运行功能模块
    def runfunc():
        global langmode
        iscanrun = True
        langmode = False
        if File_vaule.get() and save_address_vaule.get() == "%s" % (a3) or len(File_vaule.get() and save_address_vaule.get()) == 0:
            dialogs.show_message("ERROR", "%s" % (a5))
            iscanrun = False
        else:
            if File_vaule.get() == "%s" % (a3) or len(File_vaule.get()) == 0:
                dialogs.show_message("ERROR", "%s" % (a6))
                iscanrun = False
            if save_address_vaule.get() == "%s" % (a3) or len(save_address_vaule.get()) == 0:
                dialogs.show_message("ERROR", "%s" % (a7))
                iscanrun = False
            if func_entry.get() == f"{a15}" and langFile_vaule.get() == f"{a3}" or func_entry.get() == f"{a15}" and len(langFile_vaule.get()) == 0:
                dialogs.show_message("ERROR", f"{a24}")
                iscanrun = False
        if iscanrun != False:
            if func_entry.get() == f"{a23}" and not langFile_vaule.get() == f"{a4}":
                langmode = True
            if func_entry.get() == f"{a17}":
                print (f"{a20}{a17}")
                tc(save_address_vaule.get(),File_vaule.get(),cGuilang_entry.get(),authors_vaule.get(),name_vaule.get(),desc_vaule.get(),mods_vaule.get())
            if func_entry.get() == f"{a18}":
                print (f"{a20}{a18}")
                tca(save_address_vaule.get(),File_vaule.get(),cGuilang_entry.get(),authors_vaule.get(),name_vaule.get(),desc_vaule.get(),mods_vaule.get())
            if func_entry.get() == f"{a19}":
                print (f"{a20}{a19}")
                lse(save_address_vaule.get(),File_vaule.get(),cGuilang_entry.get())
            if func_entry.get() == f"{a23}":
                print (f"{a20}{a23}")
                cre(langmode,save_address_vaule.get(),File_vaule.get(),cGuilang_entry.get(),langFile_vaule.get())
            if func_entry.get() == f"{a15}":
                print (f"{a20}{a15}")
                kmm(False,save_address_vaule.get(),File_vaule.get(),cGuilang_entry.get(),langFile_vaule.get())
    saveButton = Button(root, text="%s" % (a16), command=runfunc)
    box_checked()
    root.update_idletasks()
    sv_ttk.use_light_theme()
    GUIupdate()
    dialogs.show_message('VPtool-3.0-welcome',info)
    root.mainloop()