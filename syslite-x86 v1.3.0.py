#!/usr/bin/env python3
import tkinter as tk
import subprocess
from tkinter import messagebox 
from tkinter import scrolledtext
from tkinter import simpledialog
import threading
import ttkbootstrap as ttk1
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import os
from tkinter import filedialog
import sys
import json
from collections import OrderedDict
import shutil
from ttkbootstrap.widgets.scrolled import ScrolledText
from ttkbootstrap_icons_bs import BootstrapIcon
from PIL import Image,ImageTk
import ssl
import urllib.request
import webbrowser
import psutil


# =================================================================================================
# 检测桌面环境,根据对应的桌面打开终端，然后执行命令。多个地方引用了该函数的代码。
# =================================================================================================
def jiance():
    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
    if "gnome" in desktop :
        subprocess.run(["gnome-terminal","--","bash","-c","pwd; exec bash"])	
    elif "kde" in desktop :
        subprocess.run(["konsole","-e","bash","-c","pwd; exec bash"])	
    elif "xfce" in desktop :
        subprocess.run(["xfce4-terminal","-x","bash","-c","echo hello; exec bash"])	 
    elif "mate" in desktop :
        subprocess.run(["mate-terminal","-x","bash","-c","pwd; exec bash"])	
    else:
        Messagebox.show_info("命令无法执行","提示")

# =================================================================================================
# 版本检测模块,打开工具时,联网查询gitee上的版本号文件,与当前版本号对比，如果不同弹出消息框提醒更新
# =================================================================================================

nowversion="v1.3.0" #当前版本号
url="https://gitee.com/veyne0/small-tool/raw/master/%E7%89%88%E6%9C%AC.txt" #版本号文件链接
def gengxin():
    try :
        
        ssl._create_dafault_https_context=ssl._create_unverified_context
        banben=urllib.request.urlopen(url,timeout=3)
        banbenhao=banben.read().decode().strip('"')
        if banbenhao != nowversion:
            print(banbenhao)
            print(nowversion)
            os.system(f'notify-send "syslite提醒" "检测到新的版本{banbenhao}" -i system-update -t 20000 ')
    except Exception as e:
        print(e)
gengxin()

# ===============================================================
# json配置模块,保存自定义命令,脚本,主题的信息
# ===============================================================
def peizhi():
     """
    加载并合并系统配置文件（默认配置 + 用户自定义配置）
    逻辑：
    1. 优先读取用户目录 ~/.config/small-tool/配置.json；    (small-tool是工具之前的名字)
    2. 若用户配置不存在，复制默认配置（同目录下的配置.json）到用户目录；
    3. 若用户配置存在，合并默认配置（补充用户配置中缺失的键）；
    4. 最终返回合并后的有序字典配置
    
    Returns:
        OrderedDict: 合并后的配置字典（保留键的顺序）
    """
    global configshezhi
    default=os.path.join(os.path.dirname(__file__),"配置.json")
    user_configdir=os.path.expanduser("~/.config/small-tool")
    os.makedirs(user_configdir,exist_ok=True)
    configshezhi=os.path.join(user_configdir,"配置.json")
    if os.path.exists(configshezhi) :
        with open(configshezhi,"r",encoding="utf-8",) as f1:
            config=json.load(f1,object_pairs_hook=OrderedDict)
        if os.path.exists(default):
            with open(configshezhi,"r",encoding="utf-8",) as f1:
                config=json.load(f1,object_pairs_hook=OrderedDict)
                with open(default,"r",encoding="utf-8",) as f1:
                    default_config=json.load(f1,object_pairs_hook=OrderedDict)
                    mergedconfig=OrderedDict()
                    for key ,value in config.items():
                        mergedconfig[key]=value
               
                    for key ,value in default_config.items():
                        if key not in mergedconfig:
                            mergedconfig[key]=value
                    with open(configshezhi,"w",encoding="utf-8",) as f1:
                        json.dump(mergedconfig,f1,ensure_ascii=False,indent=2)
                        return mergedconfig
    else:
        shutil.copy(default,configshezhi)
config=peizhi()


# ===============================================================
# 获取json配置中固定位置的键值对,总共19个键值对。
# ===============================================================
key_list=list(config.keys())
value_list=list(config.values())
targetkey1=key_list[1]
value1=value_list[1]
targetkey2=key_list[2]
value2=value_list[2]
targetkey3=key_list[3]
value3=value_list[3]
targetkey4=key_list[4]
value4=value_list[4]
targetkey5=key_list[5]
value5=value_list[5]
targetkey6=key_list[6]
value6=value_list[6]
targetkey7=key_list[7]
value7=value_list[7]
targetkey8=key_list[8]
value8=value_list[8]
targetkey9=key_list[9]
value9=value_list[9]
targetkey10=key_list[10]
value10=value_list[10]
targetkey11=key_list[11]
value11=value_list[11]
targetkey12=key_list[12]
value12=value_list[12]
targetkey13=key_list[13]
value13=value_list[13]
targetkey14=key_list[14]
value14=value_list[14]
targetkey15=key_list[15]
value15=value_list[15]
targetkey16=key_list[16]
value16=value_list[16]
targetkey17=key_list[17]
value17=value_list[17]
targetkey18=key_list[18]
value18=value_list[18]

# ==================================================================================================================
# 自定义命令功能,对应json中6个固定位置的键值对,编号1-6对应这个6个键值对的位置，每次添加或修改命令时会根据编号更改对应位置上的键值对
# ==================================================================================================================
def tianjia():
    """添加自定义命令"""

    global config
    shuju1=entryzi0.get()
    shuju2=entryzi1.get()
    shuju3=entryzi2.get()
    if "1"  in shuju1 or "2"  in shuju1 or "3"  in shuju1 or "4"  in shuju1 or "5"  in shuju1 or "6"  in shuju1 :
        if shuju2 != "":
            if shuju3 != "":
               if shuju1 =="1":
                  if targetkey1 in config:
                       del config[targetkey1]
                  items1=list(config.items())
                  items1.insert(1,(shuju2,shuju3))
                  config=OrderedDict(items1)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shuju1 =="2":
                  if targetkey2 in config:
                       del config[targetkey2]
                  items2=list(config.items())
                  items2.insert(2,(shuju2,shuju3))
                  config=OrderedDict(items2)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shuju1 =="3":
                  if targetkey3 in config:
                       del config[targetkey3]
                  items3=list(config.items())
                  items3.insert(3,(shuju2,shuju3))
                  config=OrderedDict(items3)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shuju1 =="4":
                  if targetkey4 in config:
                       del config[targetkey4]
                  items4=list(config.items())
                  items4.insert(4,(shuju2,shuju3))
                  config=OrderedDict(items4)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shuju1 =="5":
                  if targetkey5 in config:
                       del config[targetkey5]
                  items5=list(config.items())
                  items5.insert(5,(shuju2,shuju3))
                  config=OrderedDict(items5)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shuju1 =="6":
                  if targetkey6 in config:
                       del config[targetkey6]
                  items6=list(config.items())
                  items6.insert(6,(shuju2,shuju3))
                  config=OrderedDict(items6)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
            else:
                Messagebox.show_info("请输入命令代码","提示")

        else:
            Messagebox.show_info("请输入命令名称","提示")
    else:
         Messagebox.show_info("命令编号只能填1-6中的一个数字","提示") 
def xiugai():
    """修改自定义命令"""
    global config
    shuju1=entryzi0.get()
    shuju2=entryzi1.get()
    shuju3=entryzi2.get()
    if "1"  in shuju1 or "2"  in shuju1 or "3"  in shuju1 or "4"  in shuju1 or "5"  in shuju1 or "6"  in shuju1 :
        if shuju2 != "":
            if shuju3 != "":
               if shuju1 =="1":
                  if targetkey1 in config:
                       del config[targetkey1]
                  items1=list(config.items())
                  items1.insert(1,(shuju2,shuju3))
                  config=OrderedDict(items1)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shuju1 =="2":
                  if targetkey2 in config:
                       del config[targetkey2]
                  items2=list(config.items())
                  items2.insert(2,(shuju2,shuju3))
                  config=OrderedDict(items2)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shuju1 =="3":
                  if targetkey3 in config:
                       del config[targetkey3]
                  items3=list(config.items())
                  items3.insert(3,(shuju2,shuju3))
                  config=OrderedDict(items3)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shuju1 =="4":
                  if targetkey4 in config:
                       del config[targetkey4]
                  items4=list(config.items())
                  items4.insert(4,(shuju2,shuju3))
                  config=OrderedDict(items4)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shuju1 =="5":
                  if targetkey5 in config:
                       del config[targetkey5]
                  items5=list(config.items())
                  items5.insert(5,(shuju2,shuju3))
                  config=OrderedDict(items5)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shuju1 =="6":
                  if targetkey6 in config:
                       del config[targetkey6]
                  items6=list(config.items())
                  items6.insert(6,(shuju2,shuju3))
                  config=OrderedDict(items6)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
            else:
                Messagebox.show_info("请输入命令代码","提示")

        else:
            Messagebox.show_info("请输入命令名称","提示")
    else:
         Messagebox.show_info("命令编号只能填1-6中的一个数字","提示")

#函数minglin1到minglin6,分别执行6个自定义命令    
def minglin1():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value1}; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"{value1}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"{value1}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"{value1}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value1}; exec bash"])
def minglin2():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value2}; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"{value2}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"{value2}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"{value2}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value2}; exec bash"])
def minglin3():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value3}; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"{value3}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"{value3}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"{value3}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value3}; exec bash"])
def minglin4():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value4}; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"{value4}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"{value4}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"{value4}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value4}; exec bash"])
def minglin5():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value5}; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"{value5}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"{value5}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"{value5}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value5}; exec bash"])
def minglin6():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value6}; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"{value6}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"{value6}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"{value6}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"{value6}; exec bash"])

#函数yushe1到yushe4提供4个预设命令(可以一键添加的自定义命令)
def yushe1():
    if entryzi0.get() =="":
        entryzi0.insert(0,"1")
    else:
        entryzi0.delete(0,tk.END)
        entryzi0.insert(0,"1")
    if entryzi1.get() == "":
        entryzi1.insert(0,"检查软件包更新")
    else:
        entryzi1.delete(0,tk.END)
        entryzi1.insert(0,"检查软件包更新")
    if entryzi2.get() == "":
        entryzi2.insert(0,"sudo apt update") 
    else:
        entryzi2.delete(0,tk.END)
        entryzi2.insert(0,"sudo apt update")
def yushe2():
    if entryzi0.get() =="":
        entryzi0.insert(0,"2")
    else:
        entryzi0.delete(0,tk.END)
        entryzi0.insert(0,"2")
    if entryzi1.get() == "":
        entryzi1.insert(0,"更新软件包")
    else:
        entryzi1.delete(0,tk.END)
        entryzi1.insert(0,"更新软件包")
    if entryzi2.get() == "":
        entryzi2.insert(0,"sudo apt upgrade") 
    else:
        entryzi2.delete(0,tk.END)
        entryzi2.insert(0,"sudo apt upgrade")  
def yushe3():
    if entryzi0.get() =="":
        entryzi0.insert(0,"3")
    else:
        entryzi0.delete(0,tk.END)
        entryzi0.insert(0,"3")
    if entryzi1.get() == "":
        entryzi1.insert(0,"查看运行进程")
    else:
        entryzi1.delete(0,tk.END)
        entryzi1.insert(0,"查看运行进程")
    if entryzi2.get() == "":
        entryzi2.insert(0,"ps aux") 
    else:
        entryzi2.delete(0,tk.END)
        entryzi2.insert(0,"ps aux") 
def yushe4():
    if entryzi0.get() =="":
        entryzi0.insert(0,"4")
    else:
        entryzi0.delete(0,tk.END)
        entryzi0.insert(0,"4")
    if entryzi1.get() == "":
        entryzi1.insert(0,"测试网络")
    else:
        entryzi1.delete(0,tk.END)
        entryzi1.insert(0,"测试网络")
    if entryzi2.get() == "":
        entryzi2.insert(0,"ping baidu.com") 
    else:
        entryzi2.delete(0,tk.END)
        entryzi2.insert(0,"ping baidu.com")    

# ===============================================
# 修改主题模块
# ===============================================
def xuanzhuti():
    selectzhuti=choice1.get()
    if selectzhuti == 1:
        config["style"]="darkly"
        with open(configshezhi,"w",encoding="utf-8") as f1:
            json.dump(config,f1,ensure_ascii=False,indent=2)
        Messagebox.show_info("主题切换完成，程序重启后生效","提示")
    if selectzhuti == 2:
        config["style"]="yeti"
        with open(configshezhi,"w",encoding="utf-8") as f1:
            json.dump(config,f1,ensure_ascii=False,indent=2)
        Messagebox.show_info("主题切换完成，程序重启后生效","提示")
    if selectzhuti == 3:
        config["style"]="cosmo"
        with open(configshezhi,"w",encoding="utf-8") as f1:
            json.dump(config,f1,ensure_ascii=False,indent=2)
        Messagebox.show_info("主题切换完成，程序重启后生效","提示")
    if selectzhuti == 4:
        config["style"]="sandstone"
        with open(configshezhi,"w",encoding="utf-8") as f1:
            json.dump(config,f1,ensure_ascii=False,indent=2)
        Messagebox.show_info("主题切换完成，程序重启后生效","提示")

# ===============================================
# 第一个界面,常用功能模块，
# ===============================================
def get1():
    """获取系统信息"""

    result = subprocess.run("uname -a",shell=True,capture_output=True,text=True)
    messagebox.showinfo("系统信息",result.stdout)
def get2():
    """获取CPU信息"""

    result = subprocess.run("lscpu | sed -n '/Model name/p'",shell=True,capture_output=True,text=True)
    messagebox.showinfo("CPU信息",result.stdout)
def get3():
    """清理缓存"""
    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
    if "gnome" in desktop :
        subprocess.run(["gnome-terminal","--","bash","-c","pkexec apt autoclean; exec bash"])	
    elif "kde" in desktop :
        subprocess.run(["konsole","-e","bash","-c","pkexec apt autoclean; exec bash"])	
    elif "xfce" in desktop :
        subprocess.run(["xfce4-terminal","-x","bash","-c","pkexec apt autoclean; exec bash"])	 
    elif "mate" in desktop :
        subprocess.run(["mate-terminal","-x","bash","-c","pkexec apt autoclean; exec bash"])	
    else:
        subprocess.run(["gnome-terminal","--","bash","-c","pkexec apt autoclean; exec bash"])	  
      
def get4():
    """获取显卡信息"""

    result = subprocess.run("lspci | sed -n '/VGA/p'",shell=True,capture_output=True,text=True)
    messagebox.showinfo("显卡信息",result.stdout)
def get5():
    """获取硬盘空间信息"""

    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
    if "gnome" in desktop :
        subprocess.run(["gnome-terminal","--","bash","-c","df -h; exec bash"])	
    elif "kde" in desktop :
        subprocess.run(["konsole","-e","bash","-c","df -h; exec bash"])	
    elif "xfce" in desktop :
        subprocess.run(["xfce4-terminal","-x","bash","-c","df -h; exec bash"])	 
    elif "mate" in desktop :
        subprocess.run(["mate-terminal","-x","bash","-c","df -h; exec bash"])	
    else:
        subprocess.run(["gnome-terminal","--","bash","-c","df -h; exec bash"])
def get6():
    """更新软件包"""

    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
    if "gnome" in desktop :
        subprocess.run(["gnome-terminal","--","bash","-c","pkexec apt upgrade; exec bash"])	
    elif "kde" in desktop :
        subprocess.run(["konsole","-e","bash","-c","pkexec apt upgrade; exec bash"])	
    elif "xfce" in desktop :
        subprocess.run(["xfce4-terminal","-x","bash","-c","pkexec apt upgrade; exec bash"])	 
    elif "mate" in desktop :
        subprocess.run(["mate-terminal","-x","bash","-c","pkexec apt upgrade; exec bash"])	
    else:
        subprocess.run(["gnome-terminal","--","bash","-c","pkexec apt upgrade; exec bash"])	 

def select_file():
    """执行脚本"""

    file_path=filedialog.askopenfilename(title="选择脚本文件",filetypes=[("所有文件","*.*")])
    if file_path:
        filename=os.path.basename(file_path)
        dir_path=os.path.dirname(file_path)
	   
    if "sh" not in file_path:
	       Messagebox.show_info("请选择脚本文件","提示")
	       return
    else:
           desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
           if "gnome" in desktop :
                            subprocess.run(["gnome-terminal","--","bash","-c",f"cd '{dir_path}'&& chmod +x '{filename}' && ./'{filename}'; exec bash"])	
           elif "kde" in desktop :
                            subprocess.run(["konsole","-e","bash","-c",f"cd '{dir_path}'&& chmod +x '{filename}' && ./'{filename}'; exec bash"])	
           elif "xfce" in desktop :
                            subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd '{dir_path}'&& chmod +x '{filename}' && ./'{filename}'; exec bash"])	 
           elif "mate" in desktop :
                            subprocess.run(["mate-terminal","-x","bash","-c",f"cd '{dir_path}'&& chmod +x '{filename}' && ./'{filename}'; exec bash"])	
           else:
                     subprocess.run(["gnome-terminal","--","bash","-c",f"cd '{dir_path}'&& chmod +x '{filename}' && ./'{filename}'; exec bash"])
def anzhuang():
    """安装deb包"""

    file_path1=filedialog.askopenfilename(title="选择要安装的deb包",filetypes=[("deb文件",".deb")])
    if file_path1:
        file_name1=os.path.basename(file_path1)
        dir_name1=os.pathh.dirmane(file_path1)
        desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
        if "gnome" in desktop :
                            subprocess.run(["gnome-terminal","--","bash","-c",f"cd '{dir_path1}' && pkexec dpkg -i ./'{file_name1}'; exec bash"])	
        elif "kde" in desktop :
                            subprocess.run(["konsole","-e","bash","-c",f"cd '{dir_path1}'&& pkexec dpkg -i ./'{file_name1}'; exec bash"])	
        elif "xfce" in desktop :
                            subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd '{dir_path1}'&& pkexec dpkg -i ./'{file_name1}'; exec bash"])	 
        elif "mate" in desktop :
                            subprocess.run(["mate-terminal","-x","bash","-c",f"cd '{dir_path1}'&& pkexec dpkg -i ./'{file_name1}'; exec bash"])	
        else:
                     subprocess.run(["gnome-terminal","--","bash","-c",f"cd '{dir_path1}' && pkexec dpkg -i ./'{file_name1}'; exec bash"])    
def yilai():
    """修复依赖"""

    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
    if "gnome" in desktop :
        subprocess.run(["gnome-terminal","--","bash","-c","pkexec apt install -f; exec bash"])	
    elif "kde" in desktop :
        subprocess.run(["konsole","-e","bash","-c","pkexec apt install -f; exec bash"])	
    elif "xfce" in desktop :
        subprocess.run(["xfce4-terminal","-x","bash","-c","pkexec apt install -f; exec bash"])	 
    elif "mate" in desktop :
        subprocess.run(["mate-terminal","-x","bash","-c","pkexec apt install -f; exec bash"])	
    else:
        subprocess.run(["gnome-terminal","--","bash","-c","pkexec apt install -f; exec bash"]) 
# =============================================================
# 右键菜单模块,添加右键,复制,粘贴,剪切功能
# =============================================================
def right_menu(widget):
   menu=ttk1.Menu(widget,tearoff=0)
   menu.add_command(label="复制",command=lambda:widget.event_generate("<<Copy>>")) 
   menu.add_command(label="粘贴",command=lambda:widget.event_generate("<<Paste>>")) 
   menu.add_command(label="剪切",command=lambda:widget.event_generate("<<Cut>>"))
   def show(event):
       menu.post(event.x_root,event.y_root)
   widget.bind("<Button-3>",show)
   def hide_menu(event):
          menu.unpost()
   widget.winfo_toplevel().bind("<Button-1>",hide_menu)


# =============================================================
# 清理垃圾,检测硬盘模块
# =============================================================
def yong():
    """清理用户缓存"""

    cmd01="rm -rf ~/.cache/*"
    result01=subprocess.run(cmd01,shell=True,capture_output=True,text=True)
    if result01.returncode == 0 :
        saomiao()
        yingpan()
        framexi1.update_idletasks()
    else:
        Messagebox.show_info("清理失败","提示")
def hushou():
    """清理回收站"""

    cmd02="rm -rf ~/.local/share/Trash/files/*"
    result02=subprocess.run(cmd02,shell=True,capture_output=True,text=True)
    if result02.returncode == 0 :
        saomiao()
        yingpan()
        framexi1.update_idletasks()
    else:
        Messagebox.show_info("清理失败","提示")
def qingliapt():
    """清理apt缓存"""
    
    cmd03="pkexec apt clean"
    result03=subprocess.run(cmd03,shell=True,capture_output=True,text=True)
    if result03.returncode == 0 :
        saomiao()
        yingpan()
        framexi1.update_idletasks()
    else:
        Messagebox.show_info("清理失败","提示")
    
def yingpan():
    """通过linux终端命令,psutil库获取硬盘总容量,硬盘已使用空间,硬盘使用率"""

    global result6
    global result06
    global result07
    global result08
    global result09
    global result010
    cmd6="df -hP | awk -F'[% ]+' '$6 == \"/\" {print $5}'"
    result6=subprocess.run(cmd6,shell=True,capture_output=True,text=True)
    result06=float(result6.stdout)
    if result06 > 80:
        os.system('notify-send "syslite提醒" "您的硬盘空间不足20%" -i system-update -t 10000 ')

    disk_partitions=psutil.disk_partitions()
    for partitions in disk_partitions:
        if  partitions.mountpoint in ['/','/home','/boot'] :
            try:
                disk_usage=psutil.disk_usage(partitions.mountpoint)
                result07=disk_usage.total / 1024 / 1024 / 1024
                resultd8=disk_usage.used / 1024 / 1024 / 1024
                resultd10=disk_usage.percent
                result08=round(float(resultd8),1)
                resultd9=result07-result08
                result09=round(float(resultd9),1)
                result010=round(float(resultd10),1)
                labelyi["text"]=f"已用大小:{result08}GB"
                labelsheng["text"]=f"剩余大小:{result09}GB"
            except:
                pass
def dx():
    """通过linux终端命令获取硬盘的读写速度"""
    global result0w
    global result0r
    cmdwrite='''
temp_file=$(mktemp) && \
write_speed=$(dd if=/dev/zero of="$temp_file" bs=100M count=1 oflag=direct 2>&1 | grep -oE '[0-9.]+ MB/s' | awk '{print $1}') && \
echo ${write_speed:-0} && \
rm -f "$temp_file"
'''
    resultw=subprocess.run(cmdwrite,shell=True,capture_output=True,text=True)
    cmdr='''
temp_file=$(mktemp) && \
dd if=/dev/zero of="$temp_file" bs=100M count=1 oflag=direct > /dev/null 2>&1 && \
read_speed=$(dd if="$temp_file" of=/dev/null bs=100M count=1 iflag=direct 2>&1 | grep -oE '[0-9.]+ MB/s' | awk '{print $1}') && \
echo ${read_speed:-0} && \
rm -f "$temp_file"
'''
    resultr=subprocess.run(cmdr,shell=True,capture_output=True,text=True)
    result0w=float(resultw.stdout)
    result0r=float(resultr.stdout)
    meter5=ttk1.Meter(framexi1,padding=10,metersize=160,amountused=result0w,amountformat="{:.1f}MB",metertype="full",subtext="硬盘写入速度",interactive=False,bootstyle="INFO")
    meter5.place(x=600,y=80)
    meter6=ttk1.Meter(framexi1,padding=10,metersize=160,amountused=result0r,amountformat="{:.1f}MB",metertype="full",subtext="硬盘读取速度",interactive=False,bootstyle="INFO")
    meter6.place(x=900,y=80)
yingpan()

def saomiao():
    """通过linux终端命令获取用户缓存,回收站中文件大小,apt缓存"""
    global result1
    global result2
    global result3
    global result4
    global result5
        
    cmd1="du -sh ~/.cache/ | cut -f1"
    result1=subprocess.run(cmd1,shell=True,capture_output=True,text=True)
    cmd2="du -sh ~/.local/share/Trash/ | cut -f1"
    result2=subprocess.run(cmd2,shell=True,capture_output=True,text=True)
    cmd3="du -sh /var/cache/apt/archives | cut -f1"
    result3=subprocess.run(cmd3,shell=True,capture_output=True,text=True)
    cmd4="df -hP | awk '$6 == \"/\" {print $3}'"
    result4=subprocess.run(cmd4,shell=True,capture_output=True,text=True)
    cmd5="df -hP | awk '$6 == \"/\" {print $4}'"
    result5=subprocess.run(cmd5,shell=True,capture_output=True,text=True)
        
    labelhuan["text"]=f"用户缓存大小为:{result1.stdout}"
    labelhu["text"]=f"回收站中文件大小为:{result2.stdout}"
    labelapt["text"]=f"apt缓存大小为:{result3.stdout}"
        
    if "G" in result1.stdout:
        try :
                os.system(f'notify-send "syslite提醒" "您的用户缓存已达到{result1.stdout}" -i system-update -t 10000 ')
        except:
            pass
    if "G" in result3.stdout:
        try:
            os.system(f'notify-send "syslite提醒" "您的apt缓存已达到{result3.stdout}" -i system-update -t 10000 ')  
        except:
            pass  

# ===================
# 我的账号链接
# ===================
def web1():
    webbrowser.open_new_tab("https://www.zhihu.com/people/veyne-53")
def web2():
    webbrowser.open_new_tab("https://gitee.com/veyne0/small-tool")
def web3():
    webbrowser.open_new_tab("https://profile.zjurl.cn/rogue/ugc/profile/?app=news_article&category_new=profile&module_name=Android_tt_url&share_did=MS4wLjACAAAA5NvtIWGtzXmiEVgnkJ22fTp1hadpU55UozVzTNBbPB2lpHmQcEpxcecZpI3QsQkr&share_token=70413c89-5bad-42fb-816e-0d6859c8f0f9&share_uid=MS4wLjABAAAA0msxFyrvtZxfYiVEzpcuke6b9_aUrv1oJnMOukir_1H2j4cZa0yHE781UbtsE6SW&timestamp=1770794331&tt_from=copy_link&upstream_biz=Android_url&user_id=3256085538669162&utm_campaign=client_share&utm_medium=toutiao_android&utm_source=copy_link")

    
# ===========================================================
# 程序的主界面,以及一些组件
# ===========================================================
window=ttk1.Window(themename=config["style"])
window.title("syslite v1.3.0")
window.geometry("1200x1200")
window.resizable(True,True)
style1=ttk1.Style()
style1.configure("TNotebook")
style1.configure("TNotebook.Tab",tabposition="n",padding=(8,0,8,0),width=12,anchor=N,margin=0,borderwidth=0)
style1.configure("TNotebook",padding=(0,0,0,0))
notebook = ttk1.Notebook(window,style="TNotebook")
icon1=BootstrapIcon("gear",size=30)
icon2=BootstrapIcon("cpu",size=30)
icon3=BootstrapIcon("trash",size=30)
icon4=BootstrapIcon("play",size=30)
icon5=BootstrapIcon("display",size=30)
icon6=BootstrapIcon("hdd-stack",size=30)
icon7=BootstrapIcon("arrow-clockwise",size=30)
icon8=BootstrapIcon("box-seam",size=30)
icon9=BootstrapIcon("house",size=15)
icon10=BootstrapIcon("trash3",size=15)
icon12=BootstrapIcon("info-circle",size=15)
icon13=BootstrapIcon("window",size=15)
icon14=BootstrapIcon("terminal",size=15)
icon15=BootstrapIcon("code",size=15)
icon16=BootstrapIcon("file-code",size=15)
icon17=BootstrapIcon("server",size=15)
icon18=BootstrapIcon("sliders",size=15)
icon19=BootstrapIcon("info-square",size=15)
iconsave=BootstrapIcon("plus",size=30)
iconxiugai=BootstrapIcon("pencil",size=30)
iconj=BootstrapIcon("play-circle",size=30)
iconfile=BootstrapIcon("file-earmark",size=30)
iconxiufu=BootstrapIcon("wrench",size=30)
iconxuanze=BootstrapIcon("check",size=30)
frame1= ttk1.Frame(notebook)
framexi1=ttk1.Frame(notebook)
framexi3=ttk1.Frame(notebook)
framexi4=ttk1.Frame(notebook)
frame_wine= ttk1.Frame(notebook)
frame4= ttk1.Frame(notebook)
frame5= ttk1.Frame(notebook)
framej=ttk1.Frame(notebook)
frameq=ttk1.Frame(notebook)
frameshezhi=ttk1.Frame(notebook)
frame6=ttk1.Frame(notebook)
label1=tk.Label(frame1,text="常用功能")
label1.place()
notebook.add(frame1,text="常用功能")
notebook.add(framexi1,text="清理垃圾")
notebook.add(framexi3,text="系统信息")
notebook.add(frame_wine,text="查看日志")
notebook.add(frame4,text="添加自定义命令")
notebook.add(frame5,text="自定义命令")
notebook.add(framej,text="自定义脚本")
notebook.add(framexi4,text="服务管理")
notebook.add(frameq,text="权限管理")
notebook.add(frameshezhi,text="设置")
notebook.add(frame6,text="关于")
notebook.pack(expand=True,fill=BOTH)
labella=ttk1.Label(framexi1,text="扫描完成",font=("SimHei",20)).pack()
labelhuan=ttk1.Label(framexi1,text="",font=("SimHei",30))
labelhuan.place(x=0,y=400)
labelhu=ttk1.Label(framexi1,text="",font=("SimHei",30))
labelhu.place(x=0,y=500)
labelapt=ttk1.Label(framexi1,text="",font=("SimHei",30))
labelapt.place(x=0,y=600)
labelyi=ttk1.Label(framexi1,text="",font=("SimHei",15))
labelyi.place(x=180,y=40)
labelsheng=ttk1.Label(framexi1,text="",font=("SimHei",15))
labelsheng.place(x=500,y=40)
labelyingpan=ttk1.Label(framexi1,text="硬盘使用情况:",font=("SimHei",15),image=icon6,compound=LEFT)
labelyingpan.place(x=0,y=40)
button1=ttk1.Button(frame1,text="查看系统信息",image=icon1,cursor="hand2",compound="top",command=get1,bootstyle=(INFO,OUTLINE))
button1.place(x=0,y=0,width=200,height=200)
button2=ttk1.Button(frame1,text="查看CPU信息",command=get2,image=icon2,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button2.place(x=250,y=0,width=200,height=200)
button3=ttk1.Button(frame1,text="清理缓存",command=get3,image=icon3,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button3.place(x=500,y=0,width=200,height=200)
button4=ttk1.Button(frame1,text="查看显卡信息",command=get4,image=icon4,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button4.place(x=0,y=250,width=200,height=200)
button5=ttk1.Button(frame1,text="查看磁盘空间",command=get5,image=icon5,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button5.place(x=250,y=250,width=200,height=200)
button6=ttk1.Button(frame1,text="更新软件包",command=get6,image=icon6,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button6.place(x=500,y=250,width=200,height=200)
button7=ttk1.Button(frame1,text="安装deb包",command=anzhuang,image=icon8,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button7.place(x=750,y=250,width=200,height=200)
button06=ttk1.Button(frame1,text="执行脚本",command=select_file,image=icon7,cursor="hand2",compound="top",bootstyle=(INFO,OUTLINE))
button06.place(x=750,y=0,width=200,height=200)
buttong1=ttk1.Button(frame6,text="知乎账号",command=web1,bootstyle=(INFO,OUTLINE))
buttong1.place(x=0,y=200,width=1000)
buttong2=ttk1.Button(frame6,text="gitee仓库",command=web2,bootstyle=(INFO,OUTLINE))
buttong2.place(x=0,y=300,width=1000)
buttong3=ttk1.Button(frame6,text="今日头条账号",command=web3,bootstyle=(INFO,OUTLINE))
buttong3.place(x=0,y=400,width=1000)
labels=ttk1.Label(frameshezhi,text="主题",font=("SimHei",15))
labels.place(x=450,y=0)
labelg=ttk1.Label(frame6,text="作者：veyne\n\n关注我，以后有更新版本可以第一时间获取",font=("SimHei",20)).pack()
choice1=tk.IntVar()
choice2=tk.IntVar()
danxuan1=ttk1.Radiobutton(frameshezhi,text="深色",variable=choice1,value=1)
danxuan1.place(x=400,y=30)
danxuan2=ttk1.Radiobutton(frameshezhi,text="简约",variable=choice1,value=2)
danxuan2.place(x=500,y=30)
danxuan3=ttk1.Radiobutton(frameshezhi,text="简洁",variable=choice1,value=3)
danxuan3.place(x=600,y=30)
danxuan3=ttk1.Radiobutton(frameshezhi,text="经典",variable=choice1,value=4)
danxuan3.place(x=300,y=30)
buttonxuanzhe=ttk1.Button(frameshezhi,text="选择主题",command=xuanzhuti,image=iconxuanze,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonxuanzhe.place(x=350,y=100,width=200)
labelzi0=ttk1.Label(frame4,text="命令编号:",font=("SimHei",20))
labelzi0.place(x=500,y=0)
labelzi1=ttk1.Label(frame4,text="命令名称:",font=("SimHei",20))
labelzi1.place(x=500,y=200)
labelzi2=ttk1.Label(frame4,text="命令代码:",font=("SimHei",20))
labelzi2.place(x=500,y=400)
entryzi0=ttk1.Entry(frame4,font=("SimHei",20))
entryzi0.place(x=200,y=100,width=800,height=80)
entryzi1=ttk1.Entry(frame4,font=("SimHei",20))
entryzi1.place(x=200,y=300,width=800,height=80)
entryzi2=ttk1.Entry(frame4,font=("SimHei",20))
entryzi2.place(x=200,y=500,width=800,height=80)
buttonzi1=ttk1.Button(frame4,text="添加命令",command=tianjia,bootstyle=(INFO,OUTLINE),image=iconsave,compound=LEFT)
buttonzi1.place(x=300,y=605,width=200)
buttonzi2=ttk1.Button(frame4,text="修改命令",command=xiugai,bootstyle=(INFO,OUTLINE),image=iconxiugai,compound=LEFT)
buttonzi2.place(x=550,y=605,width=200)
buttonzi2=ttk1.Button(frame4,text="预设1",command=yushe1,bootstyle=(INFO,OUTLINE),image=iconxiugai,compound=LEFT)
buttonzi2.place(x=100,y=700,width=200)
buttonzi2=ttk1.Button(frame4,text="预设2",command=yushe2,bootstyle=(INFO,OUTLINE),image=iconxiugai,compound=LEFT)
buttonzi2.place(x=350,y=700,width=200)
buttonzi2=ttk1.Button(frame4,text="预设3",command=yushe3,bootstyle=(INFO,OUTLINE),image=iconxiugai,compound=LEFT)
buttonzi2.place(x=600,y=700,width=200)
buttonzi2=ttk1.Button(frame4,text="预设4",command=yushe4,bootstyle=(INFO,OUTLINE),image=iconxiugai,compound=LEFT)
buttonzi2.place(x=850,y=700,width=200)   
buttonzi3=ttk1.Button(frame5,text=targetkey1,command=minglin1,bootstyle=(INFO,OUTLINE),image=icon14,compound=LEFT)
buttonzi3.place(x=0,y=100,width=400,height=80)
buttonzi3=ttk1.Button(frame5,text=targetkey2,command=minglin2,bootstyle=(INFO,OUTLINE),image=icon14,compound=LEFT)
buttonzi3.place(x=500,y=100,width=400,height=80)
buttonzi3=ttk1.Button(frame5,text=targetkey3,command=minglin3,bootstyle=(INFO,OUTLINE),image=icon14,compound=LEFT)
buttonzi3.place(x=0,y=200,width=400,height=80)
buttonzi3=ttk1.Button(frame5,text=targetkey4,command=minglin4,bootstyle=(INFO,OUTLINE),image=icon14,compound=LEFT)
buttonzi3.place(x=500,y=200,width=400,height=80)
buttonzi3=ttk1.Button(frame5,text=targetkey5,command=minglin5,bootstyle=(INFO,OUTLINE),image=icon14,compound=LEFT)
buttonzi3.place(x=0,y=300,width=400,height=80)
buttonzi3=ttk1.Button(frame5,text=targetkey6,command=minglin6,bootstyle=(INFO,OUTLINE),image=icon14,compound=LEFT)
buttonzi3.place(x=500,y=300,width=400,height=80)
buttonr1=ttk1.Button(frame1,text="修复依赖",command=yilai,bootstyle=(INFO,OUTLINE),image=iconxiufu,compound=TOP)
buttonr1.place(x=1000,y=0,width=200,height=200)
buttonyong=ttk1.Button(framexi1,text="清理用户缓存",command=yong,bootstyle=(INFO,OUTLINE),image=icon3,compound=LEFT).place(x=0,y=800,width=200)
buttonhu=ttk1.Button(framexi1,text="清理回收站",command=hushou,bootstyle=(INFO,OUTLINE),image=icon3,compound=LEFT).place(x=300,y=800,width=200)
buttonapt=ttk1.Button(framexi1,text="清理apt缓存",command=qingliapt,bootstyle=(INFO,OUTLINE),image=icon3,compound=LEFT).place(x=600,y=800,width=200)
buttonapt=ttk1.Button(framexi1,text="测试硬盘读写速度",command=dx,bootstyle=(INFO,OUTLINE),image=icon3,compound=LEFT).place(x=900,y=800,width=200)
labelcpuxing=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelcpuxing.place(x=400,y=260)
labelxianka=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelxianka.place(x=500,y=20)
labelwangka=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelwangka.place(x=500,y=150)
labelfa=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelfa.place(x=0,y=20)
labelfa1=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelfa1.place(x=0,y=60)
labelfa2=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelfa2.place(x=0,y=100)
labelfa3=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelfa3.place(x=0,y=140)
labelfa4=ttk1.Label(framexi3,text="",font=("SimHei",15))
labelfa4.place(x=0,y=180)
scrolledtext2=ScrolledText(frame_wine,font=("SimHei",15),wrap=tk.WORD,bootstyle="dark")
scrolledtext2.place(x=0,y=200,width=1200,height=1000)
sep1=ttk1.Separator(framexi3,orient=HORIZONTAL)
sep1.place(x=0,y=220,width=1200)
sep2=ttk1.Separator(framexi3,orient=HORIZONTAL)
sep2.place(x=0,y=730,width=1200)
labelfa6=ttk1.Label(framexi3,text=f"CPU线程数:{psutil.cpu_count()}",font=("SimHei",15))
labelfa6.place(x=400,y=300)
labelfa7=ttk1.Label(framexi3,text=f"CPU核心数:{psutil.cpu_count(logical=False)}",font=("SimHei",15))
labelfa7.place(x=400,y=340)

# ==========================================================
# 查看日志模块
# ==========================================================
def rizhi1():
    xuan=choice2.get()
    zhi1=scrolledtext2.get("1.0","end").strip()
    if xuan==5:
        if zhi1=="":
            try:
                cmdri1='journalctl -b --no-pager | tail -50 | grep -i -E "failed|waring|error"'
                resultri1=subprocess.run(cmdri1,capture_output=True,shell=True,text=True)
                scrolledtext2.tag_configure("Veynix",foreground="red")
                if resultri1.stdout !="":
                    scrolledtext2.insert("1.0",resultri1.stdout)
                else:
                    scrolledtext2.insert("1.0","未出现错误信息")
            
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri1='journalctl -b --no-pager | tail -50 | grep -i -E "failed|waring|error"'
                resultri1=subprocess.run(cmdri1,capture_output=True,shell=True,text=True)
                if resultri1.stdout !="":
                    scrolledtext2.insert("1.0",resultri1.stdout)
                else:
                    scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass
    else:
        if zhi1=="":
            try:
                cmdri1="journalctl -b --no-pager | tail -50"
                resultri1=subprocess.run(cmdri1,capture_output=True,shell=True,text=True)
                scrolledtext2.tag_configure("Veynix",foreground="red")
                scrolledtext2.insert("1.0",resultri1.stdout)
            
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri1="journalctl -b --no-pager | tail -50"
                resultri1=subprocess.run(cmdri1,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri1.stdout)
            except:
                pass
def rizhi2():
    xuan=choice2.get()
    zhi2=scrolledtext2.get("1.0","end").strip()
    if xuan==6:
        if zhi2=="":
            try:
                cmdri2='journalctl -b SYSLOG_FACILITY=10 --no-pager | grep -i -E "failed|error|warnning"'
                resultri2=subprocess.run(cmdri2,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri2.stdout)
                if resultri2.stdout !="":
                    scrolledtext2.insert("1.0",resultri2.stdout)
                else:
                    scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri2='journalctl -b SYSLOG_FACILITY=10 --no-pager | grep -i -E "failed|error|warnning"'
                resultri2=subprocess.run(cmdri2,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri2.stdout)
                if resultri2.stdout !="":
                    scrolledtext2.insert("1.0",resultri2.stdout)
                else:
                    scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass   
    else:
        if zhi2=="":
            try:
                cmdri2="journalctl -b SYSLOG_FACILITY=10 --no-pager "
                resultri2=subprocess.run(cmdri2,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri2.stdout)
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri2="journalctl -b SYSLOG_FACILITY=10 --no-pager"
                resultri2=subprocess.run(cmdri2,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri2.stdout)
            except:
                pass   

def rizhi3():
    zhi3=scrolledtext2.get("1.0","end").strip()
    xuan=choice2.get()
    if xuan==7:
        if zhi3=="":
            try:
                cmdri3='pkexec dmesg -T --color=never | grep -i -E "error|warning|failed"'
                resultri3=subprocess.run(cmdri3,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri3.stdout)
                if resultri3.returncode !=0:
                    scrolledtext2.insert("1.0","阅读内核日志需要管理员权限")
                if resultri3.stdout !="":
                    scrolledtext3.insert("1.0",resultri3.stdout)
                else:
                    scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri3='pkexec dmesg -T --color=never | grep -i -E "error|warning|failed"'
                resultri3=subprocess.run(cmdri3,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri3.stdout)
                if resultri3.returncode !=0:
                    scrolledtext2.insert("1.0","阅读内核日志需要管理员权限")
                if resultri3.stdout !="":
                    scrolledtext2.insert("1.0",resultri3.stdout)
                else:
                    scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass
    else:
        if zhi3=="":
            try:
                cmdri3="pkexec dmesg -T --color=never"
                resultri3=subprocess.run(cmdri3,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri3.stdout)
                if resultri3.returncode !=0:
                    scrolledtext2.insert("1.0","阅读内核日志需要管理员权限")
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri3="pkexec dmesg -T --color=never"
                resultri3=subprocess.run(cmdri3,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri3.stdout)
                if resultri3.returncode !=0:
                    scrolledtext2.insert("1.0","阅读内核日志需要管理员权限")
            except:
                pass
def rizhi4():
    zhi4=scrolledtext2.get("1.0","end").strip()
    xuan=choice2.get()
    if xuan==8:
        if zhi4=="":
            try:
                cmdri4='journalctl -b --no-pager |grep -i -E "error|failed|warning"'
                resultri4=subprocess.run(cmdri4,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri4.stdout)
                if resultri4.stdout !="":
                    scrolledtext2.insert("1.0",resultri4.stdout)
                else:
                     scrolledtext2.insert("1.0","未出现错误信息")

            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri4='journalctl -b --no-pager |grep -i -E "error|failed|warning"'
                resultri4=subprocess.run(cmdri4,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri4.stdout)
                if resultri4.stdout !="":
                    scrolledtext2.insert("1.0",resultri4.stdout)
                else:
                     scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass 
    else:
        if zhi4=="":
            try:
                cmdri4="journalctl -b --no-pager"
                resultri4=subprocess.run(cmdri4,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri4.stdout)
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri4="journalctl -b --no-pager"
                resultri4=subprocess.run(cmdri4,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri4.stdout)
            except:
                pass                     
def rizhi5():
    zhi5=scrolledtext2.get("1.0","end").strip()
    xuan=choice2.get()
    if xuan==9:
        if zhi5=="":
            try:
                cmdri5='tail -50 /var/log/dpkg.log |grep -i -E "error|failed|warning"'
                resultri5=subprocess.run(cmdri5,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri4.stdout)
                if resultri5.stdout !="":
                    scrolledtext2.insert("1.0",resultri5.stdout)
                else:
                     scrolledtext2.insert("1.0","未出现错误信息")

            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri5='tail -50 /var/log/dpkg.log |grep -i -E "error|failed|warning"'
                resultri5=subprocess.run(cmdri5,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri5.stdout)
                if resultri5.stdout !="":
                    scrolledtext2.insert("1.0",resultri5.stdout)
                else:
                     scrolledtext2.insert("1.0","未出现错误信息")
            except:
                pass 
    else:
        if zhi5=="":
            try:
                cmdri5="tail -50 /var/log/dpkg.log"
                resultri5=subprocess.run(cmdri5,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri5.stdout)
            except:
                pass
        else:
            scrolledtext2.delete("1.0","end")
            try:
                cmdri5="tail -50 /var/log/dpkg.log"
                resultri5=subprocess.run(cmdri5,capture_output=True,shell=True,text=True)
                scrolledtext2.insert("1.0",resultri5.stdout)
            except:
                pass                     
  
buttonri1=ttk1.Button(frame_wine,text="查看系统日志",command=rizhi1,bootstyle=(INFO,OUTLINE)).place(x=100,y=0)  
buttonri2=ttk1.Button(frame_wine,text="查看认证日志",command=rizhi2,bootstyle=(INFO,OUTLINE)).place(x=300,y=0)     
buttonri3=ttk1.Button(frame_wine,text="查看内核日志",command=rizhi3,bootstyle=(INFO,OUTLINE)).place(x=500,y=0) 
buttonri4=ttk1.Button(frame_wine,text="查看服务日志",command=rizhi4,bootstyle=(INFO,OUTLINE)).place(x=700,y=0) 
buttonri5=ttk1.Button(frame_wine,text="查看软件安装日志",command=rizhi5,bootstyle=(INFO,OUTLINE)).place(x=900,y=0) 
danxuan3=ttk1.Radiobutton(frame_wine,text="过滤错误信息\n(系统日志)",variable=choice2,value=5)
danxuan3.place(x=0,y=100)
danxuan3=ttk1.Radiobutton(frame_wine,text="过滤错误信息\n(认证日志)",variable=choice2,value=6)
danxuan3.place(x=200,y=100)
danxuan3=ttk1.Radiobutton(frame_wine,text="过滤错误信息\n(内核日志)",variable=choice2,value=7)
danxuan3.place(x=400,y=100)
danxuan3=ttk1.Radiobutton(frame_wine,text="过滤错误信息\n(服务日志)",variable=choice2,value=8)
danxuan3.place(x=600,y=100)
danxuan3=ttk1.Radiobutton(frame_wine,text="过滤错误信息\n(软件安装日志)",variable=choice2,value=9)
danxuan3.place(x=800,y=100)
danxuan3=ttk1.Radiobutton(frame_wine,text="正常查看日志",variable=choice2,value=0)
danxuan3.place(x=1000,y=100)

# ================================================
# 服务管理模块
# ================================================
def fuwu1():
    """启动单个服务"""
    resultfu1=entryfu.get()
    cmdfu1=f"systemctl start {resultfu1}"
    resultfu01=subprocess.run(cmdfu1,shell=True,capture_output=True,text=True)
    fuwu6()
    window.update()
def fuwu2():
    """停止单个服务"""
    resultfu2=entryfu.get()
    cmdfu2=f"systemctl stop {resultfu2}"
    resultfu01=subprocess.run(cmdfu2,shell=True,capture_output=True,text=True)
    fywu6()
    window.update()
def fuwu3():
    """设置单个服务开机自启"""
    resultfu3=entryfu.get()
    cmdfu3=f"systemctl enable {resultfu3}"
    resultfu03=subprocess.run(cmdfu3,shell=True,capture_output=True,text=True)
def fuwu4():
    """取消单个服务开机自启"""
    resultfu4=entryfu.get()
    cmdfu4=f"systemctl disable {resultfu4}"
    resultfu04=subprocess.run(cmdfu4,shell=True,capture_output=True,text=True)
def fuwu5():
    """重新启动单个服务"""
    resultfu5=entryfu.get()
    cmdfu5=f"systemctl restart {resultfu5}"
    resultfu05=subprocess.run(cmdfu5,shell=True,capture_output=True,text=True)
def fuwu6():
    """查看单个服务的状态"""
    resultfu6=entryfu.get()
    cmdfu6=f"systemctl status {resultfu6}"
    resultfu06=subprocess.run(cmdfu6,shell=True,capture_output=True,text=True)
    if scrolledtext1.get("1.0","end").strip() =="":
        scrolledtext1.insert("1.0",resultfu06.stdout)
    else:
        scrolledtext1.delete("1.0","end")
        scrolledtext1.insert("1.0",resultfu06.stdout)
def fuwu7():
    """列出所有服务的状态"""
    resultfu7=entryfu.get()
    cmdfu7=f"systemctl list-units --type=service --no-pager"
    resultfu07=subprocess.run(cmdfu7,shell=True,capture_output=True,text=True)
    if scrolledtext1.get("1.0","end").strip() =="":
        scrolledtext1.insert("1.0",resultfu07.stdout)
    else:
        scrolledtext1.delete("1.0","end")
        scrolledtext1.insert("1.0",resultfu07.stdout)

labelfu1=ttk1.Label(framexi4,text="下面搜索框可以写单个服务的名称，进行操作",font=("SimHei",15))
labelfu1.place(x=400,y=0)
entryfu=ttk1.Entry(framexi4)
entryfu.place(x=200,y=50,width=800)
buttonfu1=ttk1.Button(framexi4,text="启用服务",bootstyle=(INFO,OUTLINE),command=fuwu1)
buttonfu1.place(x=250,y=100)
buttonfu2=ttk1.Button(framexi4,text="停止服务",bootstyle=(INFO,OUTLINE),command=fuwu2)
buttonfu2.place(x=350,y=100)
buttonfu3=ttk1.Button(framexi4,text="设为开机自启",bootstyle=(INFO,OUTLINE),command=fuwu3)
buttonfu3.place(x=450,y=100)
buttonfu4=ttk1.Button(framexi4,text="取消开机自启",bootstyle=(INFO,OUTLINE),command=fuwu4)
buttonfu4.place(x=600,y=100)
buttonfu5=ttk1.Button(framexi4,text="重新启动服务",bootstyle=(INFO,OUTLINE),command=fuwu5)
buttonfu5.place(x=750,y=100)
buttonfu6=ttk1.Button(framexi4,text="查看单个服务状态",bootstyle=(INFO,OUTLINE),command=fuwu6)
buttonfu6.place(x=330,y=180,width=200)
buttonfu7=ttk1.Button(framexi4,text="查看全部服务",bootstyle=(INFO,OUTLINE),command=fuwu7)
buttonfu7.place(x=630,y=180,width=200)
scrolledtext1=ScrolledText(framexi4,font=("Monospace",12))
scrolledtext1.place(x=0,y=300,width=1200,height=800)


# ===============================================================
# 系统信息模块
# ===============================================================
def cpuxingxi():
    """获取CPU主频和温度"""

    freq=psutil.cpu_freq()
    temps=psutil.sensors_temperatures()
    if 'acpitz' in temps:
        try:
            cpuwendu=temps['acpitz'][0].current
        except:
            pass

    zhuping=freq.current/1000
    zhupingG=round(float(zhuping),1)
    labelfa8=ttk1.Label(framexi3,text=f"CPU主频:{zhupingG} GHZ",font=("SimHei",15))
    labelfa8.place(x=800,y=260)
    labelfa9=ttk1.Label(framexi3,text=f"CPU温度:{cpuwendu} \u2103",font=("SimHei",15))
    labelfa9.place(x=800,y=300)

    #一秒更新一次主频和温度
    window.after(1000,cpuxingxi)
cpuxingxi() 

def xitong():
    """获取多个系统信息"""
    global result8
    global result9
    global result10
    global result011
    global result012
    cmd8="lscpu | grep \"Model name\" | awk '{print $3 $4 $5}'"
    result8=subprocess.run(cmd8,shell=True,capture_output=True,text=True)
    cmd9="lspci | grep -E 'VGA|3D controller' | awk -F: '{print $3}' | sed 's/^ *//'"
    result9=subprocess.run(cmd9,shell=True,capture_output=True,text=True)
    cmd10="lspci | grep -E 'Ethernet|Network' | awk -F: '{print $3}' | sed 's/^ *//'"
    result10=subprocess.run(cmd10,shell=True,capture_output=True,text=True)

    #获取CPU使用率
    cmd11="top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
    result11=subprocess.run(cmd11,shell=True,capture_output=True,text=True)
    if result11.stdout !="":
        result011=float(result11.stdout)
    else:
        print("错误")

    cmd13="cat /etc/os-release | grep PRETTY_NAME | cut -d'\"' -f2"
    result13=subprocess.run(cmd13,shell=True,capture_output=True,text=True)
    cmd14="uname -r"
    result14=subprocess.run(cmd14,shell=True,capture_output=True,text=True)
    cmd15="uname -m"
    result15=subprocess.run(cmd15,shell=True,capture_output=True,text=True)
    cmd16="uname -n"
    result16=subprocess.run(cmd16,shell=True,capture_output=True,text=True)
    cmd17="uptime -p | awk '{{print $2 $3}}'"
    result17=subprocess.run(cmd17,shell=True,capture_output=True,text=True)
    if result8.stdout !="" :
        labelcpuxing["text"]=f"CPU信息:{result8.stdout}"
    if result9.stdout !="" :
        labelxianka["text"]=f"显卡信息:{result9.stdout}"
    else:
        labelxianka["text"]=f"显卡信息:未知"
    if result10.stdout !="":
        labelwangka["text"]=f"网卡信息:{result10.stdout}"
    else:
        labelwangka["text"]=f"网卡信息:未知"
    if result13.stdout !="":
        labelfa["text"]=f"发行版信息:{result13.stdout}"
    if result14.stdout !="":
        labelfa1["text"]=f"系统内核信息:{result14.stdout}"
    if result15.stdout !="":
        labelfa2["text"]=f"处理器架构:{result15.stdout}"
    if result16.stdout !="":
        labelfa3["text"]=f"主机名:{result16.stdout}"
    if result17.stdout !="":
        labelfa4["text"]=f"系统已运行时间:{result17.stdout}"
    window.after(60000,xitong)
labelfa10=ttk1.Label(framexi3,text="",font=("SimHei",20))
labelfa10.place(x=0,y=500)

def paofen():
    """通过sysbench,完成CPU跑分"""


    global result0d
    labelfa10["text"]="开始测试CPU单核分数,预计需要10-15秒,请耐心等待..."
    framexi3.update_idletasks()
    try:
        cmdc=r"""
    sysbench cpu --cpu-max-prime=20000 --threads=1 run | grep 'events per second' | awk '{print $NF}'
    """
        resultd=subprocess.run(cmdc,capture_output=True,text=True,shell=True)
        result0d=resultd.stdout
        if resultd.returncode ==0:
            labelfa8=ttk1.Label(framexi3,text=f"CPU单核分数:{result0d}",font=("SimHei",18))
            labelfa8.place(x=0,y=570)
            jingdu2=ttk1.Progressbar(framexi3,length=280,mode='determinate',maximum=5000,bootstyle=INFO)
            jingdu2.place(x=300,y=590)
            jingdu2["value"]=result0d
            labelfa10["text"]="正在测试CPU多核分数,预计需要15-25秒,请耐心等待..."
            framexi3.update_idletasks()
            cmdc1=rf"""
        sysbench cpu --cpu-max-prime=20000 --threads=$(nproc) run | grep 'events per second' | awk '{{print $NF}}'
        """
            resultd1=subprocess.run(cmdc1,capture_output=True,text=True,shell=True)
            result0d1=resultd1.stdout
            labelfa9=ttk1.Label(framexi3,text=f"CPU多核核分数:{result0d1}",font=("SimHei",18))
            labelfa9.place(x=0,y=620)
            labelfa10["text"]="CPU跑分完成,以下是测试结果:"
            labelfa0=ttk1.Label(framexi3,text="CPU跑分说明\n单核分数\n低端处理器  300～600分\n中端处理器  600～900分\n高端处理器  1000～1400分\n旗舰处理器  1400分以上",font=("SimHei",18)).place(x=600,y=500)
            jingdu3=ttk1.Progressbar(framexi3,length=280,mode='determinate',maximum=50000,bootstyle=INFO)
            jingdu3.place(x=300,y=640)
            jingdu3["value"]=result0d1

    except Exception as e:
        print(e)
buttonc=ttk1.Button(framexi3,text="开始CPU跑分",command=paofen,bootstyle=(INFO,OUTLINE)).place(x=400,y=400)

xitong()
saomiao()
def neicun():
    """获取内存信息"""

    global result012
    mem=psutil.virtual_memory()
    resultnz=mem.total / 1024 / 1024 / 1024
    result0nz=round(float(resultnz),1)
    resultny=mem.used / 1024 / 1024 / 1024
    result0ny=round(float(resultny),1)
    resultnk=mem.available / 1024 / 1024 / 1024
    result0nk=round(float(resultnk),1)
    labelnz=ttk1.Label(framexi3,text=f"总内存大小:{result0nz}GB",font=("SimeHei",15)).place(x=400,y=750)
    labelny=ttk1.Label(framexi3,text=f"已使用的内存大小:{result0ny}GB",font=("SimeHei",15)).place(x=400,y=800)
    labelnk=ttk1.Label(framexi3,text=f"可使用的内存大小:{result0nk}GB",font=("SimeHei",15)).place(x=400,y=850)
    result12=mem.percent
    if result12 !="":
        result012=round(float(result12),2)
    else:
        print("错误")
    jingdu1=ttk1.Progressbar(framexi3,length=350,mode='determinate',maximum=100,bootstyle=LIGHT)
    jingdu1.place(x=0,y=780,height=30)
    labelns=ttk1.Label(framexi3,text=f"内存使用率:{result012}%",font=("SimeHei",15)).place(x=0,y=810)
    jingdu1["value"]=result012
    if result012 >0 and result012 <60:
        jingdu1.configure(bootstyle=INFO)
    if result012 >60 and result012 <80:
        jingdu1.configure(bootstyle=WARNING)
    if result012 >80:
        jingdu1.configure(bootstyle=DANGER)

    window.after(1000,neicun)


neicun()


meter1=ttk1.Meter(framexi1,padding=10,metersize=160,amountused=result010,amountformat="{:.1f}%",metertype="full",subtext="硬盘使用率",interactive=False,bootstyle="INFO")
meter1.place(x=300,y=80)
meter2=ttk1.Meter(framexi1,padding=10,metersize=160,amountused=result07,amountformat="{:.1f}GB",metertype="full",subtext="硬盘总容量",interactive=False,bootstyle="INFO")
meter2.place(x=0,y=80)
meter3=ttk1.Meter(framexi3,padding=10,metersize=160,amountused=result011,amountformat="{:.1f}%",metertype="full",subtext="CPU使用率",interactive=False,bootstyle="INFO")
meter3.place(x=50,y=280)

def updatexingxi():
    """0.9秒刷新一次CPU使用率,硬盘使用率(保证清理完缓存能立即刷新硬盘使用率)"""
    cmdnew1="top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
    resultnew1=subprocess.run(cmdnew1,shell=True,capture_output=True,text=True)
    if resultnew1.stdout != "":
        resultnew01=float(resultnew1.stdout)
        meter3.configure(amountused=resultnew01)
    cmdn6="df -P /dev/sda2 |awk 'NR==2 {printf\"%.2f\\n\",$3/$2*100}'"
    resultn6=subprocess.run(cmdn6,shell=True,capture_output=True,text=True)
    if resultn6.stdout != "":
        resultn06=float(resultn6.stdout)
        meter1.configure(amountused=resultn06)
    window.after(900,updatexingxi)
      

updatexingxi()

# ===============================================================
# 自定义脚本模块,逻辑和自定义命令模块差不多
# ===============================================================
def tianjiaj():
    global config
    shujuj1=entryj0.get()
    shujuj2=entryj1.get()
    shujuj3=entryj2.get()
    if "1"  in shujuj1 or "2"  in shujuj1 or "3"  in shujuj1 or "4"  in shujuj1 or "5"  in shujuj1 or "6"  in shujuj1  or "7"  in shujuj1 or "8"  in shujuj1 or "9"  in shujuj1 or "10"  in shujuj1:
        if shujuj2 != "":
            if shujuj3 !="":
               if shujuj1 =="1":
                  if targetkey9 in config:
                       del config[targetkey9]
                  items9=list(config.items())
                  items9.insert(9,(shujuj2,shujuj3))
                  config=OrderedDict(items9)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义脚本添加完成，重启后生效","提示")
               elif shujuj1 =="2":
                  if targetkey10 in config:
                       del config[targetkey10]
                  items10=list(config.items())
                  items10.insert(10,(shujuj2,shujuj3))
                  config=OrderedDict(items10)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本添加完成，重启后生效","提示")
               elif shujuj1 =="3":
                  if targetkey11 in config:
                       del config[targetkey11]
                  items11=list(config.items())
                  items11.insert(11,(shujuj2,shujuj3))
                  config=OrderedDict(items11)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shujuj1 =="4":
                  if targetkey12 in config:
                       del config[targetkey12]
                  items12=list(config.items())
                  items12.insert(12,(shujuj2,shujuj3))
                  config=OrderedDict(items12)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shujuj1 =="5":
                  if targetkey13 in config:
                       del config[targetkey13]
                  items13=list(config.items())
                  items13.insert(13,(shujuj2,shujuj3))
                  config=OrderedDict(items13)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shujuj1 =="6":
                  if targetkey14 in config:
                       del config[targetkey14]
                  items14=list(config.items())
                  items14.insert(14,(shujuj2,shujuj3))
                  config=OrderedDict(items14)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令添加完成，重启后生效","提示")
               elif shujuj1 =="7":
                  if targetkey15 in config:
                       del config[targetkey10]
                  items15=list(config.items())
                  items15.insert(15,(shujuj2,shujuj3))
                  config=OrderedDict(items15)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本添加完成，重启后生效","提示")
               elif shujuj1 =="8":
                  if targetkey16 in config:
                       del config[targetkey16]
                  items16=list(config.items())
                  items16.insert(16,(shujuj2,shujuj3))
                  config=OrderedDict(items16)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本添加完成，重启后生效","提示")
               elif shujuj1 =="9":
                  if targetkey17 in config:
                       del config[targetkey17]
                  items17=list(config.items())
                  items17.insert(17,(shujuj2,shujuj3))
                  config=OrderedDict(items17)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本添加完成，重启后生效","提示")
               elif shujuj1 =="10":
                  if targetkey18 in config:
                       del config[targetkey18]
                  items18=list(config.items())
                  items18.insert(18,(shujuj2,shujuj3))
                  config=OrderedDict(items18)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本添加完成，重启后生效","提示")
            else:
                Messagebox.show_info("请输入命令代码","提示")

        else:
            Messagebox.show_info("请输入命令名称","提示")
    else:
         Messagebox.show_info("命令编号只能填1-10中的一个数字","提示") 
def xiugaij():
    global config
    global shujuj2
    global shujuj3
    shujuj1=entryj0.get()
    shujuj2=entryj1.get()
    shujuj3=entryj2.get()
    if "1"  in shujuj1 or "2"  in shujuj1 or "3"  in shujuj1 or "4"  in shujuj1 or "5"  in shujuj1 or "6"  in shujuj1  or "7"  in shujuj1 or "8"  in shujuj1 or "9"  in shujuj1 or "10"  in shujuj1:
        if shujuj2 != "":
            if shujuj3 !="":
               if shujuj1 =="1":
                  if targetkey9 in config:
                       del config[targetkey9]
                  items9=list(config.items())
                  items9.insert(9,(shujuj2,shujuj3))
                  config=OrderedDict(items9)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义脚本修改完成，重启后生效","提示")
               elif shujuj1 =="2":
                  if targetkey10 in config:
                       del config[targetkey10]
                  items10=list(config.items())
                  items10.insert(10,(shujuj2,shujuj3))
                  config=OrderedDict(items10)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本修改完成，重启后生效","提示")
               elif shujuj1 =="3":
                  if targetkey11 in config:
                       del config[targetkey11]
                  items11=list(config.items())
                  items11.insert(11,(shujuj2,shujuj3))
                  config=OrderedDict(items11)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shujuj1 =="4":
                  if targetkey12 in config:
                       del config[targetkey12]
                  items12=list(config.items())
                  items12.insert(12,(shujuj2,shujuj3))
                  config=OrderedDict(items12)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shujuj1 =="5":
                  if targetkey13 in config:
                       del config[targetkey13]
                  items13=list(config.items())
                  items13.insert(13,(shujuj2,shujuj3))
                  config=OrderedDict(items13)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shujuj1 =="6":
                  if targetkey14 in config:
                       del config[targetkey14]
                  items14=list(config.items())
                  items14.insert(14,(shujuj2,shujuj3))
                  config=OrderedDict(items14)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)
                  Messagebox.show_info("自定义命令修改完成，重启后生效","提示")
               elif shujuj1 =="7":
                  if targetkey15 in config:
                       del config[targetkey10]
                  items15=list(config.items())
                  items15.insert(15,(shujuj2,shujuj3))
                  config=OrderedDict(items15)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本修改完成，重启后生效","提示")
               elif shujuj1 =="8":
                  if targetkey16 in config:
                       del config[targetkey16]
                  items16=list(config.items())
                  items16.insert(16,(shujuj2,shujuj3))
                  config=OrderedDict(items16)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本修改完成，重启后生效","提示")
               elif shujuj1 =="9":
                  if targetkey17 in config:
                       del config[targetkey17]
                  items17=list(config.items())
                  items17.insert(17,(shujuj2,shujuj3))
                  config=OrderedDict(items17)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本修改完成，重启后生效","提示")
               elif shujuj1 =="10":
                  if targetkey18 in config:
                       del config[targetkey18]
                  items18=list(config.items())
                  items18.insert(18,(shujuj2,shujuj3))
                  config=OrderedDict(items18)
                  with open(configshezhi,"w",encoding="utf-8") as f1:
                                json.dump(config,f1,ensure_ascii=False,indent=2)  
                  Messagebox.show_info("自定义脚本修改完成，重启后生效","提示")
            else:
                Messagebox.show_info("请输入命令代码","提示")

        else:
            Messagebox.show_info("请输入命令名称","提示")
    else:
         Messagebox.show_info("命令编号只能填1-10中的一个数字","提示") 
def minglin9():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value9} && chmod +x {targetkey9} && ./{targetkey9} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value9} && chmod +x {targetkey9} && ./{targetkey9}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value9} && chmod +x {targetkey9} && ./{targetkey9}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value9} && chmod +x {targetkey9} && ./{targetkey9}; exec bash"])	
                    else:
                       subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value9} && chmod +x {targetkey9} && ./{targetkey9} ; exec bash"])
def minglin10():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value10} && chmod +x {targetkey10} && ./{targetkey10} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value10} && chmod +x {targetkey10} && ./{targetkey10}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value10} && chmod +x {targetkey10} && ./{targetkey10}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value10} && chmod +x {targetkey10} && ./{targetkey10}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value10} && chmod +x {targetkey10} && ./{targetkey10} ; exec bash"])
def minglin11():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value11} && chmod +x {targetkey11} && ./{targetkey11} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value11} && chmod +x {targetkey11} && ./{targetkey11}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value11} && chmod +x {targetkey11} && ./{targetkey11}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value11} && chmod +x {targetkey11} && ./{targetkey11}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value11} && chmod +x {targetkey11} && ./{targetkey11} ; exec bash"])
def minglin12():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value12} && chmod +x {targetkey12} && ./{targetkey12} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value12} && chmod +x {targetkey12} && ./{targetkey12}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value12} && chmod +x {targetkey12} && ./{targetkey12}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value12} && chmod +x {targetkey12} && ./{targetkey12}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value12} && chmod +x {targetkey12} && ./{targetkey12} ; exec bash"])
def minglin13():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value13} && chmod +x {targetkey13} && ./{targetkey13} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value13} && chmod +x {targetkey13} && ./{targetkey13}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value13} && chmod +x {targetkey13} && ./{targetkey13}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value13} && chmod +x {targetkey13} && ./{targetkey13}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value13} && chmod +x {targetkey13} && ./{targetkey13} ; exec bash"])
def minglin14():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value14} && chmod +x {targetkey14} && ./{targetkey14} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value14} && chmod +x {targetkey14} && ./{targetkey14}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value14} && chmod +x {targetkey14} && ./{targetkey14}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value14} && chmod +x {targetkey14} && ./{targetkey14}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value14} && chmod +x {targetkey14} && ./{targetkey14} ; exec bash"])
def minglin15():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value15} && chmod +x {targetkey15} && ./{targetkey15} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value15} && chmod +x {targetkey15} && ./{targetkey15}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value15} && chmod +x {targetkey15} && ./{targetkey15}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value15} && chmod +x {targetkey15} && ./{targetkey15}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value15} && chmod +x {targetkey15} && ./{targetkey15} ; exec bash"])
def minglin16():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value16} && chmod +x {targetkey16} && ./{targetkey16} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value16} && chmod +x {targetkey16} && ./{targetkey16}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value16} && chmod +x {targetkey16} && ./{targetkey16}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value16} && chmod +x {targetkey16} && ./{targetkey16}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value16} && chmod +x {targetkey16} && ./{targetkey16} ; exec bash"])
def minglin17():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value17} && chmod +x {targetkey17} && ./{targetkey17} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value17} && chmod +x {targetkey17} && ./{targetkey17}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value17} && chmod +x {targetkey17} && ./{targetkey17}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value17} && chmod +x {targetkey17} && ./{targetkey17}; exec bash"])	
                    else:
                       subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value17} && chmod +x {targetkey17} && ./{targetkey17} ; exec bash"])
def minglin18():
                    
                    desktop=os.environ.get("XDG_CURRENT_DESKTOP","").lower()
                    if "gnome" in desktop :
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value18} && chmod +x {targetkey18} && ./{targetkey18} ; exec bash"])	
                    elif "kde" in desktop :
                        subprocess.run(["konsole","-e","bash","-c",f"cd {value18} && chmod +x {targetkey18} && ./{targetkey18}; exec bash"])	
                    elif "xfce" in desktop :
                        subprocess.run(["xfce4-terminal","-x","bash","-c",f"cd {value18} && chmod +x {targetkey18} && ./{targetkey18}; exec bash"])	 
                    elif "mate" in desktop :
                        subprocess.run(["mate-terminal","-x","bash","-c",f"cd {value18} && chmod +x {targetkey18} && ./{targetkey18}; exec bash"])	
                    else:
                        subprocess.run(["gnome-terminal","--","bash","-c",f"cd {value18} && chmod +x {targetkey18} && ./{targetkey18} ; exec bash"])
def select_filej():
    file_pathj=filedialog.askopenfilename(title="选择脚本文件",filetypes=[("脚本文件",".sh")])
    if file_pathj:
        filenamej=os.path.basename(file_pathj)
        dir_pathj=os.path.dirname(file_pathj)
        if entryj1.get() != "" or entryj2.get() != "":
            entryj1.delete(0,tk.END)
            entryj2.delete(0,tk.END)
            entryj1.insert(0,filenamej)
            entryj2.insert(0,dir_pathj)
        else:
            entryj1.insert(0,filenamej)
            entryj2.insert(0,dir_pathj)
    


labelj0=ttk1.Label(framej,text="脚本编号:",font=("SimeHei",15))
labelj0.place(x=0,y=10)
labelj1=ttk1.Label(framej,text="脚本名称:",font=("SimeHei",15))
labelj1.place(x=0,y=150)
labelj2=ttk1.Label(framej,text="脚本路径:",font=("SimeHei",15))
labelj2.place(x=0,y=290)
entryj0=ttk1.Entry(framej,bootstyle="secondary",font=("SimHei",15))
entryj0.place(x=150,y=10,width=800,height=60)
entryj1=ttk1.Entry(framej,bootstyle="secondary",font=("SimHei",15))
entryj1.place(x=150,y=150,width=800,height=60)
entryj2=ttk1.Entry(framej,bootstyle="secondary",font=("SimHei",15))
entryj2.place(x=150,y=290,width=800,height=60)
buttonj1=ttk1.Button(framej,text="添加脚本",command=tianjiaj,bootstyle=(INFO,OUTLINE),image=iconsave,compound=LEFT)
buttonj1.place(x=180,y=400)
buttonj2=ttk1.Button(framej,text="修改脚本",command=xiugaij,bootstyle=(INFO,OUTLINE),image=iconxiugai,compound=LEFT)
buttonj2.place(x=300,y=400)
buttonj2=ttk1.Button(framej,text="选择脚本文件",command=select_filej,bootstyle=(INFO,OUTLINE),image=iconfile,compound=LEFT)
buttonj2.place(x=450,y=400)
buttonjj1=ttk1.Button(framej,text=targetkey9,command=minglin9,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj1.place(x=0,y=700,width=400)
buttonjj2=ttk1.Button(framej,text=targetkey10,command=minglin10,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj2.place(x=0,y=750,width=400)
buttonjj3=ttk1.Button(framej,text=targetkey11,command=minglin11,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj3.place(x=0,y=800,width=400)
buttonjj4=ttk1.Button(framej,text=targetkey12,command=minglin12,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj4.place(x=0,y=850,width=400)
buttonjj5=ttk1.Button(framej,text=targetkey13,command=minglin13,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj5.place(x=0,y=900,width=400)
buttonjj6=ttk1.Button(framej,text=targetkey14,command=minglin14,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj6.place(x=500,y=700,width=400)
buttonjj7=ttk1.Button(framej,text=targetkey15,command=minglin15,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj7.place(x=500,y=750,width=400)
buttonjj8=ttk1.Button(framej,text=targetkey16,command=minglin16,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj8.place(x=500,y=800,width=400)
buttonjj9=ttk1.Button(framej,text=targetkey17,command=minglin17,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj9.place(x=500,y=850,width=400)
buttonjj10=ttk1.Button(framej,text=targetkey18,command=minglin18,bootstyle=(INFO,OUTLINE),image=iconj,compound=LEFT)
buttonjj10.place(x=500,y=900,width=400)
right_menu(entryzi2)
right_menu(entryfu)


# ============================================================================
# 文件,目录权限管理模块
# ============================================================================
def select_fileqm():
    global dir_pathqm
    dir_pathqm=filedialog.askdirectory(title="选择目录")
    if dir_pathqm:
        if entryqm.get() != "":
            entryqm.delete(0,tk.END)
            entryqm.insert(0,dir_pathqm)
        else:
            entryqm.insert(0,dir_pathqm)
def select_fileq():
    global dir_pathq
    global filenameq
    global file_pathq
    file_pathq=filedialog.askopenfilename(title="选择文件",filetypes=[("所有文件","*.*")])
    if file_pathq:
        filenameq=os.path.basename(file_pathq)
        dir_pathq=os.path.dirname(file_pathq)
        if entryq.get() != "":
            entryq.delete(0,tk.END)
            entryq.insert(0,filenameq)
        else:
            entryq.insert(0,filenameq)

def quanxian():
    """分析文件权限"""

    cmdq1=f"cd {dir_pathq} && ls -l {filenameq}"
    resultq1=subprocess.run(cmdq1,shell=True,capture_output=True,text=True)
    cmdq2=f"cd {dir_pathq} && ls -l {filenameq} | awk '{{print $1}}'| cut -c1"
    resultq2=subprocess.run(cmdq2,shell=True,capture_output=True,text=True)
    cmdq3=f"cd {dir_pathq} && ls -l {filenameq} | awk '{{print $1}}'| cut -c2-4"
    resultq3=subprocess.run(cmdq3,shell=True,capture_output=True,text=True)
    cmdq4=f"cd {dir_pathq} && ls -l {filenameq} | awk '{{print $1}}'| cut -c5-7"
    resultq4=subprocess.run(cmdq4,shell=True,capture_output=True,text=True)
    cmdq5=f"cd {dir_pathq} && ls -l {filenameq} | awk '{{print $1}}'| cut -c8-10"
    resultq5=subprocess.run(cmdq5,shell=True,capture_output=True,text=True)
    cmdq6=f"cd {dir_pathq} && ls -l {filenameq} | awk '{{print $3}}'"
    resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
    cmdq7=f"cd {dir_pathq} && ls -l {filenameq} | awk '{{print $4}}'"
    resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
    if resultq1.stdout.strip() != "":
        labelq01.config(text=f"文件的权限:{resultq1.stdout}")
    if resultq6.stdout.strip() != "":
        labelq05.config(text=f"文件所有者:{resultq6.stdout}")
    if resultq7.stdout.strip() != "":
        labelq06.config(text=f"文件所属组:{resultq7.stdout}")
    if resultq3.stdout.strip() =="rwx":
        labelq02.config(text="文件所有者的权限:读，写，执行")
    if resultq3.stdout.strip() =="-wx":
        labelq02.config(text="文件所有者的权限:写，执行")
    if resultq3.stdout.strip() =="r-x":
        labelq02.config(text="文件所有者的权限:读，执行")
    if resultq3.stdout.strip() =="rw-":
        labelq02.config(text="文件所有者的权限:读，写")
    if resultq3.stdout.strip() =="--x":
        labelq02.config(text="文件所有者的权限:执行")
    if resultq3.stdout.strip()=="r--":
        labelq02.config(text="文件所有者的权限:读")
 
    if resultq3.stdout.strip() =="-w-":
        labelq02.config(text="文件所有者的权限:写")

    if resultq3.stdout.strip()=="---":
        labelq02.config(text="文件所有者的权限:无")

    if resultq4.stdout.strip() =="rwx":
        labelq03.config(text="文件所属组的权限:读，写，执行")

    if resultq4.stdout.strip() =="-wx":
        labelq03.config(text="文件所属组的权限:写，执行")
    
    if resultq4.stdout.strip() =="r-x":
        labelq03.config(text="文件所属组的权限:读，执行")
       
    if resultq4.stdout.strip() =="rw-":
        labelq03.config(text="文件所属组的权限:读，写")
        
    if resultq4.stdout.strip() =="--x":
        labelq03.config(text="文件所属组的权限:执行")
        
    if resultq4.stdout.strip()=="r--":
        labelq03.config(text="文件所属组的权限:读")
        
    if resultq4.stdout.strip() =="-w-":
        labelq03.config(text="文件所属组的权限:写")
       
    if resultq4.stdout.strip()=="---":
        labelq03.config(text="文件所属组的权限:无")
    
    if resultq5.stdout.strip() =="rwx":
        labelq04.config(text="其他用户的权限:读，写，执行")
  
    if resultq5.stdout.strip() =="-wx":
        labelq04.config(text="其他用户的权限:写，执行")
 
    if resultq5.stdout.strip() =="r-x":
        labelq04.config(text="其他用户的权限:读，执行")

    if resultq5.stdout.strip() =="rw-":
        labelq04.config(text="其他用户的权限:读，写")

    if resultq5.stdout.strip() =="--x":
        labelq04.config(text="其他用户的权限:执行")

    if resultq5.stdout.strip()=="r--":
        labelq04.config(text="其他用户的权限:读")

    if resultq5.stdout.strip() =="-w-":
        labelq04.config(text="其他用户的权限:写")

    if resultq5.stdout.strip()=="---":
        labelq04.config(text="其他用户的权限:无")
def quanxianm():
    """分析目录权限"""

    cmdq1=f"ls -ld {dir_pathqm}"
    resultq1=subprocess.run(cmdq1,shell=True,capture_output=True,text=True)
    cmdq2=f"ls -ld {dir_pathqm} | awk '{{print $1}}'| cut -c1"
    resultq2=subprocess.run(cmdq2,shell=True,capture_output=True,text=True)
    cmdq3=f"ls -ld {dir_pathqm} | awk '{{print $1}}'| cut -c2-4"
    resultq3=subprocess.run(cmdq3,shell=True,capture_output=True,text=True)
    cmdq4=f"ls -ld {dir_pathqm} | awk '{{print $1}}'| cut -c5-7"
    resultq4=subprocess.run(cmdq4,shell=True,capture_output=True,text=True)
    cmdq5=f"ls -ld {dir_pathqm} | awk '{{print $1}}'| cut -c8-10"
    resultq5=subprocess.run(cmdq5,shell=True,capture_output=True,text=True)
    cmdq6=f"ls -ld {dir_pathqm} | awk '{{print $3}}'"
    resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
    cmdq7=f"ls -ld {dir_pathqm} | awk '{{print $4}}'"
    resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
    if resultq1.stdout.strip() != "":
        labelq01.config(text=f"目录的权限:{resultq1.stdout}")
    if resultq6.stdout.strip() != "":
        labelq05.config(text=f"目录所有者:{resultq6.stdout}")
    if resultq7.stdout.strip() != "":
        labelq06.config(text=f"目录所属组:{resultq7.stdout}")
    if resultq3.stdout.strip() =="rwx":
        labelq02.config(text="目录所有者的权限:读，写，执行")
    if resultq3.stdout.strip() =="-wx":
        labelq02.config(text="目录所有者的权限:写，执行")
    if resultq3.stdout.strip() =="r-x":
        labelq02.config(text="目录所有者的权限:读，执行")
    if resultq3.stdout.strip() =="rw-":
        labelq02.config(text="目录所有者的权限:读，写")
    if resultq3.stdout.strip() =="--x":
        labelq02.config(text="目录所有者的权限:执行")
    if resultq3.stdout.strip()=="r--":
        labelq02.config(text="目录所有者的权限:读")
 
    if resultq3.stdout.strip() =="-w-":
        labelq02.config(text="目录所有者的权限:写")

    if resultq3.stdout.strip()=="---":
        labelq02.config(text="目录所有者的权限:无")

    if resultq4.stdout.strip() =="rwx":
        labelq03.config(text="目录所属组的权限:读，写，执行")

    if resultq4.stdout.strip() =="-wx":
        labelq03.config(text="目录所属组的权限:写，执行")
    
    if resultq4.stdout.strip() =="r-x":
        labelq03.config(text="目录所属组的权限:读，执行")
       
    if resultq4.stdout.strip() =="rw-":
        labelq03.config(text="目录所属组的权限:读，写")
        
    if resultq4.stdout.strip() =="--x":
        labelq03.config(text="目录所属组的权限:执行")
        
    if resultq4.stdout.strip()=="r--":
        labelq03.config(text="目录所属组的权限:读")
        
    if resultq4.stdout.strip() =="-w-":
        labelq03.config(text="目录所属组的权限:写")
       
    if resultq4.stdout.strip()=="---":
        labelq03.config(text="目录所属组的权限:无")
    
    if resultq5.stdout.strip() =="rwx":
        labelq04.config(text="其他用户(目录)的权限:读，写，执行")
  
    if resultq5.stdout.strip() =="-wx":
        labelq04.config(text="其他用户(目录)的权限:写，执行")
 
    if resultq5.stdout.strip() =="r-x":
        labelq04.config(text="其他用户(目录)的权限:读，执行")

    if resultq5.stdout.strip() =="rw-":
        labelq04.config(text="其他用户(目录)的权限:读，写")

    if resultq5.stdout.strip() =="--x":
        labelq04.config(text="其他用户(目录)的权限:执行")

    if resultq5.stdout.strip()=="r--":
        labelq04.config(text="其他用户(目录)的权限:读")

    if resultq5.stdout.strip() =="-w-":
        labelq04.config(text="其他用户(目录)的权限:写")

    if resultq5.stdout.strip()=="---":
        labelq04.config(text="其他用户(目录)的权限:无")




def xiugaiquanxian1():
    """添加文件权限"""

    if var1.get() == True :
        cmdq6=f"cd {dir_pathq} && chmod u+r {filenameq}"
        resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
        quanxian()
    if var2.get() == True :
        cmdq7=f"cd {dir_pathq} && chmod u+w {filenameq}"
        resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
        quanxian()
    if var3.get() == True :
        cmdq8=f"cd {dir_pathq} && chmod u+x {filenameq}"
        resultq8=subprocess.run(cmdq8,shell=True,capture_output=True,text=True)
        quanxian()
    if var4.get() ==True :
        cmdq9=f"cd {dir_pathq} && chmod g+r {filenameq}"
        resultq9=subprocess.run(cmdq9,shell=True,capture_output=True,text=True)
        quanxian()
    if var5.get() == True :
        cmdq10=f"cd {dir_pathq} && chmod g+w {filenameq}"
        resultq10=subprocess.run(cmdq10,shell=True,capture_output=True,text=True)
        quanxian()
    if var6.get() == True :
        cmdq11=f"cd {dir_pathq} && chmod g+x {filenameq}"
        resultq11=subprocess.run(cmdq11,shell=True,capture_output=True,text=True)
        quanxian()
    if var7.get() == True :
        cmdq12=f"cd {dir_pathq} && chmod o+r {filenameq}"
        resultq12=subprocess.run(cmdq12,shell=True,capture_output=True,text=True)
        quanxian()
    if var8.get() == True :
        cmdq13=f"cd {dir_pathq} && chmod o+w {filenameq}"
        resultq13=subprocess.run(cmdq13,shell=True,capture_output=True,text=True)
        quanxian()
    if var9.get() == True :
        cmdq14=f"cd {dir_pathq} && chmod o+x {filenameq}"
        resultq14=subprocess.run(cmdq14,shell=True,capture_output=True,text=True)
        quanxian()

def xiugaiquanxian2():
    """减少文件权限"""
    if var1.get() == True :
        cmdq15=f"cd {dir_pathq} && chmod u-r {filenameq}"
        resultq15=subprocess.run(cmdq15,shell=True,capture_output=True,text=True)
        quanxian()
    if var2.get() == True :
        cmdq16=f"cd {dir_pathq} && chmod u-w {filenameq}"
        resultq16=subprocess.run(cmdq16,shell=True,capture_output=True,text=True)
        quanxian()
    if var3.get() == True :
        cmdq17=f"cd {dir_pathq} && chmod u-x {filenameq}"
        resultq17=subprocess.run(cmdq17,shell=True,capture_output=True,text=True)
        quanxian()
    if var4.get() ==True :
        cmdq18=f"cd {dir_pathq} && chmod g-r {filenameq}"
        resultq18=subprocess.run(cmdq18,shell=True,capture_output=True,text=True)
        quanxian()
    if var5.get() == True :
        cmdq19=f"cd {dir_pathq} && chmod g-w {filenameq}"
        resultq19=subprocess.run(cmdq19,shell=True,capture_output=True,text=True)
        quanxian()
    if var6.get() == True :
        cmdq20=f"cd {dir_pathq} && chmod g-x {filenameq}"
        resultq20=subprocess.run(cmdq20,shell=True,capture_output=True,text=True)
        quanxian()
    if var7.get() == True :
        cmdq21=f"cd {dir_pathq} && chmod o-r {filenameq}"
        resultq21=subprocess.run(cmdq21,shell=True,capture_output=True,text=True)
        quanxian()
    if var8.get() == True :
        cmdq22=f"cd {dir_pathq} && chmod o-w {filenameq}"
        resultq22=subprocess.run(cmdq22,shell=True,capture_output=True,text=True)
        quanxian()
    if var9.get() == True :
        cmdq23=f"cd {dir_pathq} && chmod o-x {filenameq}"
        resultq23=subprocess.run(cmdq23,shell=True,capture_output=True,text=True)
        quanxian()
def xiugaiquanxian3():
    """递归添加目录权限"""
    if var10.get() == True:
        if var1.get() == True :
            cmdq6=f"chmod -R u+r {dir_pathqm}"
            resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
            quanxian()
        if var2.get() == True :
            cmdq7=f"chmod -R u+w {dir_pathqm}"
            resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
            quanxian()
        if var3.get() == True :
            cmdq8=f"chmod -R u+x {dir_pathqm}"
            resultq8=subprocess.run(cmdq8,shell=True,capture_output=True,text=True)
            quanxian()
        if var4.get() ==True :
            cmdq9=f"chmod -R g+r {dir_pathqm}"
            resultq9=subprocess.run(cmdq9,shell=True,capture_output=True,text=True)
            quanxian()
        if var5.get() == True :
            cmdq10=f"chmod -R g+w {dir_pathqm}"
            resultq10=subprocess.run(cmdq10,shell=True,capture_output=True,text=True)
            quanxian()
        if var6.get() == True :
            cmdq11=f"chmod -R g+x {dir_pathqm}"
            resultq11=subprocess.run(cmdq11,shell=True,capture_output=True,text=True)
            quanxian()
        if var7.get() == True :
            cmdq12=f"chmod -R o+r {dir_pathqm}"
            resultq12=subprocess.run(cmdq12,shell=True,capture_output=True,text=True)
            quanxian()
        if var8.get() == True :
            cmdq13=f"chmod -R o+w {dir_pathqm}"
            resultq13=subprocess.run(cmdq13,shell=True,capture_output=True,text=True)
            quanxian()
        if var9.get() == True :
            cmdq14=f"chmod -R o+x {dir_pathqm}"
            resultq14=subprocess.run(cmdq14,shell=True,capture_output=True,text=True)
            quanxian()
    """增加目录权限"""
    if var10.get() == False:
        if var1.get() == True :
            cmdq6=f"chmod u+r {dir_pathqm}"
            resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
            quanxian()
        if var2.get() == True :
            cmdq7=f"chmod u+w {dir_pathqm}"
            resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
            quanxian()
        if var3.get() == True :
            cmdq8=f"chmod u+x {dir_pathqm}"
            resultq8=subprocess.run(cmdq8,shell=True,capture_output=True,text=True)
            quanxian()
        if var4.get() ==True :
            cmdq9=f"chmod g+r {dir_pathqm}"
            resultq9=subprocess.run(cmdq9,shell=True,capture_output=True,text=True)
            quanxian()
        if var5.get() == True :
            cmdq10=f"chmod g+w {dir_pathqm}"
            resultq10=subprocess.run(cmdq10,shell=True,capture_output=True,text=True)
            quanxian()
        if var6.get() == True :
            cmdq11=f"chmod g+x {dir_pathqm}"
            resultq11=subprocess.run(cmdq11,shell=True,capture_output=True,text=True)
            quanxian()
        if var7.get() == True :
            cmdq12=f"chmod o+r {dir_pathqm}"
            resultq12=subprocess.run(cmdq12,shell=True,capture_output=True,text=True)
            quanxian()
        if var8.get() == True :
            cmdq13=f"chmod o+w {dir_pathqm}"
            resultq13=subprocess.run(cmdq13,shell=True,capture_output=True,text=True)
            quanxian()
        if var9.get() == True :
            cmdq14=f"chmod o+x {dir_pathqm}"
            resultq14=subprocess.run(cmdq14,shell=True,capture_output=True,text=True)
            quanxian()
def xiugaiquanxian4():
    """递归减少目录权限"""
    if var10.get() == True:
        if var1.get() == True :
            cmdq6=f"chmod -R u-r {dir_pathqm}"
            resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
            quanxian()
        if var2.get() == True :
            cmdq7=f"chmod -R u-w {dir_pathqm}"
            resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
            quanxian()
        if var3.get() == True :
            cmdq8=f"chmod -R u-x {dir_pathqm}"
            resultq8=subprocess.run(cmdq8,shell=True,capture_output=True,text=True)
            quanxian()
        if var4.get() ==True :
            cmdq9=f"chmod -R g-r {dir_pathqm}"
            resultq9=subprocess.run(cmdq9,shell=True,capture_output=True,text=True)
            quanxian()
        if var5.get() == True :
            cmdq10=f"chmod -R g-w {dir_pathqm}"
            resultq10=subprocess.run(cmdq10,shell=True,capture_output=True,text=True)
            quanxian()
        if var6.get() == True :
            cmdq11=f"chmod -R g-x {dir_pathqm}"
            resultq11=subprocess.run(cmdq11,shell=True,capture_output=True,text=True)
            quanxian()
        if var7.get() == True :
            cmdq12=f"chmod -R o-r {dir_pathqm}"
            resultq12=subprocess.run(cmdq12,shell=True,capture_output=True,text=True)
            quanxian()
        if var8.get() == True :
            cmdq13=f"chmod -R o-w {dir_pathqm}"
            resultq13=subprocess.run(cmdq13,shell=True,capture_output=True,text=True)
            quanxian()
        if var9.get() == True :
            cmdq14=f"chmod -R o-x {dir_pathqm}"
            resultq14=subprocess.run(cmdq14,shell=True,capture_output=True,text=True)
            quanxian()
    """减少目录权限"""
    if var10.get() == False:
        if var1.get() == True :
            cmdq6=f"chmod u-r {dir_pathqm}"
            resultq6=subprocess.run(cmdq6,shell=True,capture_output=True,text=True)
            quanxian()
        if var2.get() == True :
            cmdq7=f"chmod u-w {dir_pathqm}"
            resultq7=subprocess.run(cmdq7,shell=True,capture_output=True,text=True)
            quanxian()
        if var3.get() == True :
            cmdq8=f"chmod u-x {dir_pathqm}"
            resultq8=subprocess.run(cmdq8,shell=True,capture_output=True,text=True)
            quanxian()
        if var4.get() ==True :
            cmdq9=f"chmod g-r {dir_pathqm}"
            resultq9=subprocess.run(cmdq9,shell=True,capture_output=True,text=True)
            quanxian()
        if var5.get() == True :
            cmdq10=f"chmod g-w {dir_pathqm}"
            resultq10=subprocess.run(cmdq10,shell=True,capture_output=True,text=True)
            quanxian()
        if var6.get() == True :
            cmdq11=f"chmod g-x {dir_pathqm}"
            resultq11=subprocess.run(cmdq11,shell=True,capture_output=True,text=True)
            quanxian()
        if var7.get() == True :
            cmdq12=f"chmod o-r {dir_pathqm}"
            resultq12=subprocess.run(cmdq12,shell=True,capture_output=True,text=True)
            quanxian()
        if var8.get() == True :
            cmdq13=f"chmod o-w {dir_pathqm}"
            resultq13=subprocess.run(cmdq13,shell=True,capture_output=True,text=True)
            quanxian()
        if var9.get() == True :
            cmdq14=f"chmod o-x {dir_pathqm}"
            resultq14=subprocess.run(cmdq14,shell=True,capture_output=True,text=True)
            quanxian() 
def wen1():
    content1=simpledialog.askstring(title="输入框",prompt="请输入你要改的文件所有者名称")
    if content1 is None :
        return 
    if content1 != "":
        cmdwen1=f"pkexec chown {content1} {file_pathq} "
        resultwen1=subprocess.run(cmdwen1,shell=True,capture_output=True,text=True)
        print(resultwen1.stderr)
        quanxian()
def wen2():
    content2=simpledialog.askstring(title="输入框",prompt="请输入你要改的文件所属组名称")
    if content2 is None :
        return 
    if content2 != "":
        cmdwen2=f"pkexec chown :{content2} {file_pathq}"
        resultwen2=subprocess.run(cmdwen2,shell=True,capture_output=True,text=True)
        print(resultwen2.stderr)
        quanxian()
def wen3():
    content3=simpledialog.askstring(title="输入框",prompt="请输入你要改的文件所有者名称")
    if content3 is None :
        return 
    if var10.get()==True:
        if content3 != "":
            cmdwen3=f"pkexec chown -R {content3} {dir_pathqm}"
            resultwen3=subprocess.run(cmdwen3,shell=True,capture_output=True,text=True)
            print(resultwen3.stderr)
            quanxian()
    if var10.get()==False:
        if content3 != "":
            cmdwen3=f"pkexec chown {content3} {dir_pathqm}"
            resultwen3=subprocess.run(cmdwen3,shell=True,capture_output=True,text=True)
            print(resultwen3.stderr)
            quanxian()  
def wen4():
    content4=simpledialog.askstring(title="输入框",prompt="请输入你要改的文件所属组名称")
    if content4 is None :
        return 
    if var10.get()==True:
        if content4 != "":
            cmdwen4=f"pkexec chown -R :{content4} {dir_pathqm}"
            resultwen4=subprocess.run(cmdwen4,shell=True,capture_output=True,text=True)
            print(resultwen4.stderr)
            quanxian()
    if var10.get()==False:
        if content4 != "":
            cmdwen4=f"pkexec chown :{content4} {dir_pathqm}"
            resultwen4=subprocess.run(cmdwen4,shell=True,capture_output=True,text=True)
            print(resultwen4.stderr)
            quanxian()          
style=ttk1.Style()
style.configure("cziti.TCheckbutton",font=("SimHei",25))
entryq=ttk1.Entry(frameq,font=("SimHei",15))
entryq.place(x=200,y=0,width=600,height=40)
entryqm=ttk1.Entry(frameq,font=("SimHei",15))
entryqm.place(x=200,y=50,width=600,height=40)
buttonq1=ttk1.Button(frameq,text="选择文件",command=select_fileq,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=0,y=160,width=200)
buttonq1=ttk1.Button(frameq,text="更改文件所有者",command=wen1,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=800,y=160)
buttonq1=ttk1.Button(frameq,text="更改文件所属组",command=wen2,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=800,y=220)
buttonq1=ttk1.Button(frameq,text="更改目录所有者",command=wen3,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=1000,y=160)
buttonq1=ttk1.Button(frameq,text="更改目录所属组",command=wen4,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=1000,y=220)
buttonq1=ttk1.Button(frameq,text="分析文件权限",command=quanxian,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=250,y=160)
buttonq1=ttk1.Button(frameq,text="分析目录权限",command=quanxianm,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=250,y=220)
buttonq1=ttk1.Button(frameq,text="修改文件权限(添加)",command=xiugaiquanxian1,image=iconxiugai,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=400,y=160)
buttonq1=ttk1.Button(frameq,text="修改文件权限(减去)",command=xiugaiquanxian2,image=iconxiugai,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=600,y=160)
buttonq1=ttk1.Button(frameq,text="修改目录权限(添加)",command=xiugaiquanxian3,image=iconxiugai,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=400,y=220)
buttonq1=ttk1.Button(frameq,text="修改目录权限(减去)",command=xiugaiquanxian4,image=iconxiugai,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=600,y=220)
buttonq1=ttk1.Button(frameq,text="选择目录",command=select_fileqm,image=iconfile,compound=LEFT,bootstyle=(INFO,OUTLINE))
buttonq1.place(x=0,y=220,width=200)
var1=ttk1.BooleanVar(value=False)
var2=ttk1.BooleanVar(value=False)
var3=ttk1.BooleanVar(value=False)
var4=ttk1.BooleanVar(value=False)
var5=ttk1.BooleanVar(value=False)
var6=ttk1.BooleanVar(value=False)
var7=ttk1.BooleanVar(value=False)
var8=ttk1.BooleanVar(value=False)
var9=ttk1.BooleanVar(value=False)
var10=ttk1.BooleanVar(value=False)
var11=ttk1.BooleanVar(value=False)
fuxuan1=ttk1.Checkbutton(frameq,text="读",variable=var1,style="cziti.TCheckbutton")
fuxuan1.place(x=0,y=350)
fuxuan2=ttk1.Checkbutton(frameq,text="写",variable=var2,style="cziti.TCheckbutton")
fuxuan2.place(x=0,y=450)
fuxuan3=ttk1.Checkbutton(frameq,text="执行",variable=var3,style="cziti.TCheckbutton")
fuxuan3.place(x=0,y=550)
fuxuan4=ttk1.Checkbutton(frameq,text="读",variable=var4,style="cziti.TCheckbutton")
fuxuan4.place(x=350,y=350)
fuxuan5=ttk1.Checkbutton(frameq,text="写",variable=var5,style="cziti.TCheckbutton")
fuxuan5.place(x=350,y=450)
fuxuan6=ttk1.Checkbutton(frameq,text="执行",variable=var6,style="cziti.TCheckbutton")
fuxuan6.place(x=350,y=550)
fuxuan7=ttk1.Checkbutton(frameq,text="读",variable=var7,style="cziti.TCheckbutton")
fuxuan7.place(x=700,y=350)
fuxuan8=ttk1.Checkbutton(frameq,text="写",variable=var8,style="cziti.TCheckbutton")
fuxuan8.place(x=700,y=450)
fuxuan9=ttk1.Checkbutton(frameq,text="执行",variable=var9,style="cziti.TCheckbutton")
fuxuan9.place(x=700,y=550)
fuxuan10=ttk1.Checkbutton(frameq,text="开启递归修改目录权限,所有者，所属组",variable=var10,style="cziti.TCheckbutton")
fuxuan10.place(x=200,y=100)
labelq1=ttk1.Label(frameq,text="修改\n文件/目录所有者的权限:",font=("SimHei",15))
labelq1.place(x=0,y=280)
labelq2=ttk1.Label(frameq,text="修改\n文件/目录所属组的权限:",font=("SimHei",15))
labelq2.place(x=350,y=280)
labelq3=ttk1.Label(frameq,text="修改其他用户的权限:",font=("SimHei",15))
labelq3.place(x=700,y=300)
labelq01=ttk1.Label(frameq,text=f"",font=("SimHei",18))
labelq01.place(x=0,y=700)
labelq02=ttk1.Label(frameq,text="",font=("SimHei",18))
labelq02.place(x=0,y=800)
labelq03=ttk1.Label(frameq,text="",font=("SimHei",18))
labelq03.place(x=0,y=900)
labelq04=ttk1.Label(frameq,text="",font=("SimHei",18))
labelq04.place(x=0,y=1000)
labelq05=ttk1.Label(frameq,text="",font=("SimHei",18))
labelq05.place(x=450,y=800)
labelq06=ttk1.Label(frameq,text="",font=("SimHei",18))
labelq06.place(x=450,y=900)
labelw=ttk1.Label(frameq,text="这里为你选择的文件:",font=("SimHei",15)).place(x=0,y=0)
labelw1=ttk1.Label(frameq,text="这里为你选择的目录:",font=("SimHei",15)).place(x=0,y=50)

window.mainloop()

