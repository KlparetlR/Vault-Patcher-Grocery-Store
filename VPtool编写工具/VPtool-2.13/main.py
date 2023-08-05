"""
*-*<适配版本：1.2.10+>*-*
项目地址：https://github.com/KlparetlR/Vault-Patcher-Grocery-Store/blob/main/VPtool%E7%BC%96%E5%86%99%E5%B7%A5%E5%85%B7/
专门为VP模组而生的配置编写工具（https://github.com/3093FengMing/VaultPatcher ）
作者及版权方：晴笙墨染（莫安）、KlparetlR、捂脸Wulian、3093FengMing, 技术辅助：XDawned
Fabric通用（https://github.com/LocalizedMC/HardcodeTextPatcher-Fabric ）
弹窗使用https://github.com/rdbende/Sun-Valley-messageboxes
"""
from tkinter import filedialog, StringVar, Tk
from tkinter.ttk import Button, Label, Entry,Combobox
import os,dialogs,sv_ttk,ctypes
from LANG import zhguitext,zdyconfig,zdyguitext
from func import tca,lse,tc

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
        func_lb.config(text=a21)
        mods_vaule.set(a4)
        desc_vaule.set(a4)
        name_vaule.set(a4)
        authors_vaule.set(a4)
        icon_var.set(a3)
        FileGUI.set(a3)
        func_entry.configure(values=func_list_data)
        func_entry.current(0)
        if sv_ttk_theme_entry.get() == "Light":
            sv_ttk.use_light_theme()
        if sv_ttk_theme_entry.get() == "Dark":
            sv_ttk.use_dark_theme()
    def runlangGui():
        global zdy,a0,info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,langcurrent
        zdy,a0 = zdyconfig()
        if vaulelang == "0x804":
           info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22 = zhguitext()
           def langcurrent():
               cGuilang_entry.current(0)
        if vaulelang == f"{a0}":
           info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22 = zdyguitext()
           def langcurrent():
               cGuilang_entry.current(2)
    runlangGui()
    def runclangGui():
        global func_list_data,zdy,a0,info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22
        zdy,a0 = zdyconfig()
        if cGuilang_entry.get() == "中文简体":
            info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22 = zhguitext()
            func_list_data =[f"{a17}",f"{a18}",f"{a19}"]
        if cGuilang_entry.get() == f"{zdy}":
            info,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22 = zdyguitext()
            func_list_data =[f"{a17}",f"{a18}",f"{a19}"]
        updateGui()
        root.update()
    def browseStruct():
        FileGUI.set(filedialog.askopenfilename(filetypes=(("%s" % (a1), "*.txt *.TXT *.jar"),),initialdir=os.path.abspath(os.path.dirname(__file__))))
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
        sv_ttk_theme_lb.grid(row=r, column=0,pady=5)
        sv_ttk_theme_entry.current(0)
        sv_ttk_theme_entry.grid(row=r, column=1,pady=5)
        r += 1
        func_lb.grid(row=r, column=0,pady=5)
        func_entry.current(0)
        func_entry.grid(row=r, column=1,pady=5)
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
        saveButton.grid(row=r, column=2,pady=45,padx=20)
    def runFromGui():
        if FileGUI.get() and icon_var.get() == "%s" % (a3) or len(FileGUI.get() and icon_var.get()) == 0:
            dialogs.show_message("ERROR", "%s" % (a5))
        else:
            if FileGUI.get() == "%s" % (a3) or len(FileGUI.get()) == 0:
                dialogs.show_message("ERROR", "%s" % (a6))
            if icon_var.get() == "%s" % (a3) or len(icon_var.get()) == 0:
                dialogs.show_message("ERROR", "%s" % (a7))
        if func_entry.get() == f"{a17}":
            print (f"{a20}{a17}")
            tc(icon_var.get(),FileGUI.get(),cGuilang_entry.get(),authors_vaule,name_vaule,desc_vaule,mods_vaule)
        if func_entry.get() == f"{a18}":
            print (f"{a20}{a18}")
            tca(icon_var.get(),FileGUI.get(),cGuilang_entry.get(),authors_vaule,name_vaule,desc_vaule,mods_vaule)
        if func_entry.get() == f"{a19}":
            print (f"{a20}{a19}")
            lse(icon_var.get(),FileGUI.get(),cGuilang_entry.get())
    root = Tk()
    root.title("VPtool 2.13")
    cGuilang_lb = Label(root, text="%s" % (a8))
    combo_list = ["中文简体",f"{zdy}"]
    empty_lb = Label(root, text=" ✿－＿＾)✧✧(＾＿－✿ ")
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
    func_lb = Label(root, text="%s" % (a21))
    func_list = [f"{a17}",f"{a18}",f"{a19}"]
    func_entry = Combobox(root,state="readonly", values=func_list)
    sv_ttk_theme_lb = Label(root, text="%s" % (a22))
    sv_ttk_theme_list = ["Light","Dark"]
    sv_ttk_theme_entry = Combobox(root,state="readonly", values=sv_ttk_theme_list)
    box_checked()
    root.update_idletasks()
    sv_ttk.use_light_theme()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2) - 200
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    root.resizable(False, False)
    dialogs.show_message('VPtool-welcome',info)
    root.mainloop()