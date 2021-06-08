# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path

def formatFileSize(sizeBytes):
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B";
    if(result>1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if(result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024) :
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result,'.2f') + suffix
        
def writefile(filereadlines):
    fileName = str(Path.cwd().name) + '.html'
    newfile = open(fileName, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main():
    # 显示完整地址 = 1，还是只显示文件名 = 0
    showAllAddress = 0
    # 第一栏的宽度，first column width %
    columnWidth = 80
    # 是否显示边框，show table border = 1, no border = 0
    showTableBorder = 1
    # 是否显示第一行，show first line = 1, no first line = 0(Name, sha1, file size)
    showFirstLine = 1
    # 是否显示处理过程, show process details = 1, no detils = 0
    showProcessDetails = 1
    # 键盘按键抬起立刻搜索 = 'onkeyup'，还是按回车搜索 = 'onchange'，文件数大于两万建议后者
    howToReactSearch = 'onkeyup'
    # 相对路径 = 1，还是绝对路径 = 0
    showPath = 1
    # 显示文件夹和文件 = 1，还是只显示文件夹 = 0
    showFolderAndFile = 1
    # 是否显示文件大小，show file size = 1, no file size = 0
    showFileSize = 1
    # 点击文件夹的操作，搜索包含这个文件夹名的所有路径 = 1，跳转到这个文件夹 = 0
    clickFolder = 1
    
    title = str(Path.cwd().name)
    outputFile = '<html><head><title>' + title + '</title>\n'
    outputFile = outputFile + '<style>body{width:90%;}table,td{border:' + str(showTableBorder) +'px solid #000000;table-layout:fixed;border-collapse:collapse;}a{color:#000000;text-decoration: none;}td{width:10%;}table tr td:first-child{width:' + str(columnWidth) +'%;}table tr:first-child{background-color:#eee;}tr:hover{background-color:#eee;}.folder{font-weight:bold;}</style>\n'
    outputFile = outputFile + '<script type="text/javascript" language="JavaScript">function onSearch(){searchContent = document.getElementById(\'mySearch\').value;var storeId = document.getElementById(\'allFileTable\');var rowsLength = storeId.rows.length;for(var i=1;i<rowsLength;i++){var searchText = storeId.rows[i].cells[0].innerHTML;if(searchText.match(searchContent) || searchText.toUpperCase().match(searchContent.toUpperCase())){storeId.rows[i].style.display=\'\';}else{storeId.rows[i].style.display=\'none\';}}}function clickFolder(){document.getElementById("mySearch").value = event.target.innerHTML;onSearch();}function frontpage(){var storeId = document.getElementById(\'allFileTable\');var rowsLength = storeId.rows.length;for(var i=1;i<rowsLength;i++){storeId.rows[i].style.display=\'\';}}</script>\n'
    outputFile = outputFile + '</head><body><div>\n<table id="allFileTable">'
    if showFirstLine:
        if showFileSize and showFolderAndFile:
            outputFile = outputFile + '<tr><td><span id="fileNameID"></span><input type="text" id="mySearch" ' + howToReactSearch + '="onSearch()" placeholder="搜索..."></td><td>Size</td></tr>'
        if (not showFileSize) or (not showFolderAndFile):
            outputFile = outputFile + '<tr><td>File name:<input type="text" id="mySearch" ' + howToReactSearch + '="onSearch()" placeholder="搜索..."></td></tr>'
    fileCount = 0
    fileSizeCount = 0
    folderCount = 0

    mypath = Path('.')
    for file in mypath.glob('**/*'):
        if showPath:
            loc = file.parent.joinpath(file.name)
        else:
            loc = Path.cwd().joinpath(file)
            print(loc)
        if showProcessDetails:
            print(loc)
        if showAllAddress:
            showName = str(loc)
            showAddr = str(loc)
        else:
            showName = str(file.name)
            showAddr = str(loc)
        if Path.is_dir(file):
            folderCount = folderCount + 1
            showName = '<span class="folder">' + showName + '</span>'
        if Path.is_file(file):
            fileCount = fileCount + 1
        if showFolderAndFile and showFileSize:
            fileSize = Path(loc).stat().st_size
            showFileSize = formatFileSize(fileSize)
            fileSizeCount = fileSizeCount + fileSize
            if clickFolder and Path.is_dir(file):
                outputFile = outputFile + '<tr><td><a onclick="clickFolder()" href="javascript:void(0);">' + showName + '</td><td>' + showFileSize + '</a></tr>\n'
            else:
                outputFile = outputFile + '<tr><td><a href="' + showAddr + '">' + showName + '</td><td>' + showFileSize + '</a></tr>\n'
        if (not showFolderAndFile and Path.is_dir(file)) or (not showFileSize):
            if clickFolder:
                outputFile = outputFile + '<tr><td><a onclick="clickFolder()" href="javascript:void(0);">' + showName + '</a></td></tr>\n'
            else:
                outputFile = outputFile + '<tr><td><a href="' + showAddr + '">' + showName + '</a></td></tr>\n'
   
    outputFile = outputFile + '</td></table></div></body></html>'
    outputFile = outputFile + '<script type="text/javascript" language="JavaScript">document.getElementById("fileNameID").innerHTML = "<a href=\\"javascript:frontpage()\\">Name</a> (' + str(fileCount) + ' files in ' + str(folderCount) + ' folders'
    if showFileSize:
        outputFile = outputFile + ', '+ formatFileSize(fileSizeCount)
    outputFile = outputFile +  ') ";</script>'
    writefile(outputFile)
    
if __name__ == '__main__':
    main()