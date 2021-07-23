## 几个python脚本

## 说明：

使用前请先安装python[https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)

### copyEachFoldersFirstFile.py

会把同级目录下的所有文件夹的第一个文件复制到cover文件夹内

用途：复制出漫画封面

### renameToTC.py

会把[换成[[]，]换成[]]
例如
[頭文字D_InitialD][重野秀一][尖端]
变成
[[]頭文字D_InitialD[]][[]重野秀一[]][[]尖端[]]Vol_[C]

用途：total commander 中ctrl+m批量重命名多卷漫画使用

输入输出都在renameToTC.txt里

### allFolderFilesRename.py

同级目录下有数个文件夹，每个文件夹里数个文件，没有二级文件夹。

重命名的格式，会自动识别扩展名:

第一个文件夹的文件夹01_001.jpg，到01_030.jpg，如果一共30个文件，扩展名是jpg的话

第二个文件夹的文件夹02_001.jpg，到02_030.jpg，如果一共30个文件，扩展名是jpg的话

以此类推

如果把allFolderFilesRename.py改名其他名字，如123_.py，那文件名就是123_01_01.jpg

第一个文件夹的数字，请修改dirCount

### 根据rarzip文件是否包含文件夹分类（拖拽，多个文件或文件夹）.py

把zip，rar文件分成2类并放入对应的文件夹里

1.包含一个或多个二级文件夹。2.仅包含文件的。

需要pip3 install zipfile，pip3 install rarfile

### 生成所有子文件目录到文件夹名.txt（拖拽，仅多个文件夹）.py

把和py文件当前目录下所有文件夹和子文件夹的名字（默认相对路径，可选绝对路径）输出到文件夹名.txt中

### listFirstAndSecondFoldersToTwoFIles.py

把和py文件当前目录的同级文件夹名字，输出到firstFoldersName.txt中
把和py文件当前目录的所有子文件夹名字，输出到secondFoldersName.txt中

### 生成目录.html，支持搜索，简繁转换（拖拽，仅一个文件夹）.py

适用于搜索，分享，查看所有的库存资源

拖拽文件夹到py文件，被拖拽的目录下的所有文件，生成文件夹名.html，可搜索，点击Name回到首页

main()函数前几行可以进行一些自定义设置，文件夹名加粗显示

可进行的设置：显示完整地址还是只显示文件名，是否显示处理过程，键盘按键抬起立刻搜索还是按回车搜索，相对路径还是绝对路径，显示文件夹和文件还是只显示文件夹，是否显示文件大小，点击文件夹是搜索包含这个文件夹名的所有路径还是跳转到这个文件夹

自动搜索中文简体和繁体，可显示搜索结果的文件和文件夹的数量和总大小

html后加?search=关键词，打开网页时后自动显示搜索结果，例如1.html?search=伊藤润二

支持排除关键词，文件名中有关键词的文件不会写到html里，文件45行，keyWords = ['关键词1','关键词2','关键词3']

### 把文件夹内的文件重命名成文件夹名+Vol_序号的格式（拖拽，仅多个文件夹）.py

**适用于已排序好的需要重命名的文件，拖拽文件夹拖到py文件上**

使用把文件夹内的文件重命名成文件夹名+Vol_序号的格式（拖拽，仅多个文件夹）.py

文件夹名的格式要符合"[书名][作者][出版社][扫者][10完]"，里面的文件会重命名成"[书名][作者][出版社][扫者]Vol_XX.XXX"的形式

以"完]"或"全]"结尾的，最后一个文件名会加上" End"，以"未]"结尾或其他结尾的则不加

按文件夹名批量重命名已排序好的文件，文件名无要求，但顺序要对

01,02,03......09,10可以。1,2,3......9,10这样顺序会出错

文件夹里可以是文件，或者文件夹，不支持混合

会生成日志和恢复文件名的bat文件，不过不想生成，就修改文件里的createLogAndRecover = False

### 交换文件或文件夹名前两个[]的内容（拖拽，多个文件或文件夹）.py

**把[扫者]放在Vol之后，适用于多个扫者的情况下卷的顺序错乱的情况，拖拽文件（夹）拖到py文件上**

把文件（夹）名中最后[]的内容和Vol_XX交换位置

文件（夹）名格式[书名][作者][出版社][扫者]Vol_XX，会重命名成"[书名][作者][出版社]Vol_XX[扫者]"

支持多个文件夹或文件一起拖拽

### 交换文件名最后[]和Vol_XX（拖拽，多个文件夹，文件名格式[][][][]Vol_XX）.py

把[扫者]放在Vol之后

适用于多个扫者的情况下卷的顺序错乱的情况

把文件夹或文件名字中最后[]和Vol_XX的内容交换位置，文件名格式[][][][]Vol_XX，支持多个文件夹或文件一起拖拽

### 删除文件结尾的.1234（拖拽，多个文件或文件夹）.py

把文件夹内后缀名是.1234文件，去掉.1234，支持多个文件夹或文件一起拖拽

### removeFilenameBefore-.py

文件夹名是 xxx - xxx.xxx的格式时，删除前面的xxx和 - ，只剩后面的xxx.xxx，拖拽文件夹到py上运行

### 文件夹和二级文件名简体转繁体（拖拽，多个文件或文件夹）.py
### 文件夹和二级文件名繁体转简体（拖拽，多个文件或文件夹）.py

拖拽文件或文件夹到py上，被拖拽的文件夹和里面的二级目录的文件夹和文件名都会被转换

需要pip install opencc-python-reimplemented

### 文件和文件夹夹繁体转简体，不转换二级目录（拖拽，仅文件夹）.py
### 文件和文件夹名简体转繁体，不转换二级目录（拖拽，仅文件夹）.py

拖拽文件或文件夹到py上，二级目录的文件夹和文件名不会被转换

需要pip install opencc-python-reimplemented

### 解压双重分割打包的RAR（拖拽，仅多个文件夹，需要UnRAR.exe）.py

需要UnRAR.exe 或 pip3 install unrar

识别两层rar的文件结尾.part1.rar

### 识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件夹，文件夹名格式[作品][作者]XX）.py

文件名格式[书名][作者]XX.XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号），被拖拽的文件会被移动到作品名文件夹里

### 识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件夹，可简繁转换，文件夹名格式[作品][作者]XX）.py

文件夹名格式[书名][作者]XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号），被拖拽的文件夹里的文件会被移动到作品名文件夹里

需要pip install opencc-python-reimplemented

### 识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件，文件名格式[作品][作者]XX）.py

文件夹名格式[书名][作者]XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号）

被拖拽的文件夹里的文件会被移动到作品名文件夹里

### 识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件，可简繁转换，文件名格式[作品][作者]XX）.py

文件名格式[书名][作者]XX.XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号），被拖拽的文件会被移动到作品名文件夹里

需要pip install opencc-python-reimplemented

### 百度网盘网址#提取码直接识别跳转.js

把百度网盘链接改成这种形式：

https://pan.baidu.com/s/xxxxxxx#yyyy

yyyy是提取码

脚本会自动识别，填写提取码，进入文件列表

### 百度网盘链接提取码格式批量转换（拖拽，仅多个txt文件）.py

把存储百度网盘链接的txt文件拖到py上

原格式：链接: https://pan.baidu.com/s/xxxxxxxxx 提取码: yyyy 复制这段内容后打开百度网盘手机App，操作更方便哦	

新格式：https://pan.baidu.com/s/xxxxxxxxx#yyyy

源文件名：链接.txt

新文件名：链接.txt.txt

可以直接在notepad++里双击进去链接，配合上面的tampermonkey脚本，可直接进入文件列表

txt要是UTF-8编码，可用记事本打开另存为时修改

### 复制出RAR或ZIP文件中的第一个文件（拖拽，多个文件或文件夹）.py

需要UnRAR.exe 或 pip3 install unrar

常用于提取漫画封面

支持压缩包里有一层或两层文件夹的情况

### 给无扩展名的文件添加扩展名，rar为例（拖拽，多个文件或文件夹）.py

添加扩展名

### 把文件或文件夹名重命名为翻转的形式（拖拽，多个文件或文件夹，包含二级目录文件）.py

例12345.txt会重命名成54321.txt

如果拖拽文件夹，文件夹名和里面的文件名都会翻转

### 识别rarzip内是否有文件名是关键词的文件，(公众号)为例（拖拽，多个文件或文件夹，支持多层文件夹）.py

如果压缩包里有文件夹包含"公众号"3个字，就会显示出这个压缩包的名字

### 计算文件sha1（拖拽，多个文件或文件夹）.py

拖拽文件或文件夹到py上，生成的.txt在和文件同级目录，在文件夹目录内

可选项：.txt还是其他格式，是否显示文件大小

### 根据漫画补档网址，生成帖子名.txt包含网址发布时间一楼内容.py

修改py内的url，获取漫画补档的某个帖子内容

## 使用前请备份，防止文件名不符合你的需求