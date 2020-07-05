# worked for python3

# Mac 上执行后，程序会在桌面创建一个文件夹，为每一本书创建一个TXT文件，里面是每一本书的摘录（Kindle内的摘录是按时间顺序存放的）
# 只留下正文，位置、时间全都舍去。记得需要改路径~ digest_path 里面 Users 后的用户名换成你自己的

import os
note_path='/Volumes/Kindle/documents/My Clippings.txt'
f=open(note_path,'r+')
digest_path='/Users/applewu/Desktop/digest/'
os.mkdir(digest_path)
while True:
    onenote=[]
    for i in range(0,5):
        line=f.readline()
        if not line:
            exit()
        onenote.append(line)
    book_note=open('%s%s.txt'%(digest_path,onenote[0]),'a+')
    book_note.write(onenote[3]+'\n')
    book_note.close()

# 作者：知乎用户
# 链接：https://www.zhihu.com/question/23031778/answer/33845296
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。