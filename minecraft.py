import minecraft_launcher_lib as mcl
import os
import subprocess
import psutil
mcdir=os.path.expanduser("~/minecraft")
os.makedirs(mcdir,exist_ok=True)

# =========================================================
# 
#提供各个版本供选择，选择哪个版本就在def xiazai()中的xiazaiversion()里填哪个版本。添加一个可选forge选项,fabric(只有高版本有)。
['1.21.11', '1.21.10', '1.21.9', '1.21.8', '1.21.7', '1.21.6', '1.21.5', '1.21.4', '1.21.3', '1.21.2', '1.21.1', '1.21', '1.20.6', '1.20.5', '1.20.4', '1.20.3', '1.20.2', '1.20.1', '1.20', '1.19.4', '1.19.3', '1.19.2', '1.19.1', '1.19', '1.18.2', '1.18.1', '1.18', '1.17.1', '1.17', '1.16.5', '1.16.4', '1.16.3', '1.16.2', '1.16.1', '1.16', '1.15.2', '1.15.1', '1.15', '1.14.4', '1.14.3', '1.14.2', '1.14.1', '1.14', '1.13.2', '1.13.1', '1.13', '1.12.2', '1.12.1', '1.12', '1.11.2', '1.11.1', '1.11', '1.10.2', '1.10.1', '1.10', '1.9.4', '1.9.3', '1.9.2', '1.9.1', '1.9', '1.8.9', '1.8.8', '1.8.7', '1.8.6', '1.8.5', '1.8.4', '1.8.3', '1.8.2', '1.8.1', '1.8', '1.7.10', '1.7.9', '1.7.8', '1.7.7', '1.7.6', '1.7.5', '1.7.4', '1.7.3', '1.7.2', '1.6.4', '1.6.2', '1.6.1', '1.5.2', '1.5.1', '1.4.7', '1.4.5', '1.4.6', '1.4.4', '1.4.2', '1.3.2', '1.3.1', '1.2.5', '1.2.4', '1.2.3', '1.2.2', '1.2.1', '1.1', '1.0']

def xiazaiversion(version,callback=None):
    mcl.install.install_minecraft_version(version,mcdir,callback=callback)
    #选择了forge就下载forge,选择了fabric就下fabric
    if 1==1:
    	try:
    		fversion=mcl.forge.find_forge_version(version)
    		mcl.forge.install_forge_version(fversion,mcdir)
    	except Exception as e:
    		print(e)
    #elif 选择了fabric:
        #mcl.fabric.install_fabric(version,mcdir)
    	

def xiazai():
    xiazaiversion("1.12.2")
#xiazai()

mem=psutil.virtual_memory()
#获取总内存
resultnz=mem.total / 1024 / 1024 / 1024
result0nz=round(float(resultnz),1)
#获取已用内存
resultny=mem.used / 1024 / 1024 / 1024
result0ny=round(float(resultny),1)
#获取可用内存
resultnk=mem.available / 1024 / 1024 / 1024
result0nk=round(float(resultnk),1)

def launchCPU():
    global cmdc
    java_path="/usr/bin/java"
    if not java_path:
        messagebox.showinfo("提示","没发现java")
    option1={
        "username":"123",
        "uuid":"123",
        "token":"0",
        "javaPath":java_path,
        "maxMemory":"4G",
        "minMemory":"1G",
        "gameDirectory":"/home/veynix/minecraft/versions/1.12.2",
        "jvmArguments":["-Dorg.lwjgl.opengl.Display.allowSoftwareOpenGL=true"]
    }
    cmdc=mcl.command.get_minecraft_command(version="1.12.2",minecraft_directory=mcdir,options=option1)
    return cmdc
cmd1=launchCPU()
def launchH():
    global cmdh
    java_path="/usr/bin/java"
    if not java_path:
        messagebox.showinfo("提示","没发现java")
    option2={
        "username":"123",
        "uuid":"123",
        "token":"0",
        "javaPath":java_path,
        "maxMemory":"4G",
        "minMemory":"1G",
        "gameDirectory":"/home/veynix/minecraft/versions/1.12.2"
    }
    cmdh=mcl.command.get_minecraft_command(version="1.12.2",minecraft_directory=mcdir,options=option2)
    return cmdh
cmd2=launchH()
def launchD():
    global cmdD
    java_path="/usr/bin/java"
    if not java_path:
        messagebox.showinfo("提示","没发现java")
    option3={
        "username":"123",
        "uuid":"123",
        "token":"0",
        "javaPath":java_path,
        "maxMemory":"4G",
        "minMemory":"1G",
        "gameDirectory":"/home/veynix/minecraft/versions/1.12.2"
    }
    cmdD=mcl.command.get_minecraft_command(version="1.12.2",minecraft_directory=mcdir,options=option3)
    return cmdD
cmd3=["switcherooctl", "launch"]+launchD()
def launchmc():
    try:
        result=subprocess.Popen(cmd3,cwd="/home/veynix/minecraft/versions/1.12.2",stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print(e)
launchmc()

# 以上为最基本的启动代码
	