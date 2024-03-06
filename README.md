# **Vault Patcher Grocery Store丨Vault Patcher杂货铺**

维护：KlparetlR、TexTrue、X209

## 相关链接

[![Vault Patcher](https://img.shields.io/badge/github-Vault%20Patcher-blue)](https://github.com/3093FengMing/VaultPatcher)
[![modrinth-VP](https://img.shields.io/badge/modrinth-Vault%20Patcher-green)](https://modrinth.com/mod/vault-patcher/versions)
[![mcmod-VP](https://img.shields.io/badge/mcmod-Vault%20Patcher-blue)](https://www.mcmod.cn/class/8765.html)
[![vpshuju](https://img.shields.io/badge/modrinth-%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%BB%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80-purple)](https://modrinth.com/resourcepack/vmct)

## 介绍

这是一个存放Vault Patcher模组的配置+汉化以及编写工具的开源库

服务于熟悉Vault Patcher模组的**大佬**，在这里，你可以调用模组的配置文件，修提交修改配置或汉化的建议

你可以用它们去汉化整合包的硬编码，提升汉化细节程度

## 配置及翻译上传的要求及格式

请在`ModConfigs`文件夹中提交你的PR，格式为`ModConfigs/patch/<模组命名空间>/<提取硬编码的对应游戏版本>`

<模组命名空间>会在之后用于硬编码汉化下载模组，需准确填写，一般是assets文件夹下存放模组主要文件（包括语言文件）的文件夹名

比如：`XPCoins(FORGE-1.16.4)vrs1.0.7.jar\assets\xpcoins\lang\en_us.json`

这里的`xpcoins`即为模组命名空间

`<提取硬编码的对应游戏版本>`尽量写区间（尽量测试保证区间内的版本启用它时不报错）,比如：`1.20.1-1.14.2`，高版本在前。也可以写`1.14.2+`

PR格式为`<模组英文名> <简述>`，例如`FTBQuests 汉化提交`

json配置文件要求第一个对象要有"authors"，"name"，"desc"，"mods"，并且**限定内容**
```txt
    {
        "authors": "<作者名>",
        "name": "<模组名>模组汉化",
        "desc": "VP<版本号>+可启用，...",
        "mods": "<模组信息，要细致到模组名、游戏版本、模组版本>",
        "dynamic": false
    },
以下为示范：
    {
        "authors": "KlparetlR、Qing_Lanovo",
        "name": "XPCoins模组汉化",
        "desc": "VP1.3.3+可启用，VPGS开源",
        "mods": "XPCoins (FORGE-1.16.4) v1.0.7",
        "dynamic": false
    },
```

可以参考CFPA的[i18n库](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package/blob/main/CONTRIBUTING.md)

## 调用后的要求和限制 **（必看，须知）**

本库的协议为[CC-BY-NC-ND 4.0](https://github.com/KlparetlR/Vault-Patcher-Grocery-Store/blob/main/LICENSE.txt)，即

BY（Attribution，署名归属）：您可自由地分享和改编本作品，但您**必须注明**创作者的版权归属。

NC（Non Commercial，非商业性）：您可自由地分享和改编本作品，但您不得用于**商业目的**。

ND（No Derivatives，禁止改编）：你可自由地分享本作品，但您不得合成、转换和改造本作品。

如果您要**用于整合包汉化发布**等分享本作品的行为，你要在汉化文件或汉化发布页内**注明**创作者的版权归属

以下是示例格式（可直接复制，也可以以其他格式注明）：
```txt
本<可改内容>中的硬编码汉化部分使用了VPGS库（KlparetlR/Vault-Patcher-Grocery-Store）提供的内容
```

## 其他的一些话

因为硬编码汉化这方面涉足的人很少，可能这个库的配置很少，但作者还是会积极努力的维护它，一般以作者主动上传和别人授权的内容上传，欢迎**大佬**提交配置和汉化（PR），Thanks♪(･ω･)ﾉ
