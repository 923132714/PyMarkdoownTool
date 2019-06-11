# PyMarkdoownTool


That is a tool that allows us to easily modify Markdown files in bulk


<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>


[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

## 起因

因为要迁移博客，要改markdown文件的格式，所以想找一个能用的工具，但是没有搜到相关的项目和软件，于是打算自己造个轮子，主要是为了方便，实现功能，质量能力有限。

## 功能

1. 读写front matter - [ ]
    * 规范化front matter - [ x ]
    * 读取front matter - [ x ]
	* 删除front matter - [ x ]
    * 修改front matter - [ ]
    * 批量操作 - [ ]
2. 修改文件名 - [ ]
    * 加前后缀 - [x]
    * 时间变格式 - [x]
    * 根据front master中信息修改 - [ ]
    * 批量操作 - [ ]
3. 修改文件内指定部分 - [ ]
    * 正则匹配 - [ ]
    * 批量操作 - [ ]


## 使用

1. 读写front matter [python-frontmatter](https://github.com/eyeseast/python-frontmatter "python-frontmatter")



## License


<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>


[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

## 版本信息

版本号 | 版本说明 | 修改日期
-----|--------| ---------
v0.1 | 完成规范化front matter | 2019/ 4/ 16
v0.2 | 完成读取front matter，删除front matter | 2019/ 06/ 06
v0.3 | 修改front matter 文件名解析工具 | 2019/ 06/ 11
