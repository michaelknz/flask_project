import pygame
from models import User
from flask import Flask,render_template,redirect,url_for
from random import randint
from models import db
import keyboard
import consts

class Base_Test:
    def __init__(self):
        pygame.init()
        self.SetMasText()
        self.cur_time=pygame.time.get_ticks()
        self.last_time=pygame.time.get_ticks()
        self.text=''
        self.ref_test=''
        self.to_next_string='&#8628;<br>'
        self.key_table_lower=[]
        self.key_table_upper=[]
        self.key_dict=dict()
        self.KeyTable_StartUp()
        self.SetTexts()
        self.shift=False
        self.time=0
        self.mistakes=0
        self.start_time=500
        self.mid_time=100
        self.is_first_key=False
        self.is_finish=False

    def SetTexts(self):
        self.ref_test1=self.mas_texts[randint(0,len(self.mas_texts)-1)]
        self.ref_test=''
        for i in self.ref_test1:
            if(i=='\n'):
                self.ref_test+=self.to_next_string
            else:
                self.ref_test+=i

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
        if(del_time>=500):
            del_time=0
            self.SetStart()
        self.time+=del_time
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
                self.is_first_key=False
            else:
                if(self.key_dict['backspace'][2]>0):
                    self.key_dict['backspace'][2]-=del_time
                else:
                    if(self.key_dict['backspace'][1]):
                        self.key_dict['backspace'][2]=self.mid_time
                        self.text=self.text[:len(self.text)-1:]
                        self.is_first_key=False
        else:
            self.key_dict['backspace'][0]=False
            self.key_dict['backspace'][1]=False
            self.key_dict['backspace'][2]=0
        if(len(self.text)==len(self.ref_test1)):
           b=self.CheckTexts()
           if(b==False):
               return
           else:
               if(consts.is_auth==False):
                   self.is_finish=True
                   return
               if(int(consts.user.timeBT)>self.time or int(consts.user.timeBT)==-1):
                   User.query.get(consts.user.id).timeBT=self.time
                   User.query.get(consts.user.id).misstakesBT=self.mistakes
               if(int(consts.user.misstakesBM)>self.mistakes or int(consts.user.timeBM)==-1):
                   User.query.get(consts.user.id).timeBM=self.time
                   User.query.get(consts.user.id).misstakesBM=self.mistakes
               self.is_finish=True
               db.session.commit()
               return
        if(keyboard.is_pressed('space')):
            if(self.key_dict['space'][0]==False):
                self.key_dict['space'][0]=True
                self.key_dict['space'][1]=True
                self.key_dict['space'][2]=self.start_time
                self.text+=' '
                self.is_first_key=True
            else:
                if(self.key_dict['space'][2]>0):
                    self.key_dict['space'][2]-=del_time
                else:
                    if(self.key_dict['space'][1]):
                        self.key_dict['space'][2]=self.mid_time
                        self.text+=' '
                        self.is_first_key=True
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
                self.is_first_key=True
            else:
                if(self.key_dict['enter'][2]>0):
                    self.key_dict['enter'][2]-=del_time
                else:
                    if(self.key_dict['enter'][1]):
                        self.key_dict['enter'][2]=self.mid_time
                        self.text+='\n'
                        self.is_first_key=True
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
                    self.is_first_key=True
                else:
                    if(self.key_dict[i][2]>0):
                        self.key_dict[i][2]-=del_time
                    else:
                        if(self.key_dict[i][1]):
                            self.key_dict[i][2]=self.mid_time
                        self.text+=i
                        self.is_first_key=True
            else:
                self.key_dict[i][0]=False
                self.key_dict[i][1]=False
                self.key_dict[i][2]=0

    def SetTextOnPage(self):
        out=''
        is_right=2
        j=0
        out+='<span id="timer">Time: '+self.GetTimer()+'</span>'
        out+='<span id="mistakes">Mistakes : '+str(self.mistakes)+'</span>'
        out+='<div class="text_block">'
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
                    if(self.is_first_key and i==len(self.text)-1):
                        self.is_first_key=False
                        self.mistakes+=1
                    j=tmp[1]
                elif(not tmp[2]):
                    out+=tmp[0]
                    is_right=0
                    if(self.is_first_key and i==len(self.text)-1):
                        self.is_first_key=False
                        self.mistakes+=1
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
                if(self.is_first_key and i==len(self.text)-1):
                    self.is_first_key=False
                    self.mistakes+=1
                is_right=0
            elif(self.text[i]!=self.ref_test[j]):
                tmp=self.CheckBR(j)
                if(tmp[2]):
                    out+=tmp[0]
                    j=tmp[1]
                else:
                    out+=self.ref_test[j]
                    j+=1
                if(self.is_first_key and i==len(self.text)-1):
                    self.is_first_key=False
                    self.mistakes+=1
                is_right=0

        if(is_right!=2):
            out+='</span>'
        out+='<span class="none">'
        for i in range(j,len(self.ref_test)):
            out+=self.ref_test[i]
        out+='</span>'
        out+='</div>'
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

    def GetTimer(self):
        m=str((self.time//1000)//60)
        s=str((self.time//1000)%60)
        if(len(m)==1):
            m='0'+m
        if(len(s)==1):
            s='0'+s
        return m+':'+s

    def SetMasText(self):
        self.mas_texts=[]
        self.mas_texts.append('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam interdum augue ut est condimentum molestie. Fusce in felis in mi tempus\niaculis. Aliquam nec viverra nisi, nec tempor odio. Donec sagittis iaculis sapien eget elementum. Suspendisse est libero, vulputate eget\nturpis nec, accumsan tempus magna. Integer massa arcu, gravida eget massa a, malesuada molestie nibh. Phasellus sit amet sapien\nvestibulum, venenatis dui ac, faucibus sapien. Etiam vel nunc enim. Etiam id congue mi. Donec eu dictum risus. Curabitur nec massa\nsuscipit, facilisis urna sed, egestas neque. Suspendisse potenti. Proin vel enim ut ex efficitur cursus vitae sed erat. Duis libero mi,\nsollicitudin et mollis sed, condimentum at nunc.')
        self.mas_texts.append('Aenean semper tortor tristique tortor ultrices, et pharetra tortor euismod. Mauris maximus eleifend ante. Sed sodales, felis at vestibulum\nporttitor, est est consectetur lacus, interdum malesuada nunc nunc in sem. Sed ante est, commodo at nunc a, cursus aliquam neque.\nNullam aliquam scelerisque magna, sed lobortis tellus tristique id. Sed eget sem metus. Vivamus sed turpis urna. Ut ante felis, sagittis ut\nscelerisque vitae, hendrerit in augue. Aliquam ac semper quam, vel iaculis velit. Fusce auctor lacinia purus non mollis. Donec hendrerit\nblandit mattis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris eros nunc, ullamcorper in\nfringilla sed, congue sit amet odio. Maecenas ut ultricies lectus.')
        self.mas_texts.append('Vestibulum dolor nunc, mollis ac scelerisque id, bibendum nec mi. Sed mollis rhoncus tellus, blandit bibendum urna dictum ac. Cras quis\nlectus blandit sem ultrices feugiat. Sed eget suscipit quam. Donec dictum molestie turpis, in dapibus augue posuere quis. Quisque porta\nporttitor diam, a varius purus sodales sit amet. Proin efficitur mollis diam vitae ultrices. Sed euismod malesuada auctor. Pellentesque\nconsectetur magna non justo placerat sagittis. Phasellus nec nisi et justo tristique finibus. Duis finibus purus vel facilisis blandit. Phasellus consequat molestie augue, egestas maximus ex. Duis accumsan orci vehicula dictum finibus. Curabitur bibendum metus at diam facilisis,\nvel posuere lorem volutpat. Aenean sit amet enim posuere, consectetur metus non, sollicitudin libero. Donec sed sodales nulla.')
        self.mas_texts.append('Ut sodales mi sit amet pellentesque varius. Suspendisse eget nibh eget turpis rhoncus tempor ut eget ante. In hac habitasse platea\ndictumst. Aenean eleifend est felis, vitae consectetur orci convallis nec. Curabitur fermentum, orci a varius condimentum, erat odio\negestas diam, eget gravida leo orci non nisi. Maecenas venenatis neque elementum turpis pharetra congue. In id quam eget nibh efficitur\nplacerat. Nunc in justo accumsan, vulputate eros a, semper urna. Phasellus neque purus, rutrum in tortor at, lobortis posuere lectus. Sed\nornare pharetra velit, eu volutpat nunc aliquet in. Ut magna nunc, aliquam nec massa eget, maximus dictum augue. Praesent vel molestie\nmi. Vivamus laoreet justo nec feugiat imperdiet.')
        self.mas_texts.append('In aliquet cursus aliquet. Cras risus mauris, imperdiet id diam eu, tincidunt pharetra leo. Sed blandit interdum dignissim. Donec vel massa\nsed velit pretium eleifend. Pellentesque auctor nunc auctor dui vestibulum volutpat. Ut porta sapien a lacus pellentesque posuere. Ut\ncursus pharetra tristique. Pellentesque at risus et dolor sodales sagittis. Cras ut feugiat nibh. Praesent at lectus porttitor, laoreet nisl nec,\nelementum purus. Donec erat purus, aliquet at sapien a, tristique congue augue. Ut at turpis arcu. Fusce sed orci pretium, scelerisque elit\neu, faucibus erat. Morbi feugiat eleifend sapien ac molestie.')

    def SetStart(self):
        self.text=''
        self.SetTexts()
        self.mistakes=0
        self.time=0
        self.is_finish=False

    def CheckTexts(self):
        for i in range(len(self.text)):
            if(self.text[i]!=self.ref_test1[i]):
                return False
        return True

    def GetFin(self):
        return str(int(self.is_finish))
