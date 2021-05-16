from flask import render_template
import consts

class Profile:
    def __init__(self):
        pass
    def Render_Profile(self):
        return render_template('profile/profile.html',timeBT=self.Redo_timeBT(),misstakesBT=consts.user.misstakesBT,timeBM=self.Redo_timeBM(),misstakesBM=consts.user.misstakesBM,name=consts.user.nickname,email=consts.user.email)

    def Redo_timeBT(self):
        if(int(consts.user.timeBT)==-1):
            return consts.user.timeBT
        else:
            m=str((int(consts.user.timeBT)//1000)//60)
            if(len(m)==1):
                m='0'+m
            s=str((int(consts.user.timeBT)//1000)%60)
            if(len(s)==1):
                s='0'+s
            return m+':'+s

    def Redo_timeBM(self):
        if(int(consts.user.timeBM)==-1):
            return consts.user.timeBM
        else:
            m=str((int(consts.user.timeBM)//1000)//60)
            if(len(m)==1):
                m='0'+m
            s=str((int(consts.user.timeBM)//1000)%60)
            if(len(s)==1):
                s='0'+s
            return m+':'+s
