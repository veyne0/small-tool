

# Small Tool

这是一个基于 Gitee 的开源项目仓库。

## 项目简介

本项目提供了一个预编译的 Debian 软件包 (`small-tool_0.1.0_all.deb`)，适用于 Debian/Ubuntu 等 Linux 发行版。

## 软件包说明

- **软件包名称**: small-tool
- **版本**: 0.1.0
- **架构**: all (适用于所有架构)
- **格式**: .deb (Debian 软件包)

## 安装方法

### 方法一：使用 dpkg 命令
```bash
sudo dpkg -i small-tool_0.1.0_all.deb
```

### 方法二：使用 gdebi 工具（自动解决依赖）
```bash
sudo gdebi small-tool_0.1.0_all.deb
```

### 方法三：使用 apt 命令
```bash
sudo apt install ./small-tool_0.1.0_all.deb
```

## 系统要求

- Debian 系统 (9.x/10.x/11.x 等)
- Ubuntu 系统 (16.04/18.04/20.04/22.04 等)
- 其他基于 Debian 的 Linux 发行版

## 许可证

本项目采用 MIT 许可证。

## 参与贡献

如果您对本项目有任何建议或发现 bug，欢迎通过 Gitee 平台提交 Issue 或 Pull Request。

## 联系方式

- 项目地址: https://gitee.com/veyne0/small-tool

---

**注意**: 由于本仓库目前仅包含编译后的软件包文件，如需查看源代码或了解工具的具体功能，请联系项目维护者或查阅相关文档。