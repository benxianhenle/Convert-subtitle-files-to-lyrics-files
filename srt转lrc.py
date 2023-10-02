import os

# 指定SRT文件所在文件夹和目标文件夹
srt_folder =  r"C:\Users\86150\Desktop\临时文件夹\过程\歌词"
output_folder = "C:\\Users\\86150\\Desktop\\临时文件夹\\过程\\新建文件夹\\output\\"

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历SRT文件夹中的所有SRT文件
for filename in os.listdir(srt_folder):
    if filename.endswith(".srt"):
        srt_file_path = os.path.join(srt_folder, filename)

        # 打开SRT文件以供读取
        with open(srt_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 初始化变量以保存提取的内容
        output_lines = []
        current_time = None
        current_text = []

        # 遍历SRT文件的每一行
        for line in lines:
            line = line.strip()  # 去除行首尾的空白字符
            if line.isdigit():
                # 行是字幕序号，将当前文本保存到输出
                if current_time and current_text:
                    # 修改时间格式，将毫秒转换为秒并保留两位小数
                    time_parts = current_time.split(',')
                    if len(time_parts) == 2:
                        milliseconds = f"{round(int(time_parts[1]) / 1000, 2):.2f}"
                        current_time = f"[{time_parts[0][3:]}{milliseconds}]"
                        #去除浮点数的0和.
                        current_time = current_time[:-5] + current_time[-4:]
                        #print(current_time)
                    output_lines.append(f"{current_time} {' '.join(current_text)}")
                current_time = None
                current_text = []
            elif '-->' in line:
                # 行包含时间信息，提取时间
                times = line.split(' --> ')
                if len(times) == 2:
                    current_time = times[0].strip()
                    #print(current_time)
                    #current_time = current_time[:-5] + current_time[-4:]
            elif line:
                # 行包含文本内容，添加到当前文本列表
                current_text.append(line)

        # 处理最后一个字幕
        if current_time and current_text:
            # 修改时间格式，将毫秒转换为秒并保留两位小数
            time_parts = current_time.split(',')
            if len(time_parts) == 2:
                milliseconds = f"{round(int(time_parts[1]) / 1000, 2):.2f}"
                current_time = f"[{time_parts[0][3:]}{milliseconds}]"
                current_time = current_time[:-5] + current_time[-4:]
                #print(current_time)
            output_lines.append(f"{current_time} {' '.join(current_text)}")

        # 构建输出文件名，并将后缀改为lrc
        output_filename = os.path.splitext(filename)[0] + ".lrc"
        output_filepath = os.path.join(output_folder, output_filename)

        # 将提取的内容保存为LRC格式文件
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(output_lines))

print("提取完成，内容已保存为LRC格式文件到指定的文件夹中。")
