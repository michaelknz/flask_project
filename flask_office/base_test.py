import pygame
from flask import Flask,render_template
import keyboard

class Base_Test:
    def __init__(self):
        pygame.init()
        self.cur_time=pygame.time.get_ticks()
        self.last_time=pygame.time.get_ticks()
        self.text=''
        self.ref_test=''
        self.key_table_lower=[]
        self.key_table_upper=[]
        self.key_dict=dict()
        self.KeyTable_StartUp()
        self.SetTexts()
        self.shift=False
        self.start_time=500
        self.mid_time=100

    def SetTexts(self):
        self.ref_test='Hello world!&#8628;<br>Great!'

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
        self.key_dict.update({'backspace':[False,False,0]})
        self.key_dict.update({'space':[False,False,0]})
        self.key_dict.update({'enter':[False,False,0]})



    def UpdateTable(self):
        cur_time=pygame.time.get_ticks()
        del_time=cur_time-self.last_time
        self.last_time=cur_time
        if(keyboard.is_pressed('shift')):
            self.shift=True
        else:
            self.shift=False
        if(keyboard.is_pressed('backspace')):
            if(self.key_dict['backspace'][0]==False):
                self.key_dict['backspace'][0]=True
                self.key_dict['backspace'][1]=True
                self.key_dict['backspace'][2]=self.start_time
                self.text=self.text[:len(self.text)-1:]
            else:
                if(self.key_dict['backspace'][2]>0):
                    self.key_dict['backspace'][2]-=del_time
                else:
                    if(self.key_dict['backspace'][1]):
                        self.key_dict['backspace'][2]=self.mid_time
                        self.text=self.text[:len(self.text)-1:]
        else:
            self.key_dict['backspace'][0]=False
            self.key_dict['backspace'][1]=False
            self.key_dict['backspace'][2]=0
        if(keyboard.is_pressed('space')):
            if(self.key_dict['space'][0]==False):
                self.key_dict['space'][0]=True
                self.key_dict['space'][1]=True
                self.key_dict['space'][2]=self.start_time
                self.text+=' '
            else:
                if(self.key_dict['space'][2]>0):
                    self.key_dict['space'][2]-=del_time
                else:
                    if(self.key_dict['space'][1]):
                        self.key_dict['space'][2]=self.mid_time
                        self.text+=' '
        else:
            self.key_dict['space'][0]=False
            self.key_dict['space'][1]=False
            self.key_dict['space'][2]=0

        if(keyboard.is_pressed('enter')):
            if(self.key_dict['enter'][0]==False):
                self.key_dict['enter'][0]=True
                self.key_dict['enter'][1]=True
                self.key_dict['enter'][2]=self.start_time
                self.text+='\n'
            else:
                if(self.key_dict['enter'][2]>0):
                    self.key_dict['enter'][2]-=del_time
                else:
                    if(self.key_dict['enter'][1]):
                        self.key_dict['enter'][2]=self.mid_time
                        self.text+='\n'
        else:
            self.key_dict['enter'][0]=False
            self.key_dict['enter'][1]=False
            self.key_dict['enter'][2]=0
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

    def SetTextOnPage(self):
        out=''
        is_right=2
        j=0
        for i in range(len(self.text)):
            if(self.text[i]==self.ref_test[j] and is_right!=1):
                if(is_right!=2):
                    out+='</span>'
                out+='<span class="right">'+self.ref_test[j]
                is_right=1
                j+=1
            elif(self.text[i]==self.ref_test[j]):
                out+=self.ref_test[j]
                is_right=1
                j+=1
            elif(self.text[i]=='\n'):
                tmp=self.CheckBR(j)
                if(tmp[2] and is_right!=1):
                    if(is_right!=2):
                        out+='</span>'
                    out+='<span class="right">'+tmp[0]
                    is_right=1
                    j=tmp[1]
                elif(tmp[2]):
                    out+=tmp[0]
                    is_right=1
                    j=tmp[1]
                elif(not tmp[2] and is_right!=0):
                    if(is_right!=2):
                        out+='</span>'
                    out+='<span class="wrong">'+tmp[0]
                    is_right=0
                    j=tmp[1]
                elif(not tmp[2]):
                    out+=tmp[0]
                    is_right=0
                    j=tmp[1]
            elif(self.text[i]!=self.ref_test[j] and is_right!=0):
                if(is_right!=2):
                    out+='</span>'
                tmp=self.CheckBR(j)
                if(tmp[2]):
                    out+='<span class="wrong">'+tmp[0]
                    j=tmp[1]
                else:
                    out+='<span class="wrong">'+self.ref_test[j]
                    j+=1
                is_right=0
            elif(self.text[i]!=self.ref_test[j]):
                tmp=self.CheckBR(j)
                if(tmp[2]):
                    out+=tmp[0]
                    j=tmp[1]
                else:
                    out+=self.ref_test[j]
                    j+=1
                is_right=0

        if(is_right!=2):
            out+='</span>'
        out+='<span class="none">'
        for i in range(j,len(self.ref_test)):
            out+=self.ref_test[i]
        out+='</span>'
        return out


    def SendData(self):
        self.UpdateTable()
        return self.SetTextOnPage()

    def RenderBaseTestPage(self):
        return render_template('basetest/basetest.html')

    def CheckBR(self,ind):
        if(self.ref_test[ind:ind+11:]=='&#8628;<br>'):
            return(self.ref_test[ind:ind+11:],ind+11,True)
        else:
            return (self.ref_test[ind:ind+11:],ind+11,False)
