#! /usr/bin/python3

import pyperclip,re,sys,time,os

clip_file = open("./clip_file.txt")
clip_string = clip_file.readlines()
newline_del = re.compile(r"\n")
default_wait_time = "5"
default_program_mode = "0"

def timer_mode():
    #値が入力されたら値をクリップボード変更の待ち時間に設定する。空白はデフォルト値を入力。それ以外は再度入力させる。
    while True:
        wait_time = input("Please Enter the second to change the next clipboard.(default: {}sec) :".format(default_wait_time))
        if str.isdecimal(wait_time):
            break
        elif wait_time == "":
            wait_time = default_wait_time
            break
        else:
            print("Please insert decimal.")

    for i in range(len(clip_string)):
        clip_string[i] =  newline_del.sub("",clip_string[i])

        for n in range(int(wait_time),-1,-1):
            #カウントダウンをする。前の秒数は\bとflush=Trueで消す。10秒以上（2桁の数値）を入力されると表示がおかしくなる
            print("\b",n,sep="",end="",flush=True)
            if n > 0:
                # os.system("beep -f 300 -l 50")
                os.system("echo 1")
                time.sleep(0.95)
        print("\b" + str(i+1) + "/" + str(len(clip_string)) + "クリップボードに \"" + clip_string[i] + "\" がコピーされました。",flush=True)
        pyperclip.copy(clip_string[i])
        # os.system("beep -f 300 -l 700")
        os.system("echo 2")
        time.sleep(0.3)

def return_mode():
    for i in range(len(clip_string)):
        clip_string[i] = newline_del.sub("",clip_string[i])
        input("If do you want next word, press [return] :")
        print(str(i+1) + "/" + str(len(clip_string)) + ": クリップボードに \"" + clip_string[i] + "\" がコピーされました。")
        pyperclip.copy(clip_string[i])

def list_mode():
    for i in range(len(clip_string)):
        clip_string[i] = newline_del.sub("",clip_string[i])
        print("{}:{}".format(i,clip_string[i]))
    while True:
        clip_number = input("Please input Clipboard number. :")
        if str.isdecimal(clip_number):
            if int(clip_number) < len(clip_string):
                print("クリップボードに" + str(clip_number) + ":" + "\"" + clip_string[int(clip_number)] + "\"がコピーされました。" )
                pyperclip.copy(clip_string[int(clip_number)])
            else:
                print("Please input number less than {}.".format(len(clip_string)))
        else:
            print("Please input correct number.")


try:
    program_mode = input("Which do you want ?(0:Return mode/1:Timer mode/2:List mode)(default:{}) :".format(default_program_mode))
    if program_mode != "0" and program_mode != "1" and program_mode != "2":
        program_mode = default_program_mode
    
    if program_mode == "0":
        return_mode()
    elif program_mode == "1":
        timer_mode()
    elif program_mode == "2":
        list_mode()

except KeyboardInterrupt:
    print("\nProgram was ended.")
    sys.exit()
