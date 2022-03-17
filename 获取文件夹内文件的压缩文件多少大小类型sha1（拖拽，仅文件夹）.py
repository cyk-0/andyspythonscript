# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript


from pathlib import Path
from hashlib import sha1

import sys
import zipfile
import rarfile

# pip install rarfile, zipfile

def formatFileSize(sizeBytes):
    # 格式化文件大小
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B"
    if(result > 1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if(result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024):
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024):
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024):
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result, '.2f') + suffix
    
    
def getSha1(filename):
    # 计算sha1
    sha1Obj = sha1()
    with open(filename, 'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()
    
    
def writeFile(aPath, filereadlines):
    # 写入md文件
    # 放在文件夹外面
    #newfile = open(aPath.parent.joinpath(aPath.name + '.md'), mode='w', encoding='UTF-8')
    # 放在文件夹里面，html格式
    newfile = open(aPath, mode='w', encoding='UTF-8')
    # markdown格式
    newfile = open(aPath, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()  
    
    
def arrayFormatToHTML(myArray):
    # 转换成html格式
    returnFileInfo = []
    returnFileInfo.append('<html><head><title>文件信息</title><style>table{width:auto;}table,td{border:1px solid #000000;table-layout:fixed;border-collapse:collapse;}table td:first-child{width:auto;}table td{min-width:100px;}a{text-decoration: none;}table tr:first-child{background-color:#eee;}tr:hover{background-color:#eee;}</style></head><body><table id="allFileTable"><tr><td>文件夹名</td><td>文件类型</td><td>文件大小</td><td>压缩包内文件数量</td><td>压缩包内文件夹数量</td><td>扩展名对应的文件数量</td><td>SHA1校验码</td></tr>')
    
    for eachInfo in myArray:
        newContent = '<tr>'
        for eachString in eachInfo:
            newContent = newContent + '<td>' + str(eachString) + '</td>'
        returnFileInfo.append(newContent + '</tr>')
    returnFileInfo.append('</table></body></html>')
    print(returnFileInfo)
    return returnFileInfo
    
    
def arrayFormatToMD(myArray):
    # 转换成markdown格式
    returnFileInfo = []
    returnFileInfo.append('|文件夹名|文件类型|文件大小|压缩包内文件数量|压缩包内文件夹数量|扩展名对应的文件数量|SHA1校验码|\n')
    returnFileInfo.append('| --- | --- | --- | --- | --- | --- | --- |\n')
    
    for eachInfo in myArray:
        newContent = '|'
        for eachString in eachInfo:
            newContent = newContent + str(eachString) + '|'
        returnFileInfo.append(newContent + '\n')
    return returnFileInfo
    
def getFileInfo(directoryPath, filePath):
    # Path(filePath)
    eachFileInfo = []
    dirCount = 0
    fileCount = 0
    fileType = {}
    
    if zipfile.is_zipfile(filePath):
        zf = zipfile.ZipFile(filePath)
        for eachFile in zf.infolist():
            if eachFile.is_dir():
                dirCount = dirCount + 1
            else:
                fileCount = fileCount + 1
                if (Path(eachFile.filename).suffix not in fileType):
                    fileType[Path(eachFile.filename).suffix] = 1
                else:
                    fileType[Path(eachFile.filename).suffix] = fileType[Path(eachFile.filename).suffix] + 1
        zf.close()
    if rarfile.is_rarfile(filePath):
        rf = rarfile.RarFile(filePath)
        for eachFile in rf.infolist():
            if eachFile.is_dir():
                dirCount = dirCount + 1
            else:
                fileCount = fileCount + 1
                if (Path(eachFile.filename).suffix not in fileType):
                    fileType[Path(eachFile.filename).suffix] = 1
                else:
                    fileType[Path(eachFile.filename).suffix] = fileType[Path(eachFile.filename).suffix] + 1
        rf.close()
        
    eachFileInfo.append(filePath.name)
    eachFileInfo.append(filePath.suffix[1:])
    eachFileInfo.append(formatFileSize(filePath.stat().st_size))
    eachFileInfo.append(fileCount)
    eachFileInfo.append(dirCount)
    tempFileType = ''
    for key in fileType:
        tempFileType = tempFileType + key[1:] + '=' + str(fileType[key]) + ', '
    eachFileInfo.append(tempFileType[:-2])
    eachFileInfo.append(getSha1(filePath))
    return eachFileInfo
    
def main(inputPath): 
    del inputPath[0]
    # 所有信息
    # 每个文件的信息：|文件夹名|文件类型，文件大小|压缩包内文件数量|压缩包内文件夹数量|扩展名对应的文件数量|SHA1校验码
    allFileInfo = []
    #转换成html = True, markdown = False
    fileType = True
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'): 
                if Path.is_file(Path(file)):
                    allFileInfo.append(getFileInfo(Path(aPath), file))
            if fileType:
                writeFile(Path(aPath).joinpath(Path(aPath).name + '.html'), arrayFormatToHTML(allFileInfo))
            else:
                writeFile(Path(aPath).joinpath(Path(aPath).name + '.md'), arrayFormatToMD(allFileInfo))
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass