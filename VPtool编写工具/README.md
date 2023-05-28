# **Vault Patcher Tool**

作者及版权方：晴笙墨染（墨安）、KlparetlR、捂脸Wulian

## 专门为[Vault Patcher模组](https://github.com/3093FengMing/VaultPatcher)而生的配置编写工具

由 KlparetlR 提出的方案， 晴笙墨染（墨安） 实现的基础代码和bug修复，外包修饰由 KlparetlR 自学py编写

GUI场外援助:Wulian、捂脸、VM汉化组Wulian、VM汉化组捂脸、网站捂脸、网站Wulian

弹窗使用https://github.com/rdbende/Sun-Valley-messageboxes

ttk UI用了sv-ttk模块，没有会自己下载

## 支持VP模组的移植[Fabric版](https://github.com/LocalizedMC/HardcodePatcher),（在选择模组加载器格式窗口单击Fabric）

提出支持Fabric的是TexTrue，编写这部分的是KlparetlR,他自己也写了[移植版](https://gist.github.com/TexBlock/e54a48ad59e9d8b8e9c411015943efa9)

## 支持的语言 Supported languages

目前仅支持中文，如果想要其他语言，可以评论表达你要的语种（顺便把内容翻译给我）

Currently, only Chinese is supported. If you want other languages, you can comment on the language you want (please translate the content to me by the way)

(Only includes the contents of the window display in this py file and Tutorial content, this tool actually supports any language as long as it is UTF-8 encoded)

---

# 使用教程

## 配置文件

该工具仅支持`.txt`后缀文件和utf-8编码的原始文件

### 配置

以下是一个key的配置内容（接下来都以这个为模板）：

```json  
{
  "target_class": {
    "name": "nametype",
    "mapping": "loadertype",
    "stack_depth": -1
  },
  "key": "I'm key",
  "value": "I'm value"
}
```

#### 第一行（包名匹配模块）

第一行的内容（以`@`开头的内容）将替换`target_class`中的`name`的值，即`nametype` = 第一行的内容。作为全局的文本来使用。触发功能前缀：`@bm;`

#### 第二行（将按数字顺序输出`value`的基础内容）

这部分你可以像lang文件那样取名，比如：`namespace.modify.the_vault.`，这会作为第三行实数排序的前缀。

#### 第三行（按 数字顺序 输出`value`的后缀）

将第二行的内容作为前缀，只允许填入初始实数，从这个数字开始会按顺序往后排，然后做为后缀填入`value`，即`value` = 第二行内容+第三行内容。

举例一个基础配置：

输出的配置：
```json 
{
  "key": "Abilities",
  "value": "namespace.modify.the_vault.1"
},
{
  "key": "Archetypes",
  "value": "namespace.modify.the_vault.2"
},
{
  "key": "Researches",
  "value": "namespace.modify.the_vault.3"
}
```
输出的lang：
```json  
{
  "namespace.modify.the_vault.1": "Abilities",
  "namespace.modify.the_vault.2": "Archetypes",
  "namespace.modify.the_vault.3": "Researches",
}
```

#### 第四行以下

格式为：`功能前缀`+`key`。当然你也可以只输入`key`，这样就会输出没有开启任何功能的配置文本（`target_class`的那一类内容也不会出现,且全匹配模式）

[第三行](https://gist.github.com/KlparetlR/b7aa7c3004852575683ce9b3338db604#第三行按-数字顺序-输出value的后缀)举例的`.txt`文件配置：
```txt
@iskallia.vault
namespace.modify.the_vault.
1
Abilities
Archetypes
Researches
```

### 启用功能的前缀

就是用一个固定的内容替换`功能前缀`，工具处理时会将其转化，现在支持的功能有 半匹配、包名匹配、类匹配

#### 半匹配(`@;`)

在`功能前缀`部分填入`@;`即可。兼容 包名匹配 和 类匹配。

#### 包名匹配(`@bm;`)

在`功能前缀`部分填入`@bm;`即可。不兼容`类匹配`，如果你两个功能都开了，工具也不会报错，它设定`类匹配`的优先级最高，处理时,`包名匹配`不会体现。

包名如何获取：打开你要汉化硬编码的模组.jar文件，找到其中放有大量`.class`文件的文件夹（最好能看见与模组名相关的`.class`文件，比如模组名：XPCoins，找到XPCoins.class文件所在的目录），将这个文件夹的地址复制，大致是XXX.jar\ `com\coldspell\xpcoins`，不同模组存`.class`文件的文件夹名可能不同（没有com文件夹），要自己辨别，接着把`\`全部改成`.`并把`XXX.jar\`删掉，最后在原始文件中的第一行输入`@文件夹地址`,比如`@com.coldspell.xpcoins`或者`@iskallia.vault`

#### 类匹配(`#内容根地址`+`#END`)

类匹配的开启比较特殊，它相当于开关，输入`#内容根地址`后，下一行开始都会属于这个类匹配的影响范围，要控制这个范围，需要你在这个key的下一行单独输入`#END`，再下一行就是正常的key了。

内容根地址如何获取：与包名获取相同，找到那个文件夹（这里称它为`内容根初始地址`），里面的文件夹和.class文件是可以作为内容根地址，越深入，匹配范围越小。一般来说，你要用类匹配，就要知道这个key来源于哪个文件和文件夹，从`内容根初始地址`到某个文件夹或文件的地址，再把`\`全部改成`.`，并删除文件后缀，就是`内容根地址`，然后在前面加上`#`即可。

如果你使用IDEA来反编译获取key，那么在IDEA打开.jar解压的文件夹（叫作项目），在你反编译（双击）一个.class文件后，在文件栏右键单击这个文件，选择`复制路径/引用...`,再选择`来自内容根的路径`，同样要把`\`全部改成`.`即可。

#### 方法名匹配（`&<method>;`）

`method`如何获取：指的是java中的`方法名`，详见[教程](https://www.runoob.com/java/java-methods.html)，要配合类匹配使用

`&<method>;`，这里的`<method>`部分就是`方法名`

### 全功能配置文件
```txt
@iskallia.vault
namespace.modify.the_vault.
1
KEY
@;KEY
@bm;KEY
@bm;@;key
#A
&mt1;KEY
@;&mt2;KEY
@bm;KEY
@bm;&mt3;@;key
\u
#END
#B
KEY
@;KEY
@bm;KEY
@;@bm;KEY
#END
```

模组QQ交流群：点击链接加入群聊【Vault Patcher 模组讨论群】：https://jq.qq.com/?_wv=1027&k=3Slm2Zso
