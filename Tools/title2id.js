/** 
@info  动将Markdown文件中的三级标题，链接在标题末尾；只需浏览器github中markdown预览，F12-Console运行本段脚本即可
@author 顾晓 https://github.com/chenyanzz
*/

for (var e of document.getElementsByTagName("h3")) 
    if(e.firstChild && e.firstChild.id) 
        e.innerHTML += 
            "<span style=\"color: red;\">#" + 
            e.firstChild.id.replace("user-content-","") + 
            "</span>";