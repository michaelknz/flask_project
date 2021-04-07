import pygame
from flask import Flask,render_template
import keyboard

class Text_Editor:
    def __init__(self):
        pygame.init()
        self.cur_time=pygame.time.get_ticks()
        self.last_time=pygame.time.get_ticks()
        self.text=''
        self.key_table_lower=[]
        self.key_table_upper=[]
        self.key_table_special=[]
        self.key_dict=dict()
        self.KeyTable_StartUp()
        self.shift=False
        self.start_time=500
        self.mid_time=100

    def KeyTable_StartUp(self):
        for i in range(33,39):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(40,44):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(58,59):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(60,61):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(62,91):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(94,96):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(123,127):
            self.key_table_upper.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(39,40):
            self.key_table_lower.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(44,58):
            self.key_table_lower.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(59,60):
            self.key_table_lower.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(61,62):
            self.key_table_lower.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(91,94):
            self.key_table_lower.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})
        for i in range(96,123):
            self.key_table_lower.append(chr(i))
            self.key_dict.update({chr(i):[False,False,0]})



    def UpdateTable(self):
        cur_time=pygame.time.get_ticks()
        del_time=cur_time-self.last_time
        self.last_time=cur_time
        if(keyboard.is_pressed('shift')):
            self.shift=True
        else:
            self.shift=False
        s=0
        if(self.shift):
            s=self.key_table_upper
        else:
            s=self.key_table_lower
        for i in s:
            if(keyboard.is_pressed(i)):
                if(self.key_dict[i][0]==False):
                    self.key_dict[i][0]=True
                    self.key_dict[i][1]=True
                    self.key_dict[i][2]=self.start_time
                    self.text+=i
                else:
                    if(self.key_dict[i][2]>0):
                        self.key_dict[i][2]-=del_time
                    else:
                        if(self.key_dict[i][1]):
                            self.key_dict[i][2]=self.mid_time
                        self.text+=i
            else:
                self.key_dict[i][0]=False
                self.key_dict[i][1]=False
                self.key_dict[i][2]=0

    def SendData(self):
        self.UpdateTable()
        return self.text

    def RenderEdPage(self):
        return render_template('text_editor/text_editor.html')
