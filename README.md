# Convert-subtitle-files-to-lyrics-files
这个代码的作用是，从剪影上白票的歌词只要txt或者srt，而且内容是这样的： 
1 
00：00：25,500 --> 00：00：31,833  
上天啊 难道你看不出我很爱她

2 00：00：32,466 --> 00：00：35,899  
怎么明明相爱的两个人

3 00： 00：35,900 --> 00：00：38,966
你要拆散他们啊

4 00：00：42,566 --> 00：00：48,466  
上天啊 你千万不要偷偷告诉她
（长度问题就只展示这一段）

音乐软件无法读取
这个段代码就是把这样的文件给批量改成正常的lrc歌词文件，可以让音乐软件读取：
[00:25.50] 上天啊 难道你看不出我很爱她
[00:32.47] 怎么明明相爱的两个人
[00:35.90] 你要拆散他们啊
[00:42.57] 上天啊 你千万不要偷偷告诉她
使用方法给srt_folder和output_folder分别分别赋值需要处理的文件夹和处理后文件保存所用的文件夹
