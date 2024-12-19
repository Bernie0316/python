#分解檔案字符串(string):====================
colors = "red green blue yellow"
#展開字串
color_parts = colors.split()
#在splie()可以用("")來命令分開任何字元
#來做個比較
print(colors)
#展開後:
print(color_parts)
#可以印出其中一個 #這邊我印第一個[0]
print(color_parts[0])
#去除多餘的空白格==============================
name = "Bernie Zhong   "
no_space = name.strip()
print(f"----{name}----")
print(f"----{no_space}----")


#How to open text file and read them in python
#.txt .py 檔案名稱後面會顯示是哪種檔案
#現在我們有一個text檔在VScode，我們來打開它
#第一種開啟方式:
#hr_system = open("hr_system.txt")
#第二種開啟檔案的方式:
with open("hr_system.txt") as hr_system:
# line 會把text檔解讀
    for line in hr_system:
        #line = Alexia 1913 Engineer 84000
        parts = line.split(" ")
        name = parts[0]
        birthday = int(parts[1])
        position = parts[2]
        薪水 = int(parts[3])
        print(f"Name:{name} - {birthday} - {position} - {薪水}")


