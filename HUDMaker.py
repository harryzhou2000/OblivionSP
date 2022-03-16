
from tkinter import NS
import numpy as np
import numpy.random as random
import re


XC = 0
YC = 0.63


def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True


def V2F(var, zoom=1):
    if(isNum(var)):
        return "%.3g" % (var * zoom)
    else:
        if(zoom != 1):
            return "{(%s)*%.3g;f3}" % (var, zoom)
        else:
            return "{%s;f3}" % (var)


def F_PlaneRotX(R, x, y, zoom=1):
    if(isNum(x)):
        xR = x-XC
    else:
        xR = "%s-%.3g"%(x,XC)
    if(isNum(y)):
        yR = y-YC
    else:
        yR = "%s-%.3g" % (y, YC)

    if(zoom != 1):
        return "((%s-%.3g)*cos(%s)+(%s-%.3g)*sin(%s))*%s+%.3g" % (x, XC, R, y, YC, R, zoom, XC)
    else:
        if(isNum(R) and isNum(xR) and isNum(yR)):
            return "%.3g" % (np.cos(np.deg2rad(R)) * xR + np.sin(np.deg2rad(R)) * yR + XC)
        elif(not isNum(R)):
            if(isNum(xR)):
                xPart = "%.3g*cos(%s)"%(xR,R)
            else:
                xPart = "(%s)*cos(%s)" % (xR, R)
            if(isNum(yR)):
                yPart = "%.3g*sin(%s)" % (yR, R)
            else:
                yPart = "(%s)*sin(%s)" % (yR, R)
            return "%s+%s+%.3g" % (xPart,yPart, XC)
        else:
            return "(%s)*cos(%s)+(%s)*sin(%s)+%.3g" % (xR, R, y, yR, XC)


# def F_PlaneRotY(R, x, y, zoom=1):
#     if(zoom != 1):
#         return "(-(%s-%.3g)*sin(%s)+(%s-%.3g)*cos(%s-%.3g))*%s+%.3g" % (x, XC, R, y, YC, R, zoom, YC)
#     else:
#         return "-(%s-%.3g)*sin(%s)+(%s-%.3g)*cos(%s)+%.3g" % (x, XC, R, y, YC, R, YC)

def F_PlaneRotY(R, x, y, zoom=1):
    if(isNum(x)):
        xR = x-XC
    else:
        xR = "%s-%.3g" % (x, XC)
    if(isNum(y)):
        yR = y-YC
    else:
        yR = "%s-%.3g" % (y, YC)

    if(zoom != 1):
        return "(-(%s-%.3g)*sin(%s)+(%s-%.3g)*cos(%s))*%s+%.3g" % (x, XC, R, y, YC, R, zoom, YC)
    else:
        if(isNum(R) and isNum(xR) and isNum(yR)):
            return "%.3g" % (-np.sin(np.deg2rad(R)) * xR + np.cos(np.deg2rad(R)) * yR + YC)
        elif(not isNum(R)):
            if(isNum(xR)):
                xPart = "%.3g*sin(%s)" % (xR, R)
            else:
                xPart = "(%s)*sin(%s)" % (xR, R)
            if(isNum(yR)):
                yPart = "%.3g*cos(%s)" % (yR, R)
            else:
                yPart = "(%s)*cos(%s)" % (yR, R)
            return "-%s+%s+%.3g" % (xPart, yPart, YC)
        else:
            return "-(%s)*sin(%s)+(%s)*cos(%s)+%.3g" % (xR, R, y, yR, YC)


class RTObject:
    def __init__(self, nR=0, nX=0, nY=0, nSpace=1, nSize=2, nRot=0,
                 ncolor="#00FF00", nalpha="#FF", nContent="^", nZoom=1, nbndX=0, nbndY=0) -> None:
        self.R = nR
        self.X = nX
        self.Y = nY
        self.Space = nSpace
        self.Size = nSize
        self.Rot = nRot
        self.color = ncolor
        self.alpha = nalpha
        self.Content = nContent
        self.zoom = nZoom
        self.bndX = nbndX
        self.bndY = nbndY

    def Parse(self) -> str:
        Head = "<line-height=-0px>"
        Space = "<mspace=%spx>" % (V2F(self.Space, self.zoom))
        Size = "<size=%spx>" % (V2F(self.Size, self.zoom))
        if(self.R != 0):
            X = "(%s)*2" % (F_PlaneRotX(self.R, self.X, self.Y, self.zoom))
            Y = "%s" % (F_PlaneRotY(self.R, self.X, self.Y, self.zoom))
        else:
            if(isNum(self.zoom)):
                if(self.zoom == 1):
                    if(isNum(self.X) and isNum(self.Y)):
                        X = "%.3g" % (self.X * 2)
                        Y = "%.3g" % (self.Y)
                    else:
                        X = "(%s)*2" % (self.X)
                        Y = "(%s)" % (self.Y)
                else:
                    if(isNum(self.X) and isNum(self.Y)):
                        X = "%.3g" % (self.X * 2* self.zoom)
                        Y = "%.3g" % (self.Y* self.zoom)
                    else:
                        X = "(%s)*2*%.3g" % (self.X, self.zoom)
                        Y = "(%s)*%.3g" % (self.Y, self.zoom)
            else:
                if(isNum(self.X) and isNum(self.Y)):
                    X = "%.3g*(%s)" % (self.X * 2, self.zoom)
                    Y = "%.3g*(%s)" % (self.Y, self.zoom)
                else:
                    X = "(%s)*2*(%s)" % (self.X, self.zoom)
                    Y = "(%s)*(%s)" % (self.Y, self.zoom)

        if(self.bndX != 0 or self.bndY != 0):
            Xstr = X; Ystr=Y
            if(isNum(X)):
                Xstr = "%.3g"%(X)
            if(isNum(Y)):
                Ystr = "%.3g"%(Y)
            Alpha = "<alpha={abs(%s-%.3g)<%.3g & abs(%s-%.3g)<%.3g ? \"%s\": \"#00\" }>" % (Xstr, 2*XC, 2*self.bndX, Ystr, YC, self.bndY, self.alpha
                                                                                    )
        else:
            Alpha = "<alpha=%s>" % (self.alpha)

        if(self.bndX != 0 or self.bndY != 0):
            if(isNum(X)):
                X = "clamp(%.4f,%.3g,%.3g)" % (X, 2*(XC-self.bndX), 2*(XC+self.bndX))
            else:
                X = "clamp(%s,%.3g,%.3g)" % (
                    X, 2*(XC-self.bndX), 2*(XC+self.bndX))
            if(isNum(Y)):
                Y = "clamp(%.4f,%.3g,%.3g)" % (Y, YC-self.bndY, YC+self.bndY)
            else:
                Y = "clamp(%s,%.3g,%.3g)" % (Y, YC-self.bndY, YC+self.bndY)

        Pos = "<pos={%s;f3}px>" % (X)
        Voffset = "<voffset={%s;f3}px>" % (Y)

        Color = "<color=%s>" % (self.color)

        Tailing = "</mspace></size></color></voffset>"

        if self.Rot !=0 :
            Rotate = "<rotate=%s>" % (V2F(self.Rot))
            Tailing = Tailing + "</rotate>"
        else:
            Rotate = ""

        

        return Head+Space+Size+Color+Alpha+Rotate+Pos+Voffset+self.Content + Tailing


def GetArticle(RTObjects):
    Article = "<color=#FFFF00><alpha=#00><size=2px><width=100px><mspace=1px><line-height=-0px><voffset=0px>+"
    for obj in RTObjects:
        Article = Article + "\n" + obj.Parse()
    Article = Article + "\n<alpha=#00><size=2px><line-height=-0px></rotate><voffset=0px>+ "
    return Article


def TestSine():
    xs = np.linspace(-10, 10, 101)
    ys = np.sin(xs/10 * np.pi * 2) * 5
    RTObjs = []
    for i in range(xs.size):
        RTObjs.append(RTObject(
            nX=xs[i], nY="sin(%.3g/10 * 360+Time*360)*5 " % (xs[i]), nContent="-", nbndX=1, nbndY=1))
    return GetArticle(RTObjs)


def HUD():
    def F_MeterPs2Kn(m):
        return "(%s)*1.943845" % (m)

    def F_MeterPs2Kph(m):
        return "(%s)*3.6" % (m)

    def F_Meter2Ft(m):
        return "(%s)/0.3048" % (m)

    def F_Meter2Nm(m):
        return "(%s)/1000*0.54" % (m)

    def F_Meter2Km(m):
        return "(%s)/1000" % (m)

    def LineOfSight():
        L = []
        L.append(RTObject(nX=0, nY=.63, nSpace=.04, nSize=.1,
                 nContent="<size=.2px>-</size>vv<size=.2px>-</size>"))
        return L

    Vt = "rate(TargetHeading/180*pi)*cos(TargetElevation)*TargetDistance"
    Vp = "rate(TargetElevation/180*pi)*TargetDistance"
    Vr = "rate(TargetDistance)"
    V = "sqrt(pow(%s,2)+pow(%s,2)+pow(%s,2))" % (Vt, Vp, Vr)
    Vrg = "(%s)*cos(TargetElevation)-(%s)*sin(TargetElevation)" % (Vr, Vp)
    Vzg = "(%s)*sin(TargetElevation)+(%s)*cos(TargetElevation)" % (Vr, Vp)
    eqtc = "pow(%s,2)" % ("TargetDistance")
    eqtb = "TargetSelected?2*TargetDistance*(%s):0" % (Vr)
    eqta = "pow(%s,2)-800*800" % (V)
    T = "(-(%s)-sqrt(pow((%s),2)-4*(%s)*(%s)))/(2*(%s))" % (eqtb,
                                                            eqtb, eqta, eqtc, eqta)
    Zgnew = "(%s)*(%s)+TargetDistance*sin(TargetElevation)" % (Vzg, T)
    RgNew = "(%s)*(%s)+TargetDistance*cos(TargetElevation)" % (Vrg, T)
    HeadingFix = "atan((%s)*(%s)/(%s))" % (Vt, T, RgNew)
    ElevNew = "atan((%s)/(%s))" % (Zgnew, RgNew)
    HeadingNew = "TargetHeading + %s" % (HeadingFix)

    def dirGlob2Loc(H, R):
        EGx = "sin(%s-Heading)*cos(%s)" % (H, R)
        EGy = "cos(%s-Heading)*cos(%s)" % (H, R)
        EGz = "sin(%s)" % (R)
        EPx = EGx
        EPy = "(%s)*cos(PitchAngle)+(%s)*sin(PitchAngle)" % (EGy, EGz)
        EPz = "-(%s)*sin(PitchAngle)+(%s)*cos(PitchAngle)" % (EGy, EGz)
        ERx = "(%s)*cos(RollAngle)+(%s)*sin(RollAngle)" % (EPx, EPz)
        ERy = EPy
        ERz = "(%s)*cos(RollAngle)-(%s)*sin(RollAngle)" % (EPz, EPx)
        return(
            "(%s>0?1:-1)*acos((%s)/sqrt(pow(%s,2)+pow(%s,2)))" % (ERx, ERy, ERx, ERy),
            "asin(%s)" % (ERz)
        )

    EHTarget = dirGlob2Loc("TargetHeading", "TargetElevation")
    EHTargetLead = dirGlob2Loc(HeadingNew, ElevNew)

    # print(EHTargetLead[0])
    # print(EHTargetLead[1])

    def ElevLines():
        L = []
        Angles = np.linspace(-5*2, 5*2, 5)
        FiveDegreePx = 0.14  # pix per degree, for 5 degree accurate ad 0.6m
        LineBnd = 1.25
        Lsiz = .15
        Lzoom = 1.3

        # print(Angles)
        for i in range(Angles.size):
            PAngle = "{round(PitchAngle/5)*5+%d;00}" % (Angles[i])
            Yplace = "(repeat(-PitchAngle+2.5,5)-2.5)*%.3g + %.3g + %.3g" % (
                FiveDegreePx, Angles[i]*FiveDegreePx, YC + 0.005)
            # print(Yplace)

            L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=-0.12 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
            L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=0.12 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
            L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=-0.19 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
            L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=0.19 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
            L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=-0.26 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
            L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=0.26 * Lzoom,
                              nY=Yplace,
                              nSpace=.05, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
            L.append(RTObject(nR="RollAngle", nRot=0, nX=-0.38 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent=PAngle+" " % (Angles[i])))
            L.append(RTObject(nR="RollAngle", nRot=0, nX=0.38 * Lzoom,
                              nY=Yplace,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent=" "+PAngle % (Angles[i])))

        Yplace = "-PitchAngle * %.3g + %.3g " % (FiveDegreePx, YC + 0.005)
        L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=-0.5 * Lzoom,
                          nY=Yplace,
                          nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))
        L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=0.5 * Lzoom,
                          nY=Yplace,
                          nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=LineBnd, nbndY=LineBnd, nContent="─"))

        L.append(RTObject(nR="RollAngle", nRot="-RollAngle", nX=0 + XC,
                          nY=1.25 + YC,
                          nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=0, nbndY=0, nContent="Δ"))
        L.append(RTObject(nR="RollAngle-90", nRot="-RollAngle+90", nX=0 + XC,
                          nY=1.25 + YC,
                          nSpace=.05 * Lzoom, nSize=Lsiz*.5, nbndX=0, nbndY=0, nContent="Δ"))
        L.append(RTObject(nR="RollAngle+90", nRot="-RollAngle-90", nX=0 + XC,
                          nY=1.25 + YC,
                          nSpace=.05 * Lzoom, nSize=Lsiz*.5, nbndX=0, nbndY=0, nContent="Δ"))
        RollInds = np.linspace(-90, 90, 13)
        for angle in RollInds:
            L.append(RTObject(nR=angle, nRot=-angle, nX=0 + XC,
                              nY=1.35 + YC,
                              nSpace=.05 * Lzoom, nSize=Lsiz, nbndX=0, nbndY=0, nContent="|"))
        L.append(RTObject(nR=0, nRot=0, nX=0 + XC,
                          nY=1.50 + YC,
                          nSpace=.08, nSize=0.14, nbndX=0, nbndY=0,
                          nContent="<u>{abs(RollAngle);000}{ abs(RollAngle)<1?\"M\":(RollAngle>0?\"R\":\"L\")}</u>"))

        # Velo Vector
        L.append(RTObject(nX="AngleOfSlip*%.3g+%.3g" % (FiveDegreePx, XC), nY="AngleOfAttack*%.3g+%.3g" % (FiveDegreePx, YC), nSize=Lsiz,
                          nSpace=Lsiz*0.4, nContent="-o-", nbndX=1, nbndY=1))
        L.append(RTObject(nX="AngleOfSlip*%.3g+%.3g" % (FiveDegreePx, XC), nY="AngleOfAttack*%.3g+%.3g+(IAS<80?0:(IAS>140?0.01:0.02))" % (FiveDegreePx, YC+0.03), nSize=Lsiz,
                          nSpace=Lsiz*0.4, nContent="-", nRot=90, nbndX=1, nbndY=1))

        # Target Vector
        # L.append(RTObject(nX="TargetSelected?(%s)*%s+%s:0" % (EHTarget[0], FiveDegreePx, XC), nY="TargetSelected?(%s)*%s+%s:0" % (
        #     EHTarget[1], FiveDegreePx, YC), nSize=Lsiz*2, ncolor="{TargetLocked?\"#FF0000\":\"#FFFF00\"}",
        #     nalpha="#BF", nbndX=2, nbndY=2, nSpace=.05*Lzoom, nContent="{TargetSelected?\"Θ\":\"\"}"))
        TGTY = "TargetSelected?(%s)*%.3g+%.3g:0" % (
            "TGT_ELVR", FiveDegreePx, YC)
        TGTX = "TargetSelected?(%s)*%.3g+%.3g:0" % ("TGT_HDGR",
                                                    FiveDegreePx, XC)
        L.append(RTObject(nX="clamp(%s,%.4f,%.4f)" % (TGTX, -1.5+XC, 1.5+XC), nY="clamp(%s,%.4f,%.4f)" % (TGTY, -1+YC, 1+YC), nSize=Lsiz*2, ncolor="{TargetLocked?\"#FF0000\":\"#FFFF00\"}",
                          nalpha="{(abs((%s)-%.4f)<1.5) & (abs((%s)-%.4f)<1) & (repeat(Time*4,1)>0.5)?\"#BF\":\"#6F\"}" % (TGTX, XC, TGTY, YC), nSpace=.05*Lzoom, nContent="{TargetSelected ?\"Θ\":\"\"}"))

        return L

    def SpeedMeter():
        L = []
        speedOffs = np.linspace(-50, 50, 11)
        # sValue = "UnitMetric!=0?(%s):(%s)" % (
        #     F_MeterPs2Kph("TAS"), F_MeterPs2Kn("TAS"))
        sValue = "TASKnot"

        x0 = XC - 1.5
        y0 = YC + 0.0
        vgap = 0.15
        vsiz = 0.15
        vspc = 0.08

        for dspeed in speedOffs:
            vmetre = "(%s)+%d" % (sValue, dspeed)
            content = "{repeat(round((%s)/10),2)=0 ?\"\":\"<alpha=#00>\"}{round((%s)/10) * 10;000}" % (
                vmetre, vmetre)
            Yplc = "%.3g + (repeat(-(%s)+5,10)-5 + %.3g)*%.3g" % (y0,
                                                            sValue, dspeed, vgap/10)
            L.append(RTObject(nX=x0-0.18, nY=Yplc, nSpace=vspc,
                     nSize=vsiz, nContent=content))
            L.append(RTObject(nX=x0, nY=Yplc, nSpace=vspc,
                     nSize=vsiz, nContent="┤"))
        L.append(RTObject(nX=x0+0.1, nY=y0-0.01, nSize=vsiz *
                 1.2, nSpace=vspc, nRot=90, nContent="Δ"))
        L.append(RTObject(nX=x0, nY=y0+5.8*vgap,
                 nSize=vsiz, nSpace=vspc, nContent="┐"))
        L.append(RTObject(nX=x0, nY=y0-5.8*vgap,
                 nSize=vsiz, nSpace=vspc, nContent="┘"))
        L.append(RTObject(nX=x0, nY=y0 + 7*vgap, nSize=vsiz, nSpace=vspc,
                          ncolor="{(IAS>80&TAS<1020)|AltitudeAgl<4.00731?\"#00FF00\":(repeat(Time*3,1)>0.5?\"#00FF00\":\"#FF0000\")}",
                          nContent="<u>{%s;0000}</u>" % (sValue)))
        L.append(RTObject(nX=x0, nY=y0 + 7*vgap + vsiz*1.1, nSize=vsiz*0.6, nSpace=vspc * 0.6,
                          ncolor="{(IAS>80&TAS<1020)|AltitudeAgl<4.00731?\"#00FF00\":(repeat(Time*3,1)>0.5?\"#00FF00\":\"#FF0000\")}",
                          nContent="IAS <u>{%s;0000}</u>" % ("IASKnot")))
        L.append(RTObject(nX=x0+0.1, nY=y0 - 2.5*vgap, nSize=vsiz*1.7, nSpace=vspc*1.1,
                          nContent="{abs(rate(%s))<0.5?\"~\":(rate(%s)>0?\"↑\":\"↓\")}" % (sValue, sValue)))
        return L

    def HdgMeter():
        L = []
        speedOffs = np.linspace(-50, 50, 11)
        # sValue = "UnitMetric!=0?(%s):(%s)" % (
        #     F_MeterPs2Kph("TAS"), F_MeterPs2Kn("TAS"))
        sValue = "Heading"

        x0 = XC + 0
        y0 = YC + 1.9
        vgap = 0.075
        vsiz = 0.15
        vspc = 0.08

        for dspeed in speedOffs:
            # vmetre = "((%s)+%d)<0?((%s)+%d)+360:((%s)+%d)" % (sValue,
            #                                                   dspeed, sValue, dspeed, sValue, dspeed)
            vmetre = "(%s)+%d" % (sValue,
                                  dspeed)
            content = "{repeat(round((%s)/10),2)=0 ?\"\":\"<alpha=#00>\"}{round((%s)/10)<0?round((%s)/10)*10+360: round((%s)/10)*10;000}" % (
                vmetre, vmetre, vmetre, vmetre)
            Xplc = "%s + (repeat(-(%s)+5,10)-5 + %s)*%s" % (x0,
                                                            sValue, dspeed, vgap/10)
            L.append(RTObject(nX=Xplc, nY=y0+0.15, nSpace=vspc*.5,
                     nSize=vsiz*.5, nContent=content))
            L.append(RTObject(nX=Xplc, nY=y0, nSpace=vspc,
                     nSize=vsiz, nContent="┴"))
        L.append(RTObject(nX=x0, nY=y0-0.07, nSize=vsiz *
                 1.2, nSpace=vspc, nRot=00, nContent="Δ"))
        L.append(RTObject(nX=x0+5.8*vgap, nY=y0,
                 nSize=vsiz, nSpace=vspc, nContent="┘"))
        L.append(RTObject(nX=x0-5.8*vgap, nY=y0,
                 nSize=vsiz, nSpace=vspc, nContent="└"))
        L.append(RTObject(nX=x0, nY=y0-0.17, nSize=vsiz *
                 1.0, nSpace=vspc, nRot=00, nContent="<u>{Heading<0?Heading+360:Heading;000}</u>"))

        return L

    def AltMeter():
        L = []
        altOffs = np.linspace(-500, 500, 11)
        # sValue = "UnitMetric!=0?(%s):(%s)" % (
        #     F_MeterPs2Kph("TAS"), F_MeterPs2Kn("TAS"))
        sValue = "AltFeet"

        x0 = XC + 1.5
        y0 = YC + 0.0
        vgap = 0.15
        vsiz = 0.15
        vspc = 0.08

        for dalt in altOffs:
            vmetre = "(%s)+%d" % (sValue, dalt)
            content = "{repeat(round((%s)/100),2)=0 ?\"\" :\"<alpha=#00>\"}{round((%s)/100)>=0 ?\"\":\"-\"}{floor( (round(abs(%s)/100)/10));00}<size=%.3gpx>{repeat(round(abs(%s)/100)*100,1000);000}</size>" % (
                vmetre, vmetre, vmetre, vsiz*0.7, vmetre)
            Yplc = "%s + (repeat(-(%s)+50,100)-50 + %s)*%s" % (y0,
                                                               sValue, dalt, vgap/100)
            L.append(RTObject(nX=x0+0.22, nY=Yplc, nSpace=vspc,
                     nSize=vsiz, nContent=content))
            L.append(RTObject(nX=x0, nY=Yplc, nSpace=vspc,
                     nSize=vsiz, nContent="├"))
        L.append(RTObject(nX=x0-0.1, nY=y0-0.01, nSize=vsiz *
                 1.2, nSpace=vspc, nRot=-90, nContent="Δ"))
        L.append(RTObject(nX=x0, nY=y0+5.8*vgap,
                 nSize=vsiz, nSpace=vspc, nContent="┌"))
        L.append(RTObject(nX=x0, nY=y0-5.8*vgap,
                 nSize=vsiz, nSpace=vspc, nContent="└"))

        L.append(RTObject(nX=x0, nY=y0 + 7*vgap, nSize=vsiz, nSpace=vspc,
                          nContent="<u>{floor((%s)/1000);00}<size=%.3gpx>{repeat(%s,1000);000}</size></u>" % (sValue, vsiz*0.7, sValue)))
        L.append(RTObject(nX=x0, nY=y0 + 7*vgap + vsiz*1.1, nSize=vsiz*0.6, nSpace=vspc * 0.6,
                          nContent="AGL <u>{floor((%s)/1000);00}<size=%.3gpx>{repeat(%s,1000);000}</size></u>" % ("AltAGLFeet", vsiz*0.7*0.6, "AltAGLFeet")))
        L.append(RTObject(nX=x0+0.15, nY=y0 - 7.1*vgap, nSize=vsiz*0.8, nSpace=vspc*0.8,
                          nContent="{abs(rate(%s))<2?\"~\":(rate(%s)>0?\"↑\":\"↓\")}{abs(rate(%s))*60;000000}" % (sValue, sValue, sValue)))

        return L

    def InfoPad():
        L = []

        lineH = 0.10
        spc = 0.055
        siz = 0.11
        x0 = XC-2.2
        y0 = YC-0.6

        L.append(RTObject(nX=x0, nY=y0-0*lineH,
                          nSize=siz, nSpace=spc, nContent="G"))
        L.append(RTObject(nX=x0, nY=y0-1*lineH,
                          nSize=siz, nSpace=spc, nContent="α"))
        L.append(RTObject(nX=x0, nY=y0-2*lineH,
                          nSize=siz, nSpace=spc, nContent="M"))
        L.append(RTObject(nX=x0+2*spc, nY=y0-3*lineH,
                          nSize=siz, nSpace=spc, nContent="{Activate1?\"VTOL\":\"    \"} {Activate4?\"VEC\":\"    \"}"))
        L.append(RTObject(nX=x0+1.5*spc, nY=y0-4*lineH,
                          nSize=siz, nSpace=spc, nContent="{LandingGear?\"   \":\"L F\"} {Activate5?\"ABN\":\"\"}"))
        L.append(RTObject(nX=x0+6.5*spc, nY=y0-5*lineH,
                          nSize=siz, nSpace=spc*1.5, nContent="Ammo {SelectedWeapon} {ammo(SelectedWeapon)}"))

        L.append(RTObject(nX=x0+4*spc, nY=y0-0*lineH,
                          nSize=siz, nSpace=spc, nContent="{VerticalG;0.0}"))
        L.append(RTObject(nX=x0+4*spc, nY=y0-1*lineH,
                          nSize=siz, nSpace=spc, nContent="{-AngleOfAttack;0.0}"))
        L.append(RTObject(nX=x0+4*spc, nY=y0-2*lineH,
                          nSize=siz, nSpace=spc, nContent="{TAS/(340-clamp((Altitude*0.003937),0,43));#0.00}"))

        return L

    def Warnings():
        L = []
        lineH = 0.1
        spc = 0.1
        siz = 0.1
        x0 = XC
        y0 = YC

        L.append(RTObject(nX=x0, nY=y0+0*lineH, nSpace=spc, nSize=siz,
                 ncolor="#FF0000", nalpha="{sin(3*360*Time)>0?\"#00\":\"#FF\"}", nContent="{(IAS<80 | abs(AngleOfAttack) >45) & AltitudeAgl>4 & (! Activate1) ? \"STALL\" : ""} {GForce>9 ? \"HIGH G\" : \"\"}"))

        L.append(RTObject(nX=x0, nY=y0+1*lineH, nSpace=spc, nSize=siz,
                 ncolor="{sin(3*360*Time)>0? \"#FF4000FF\" : \"#00FF00FF\"}", nContent="{TargetLocked?\"LOCKED\" : (TargetLocking?\"LOCKING\":\"\")}"))
        L.append(RTObject(nX=x0, nY=y0+2*lineH, nSpace=spc, nSize=siz,
                 ncolor="{sin(3*360*Time)>0&!CanAutoPilot? \"#FF4000FF\" : \"#00FF00FF\"}", nContent="{HoldAlt|HoldSpd|HoldHdg?(CanAutoPilot?\"Auto Pilot\":\"Approach Lvl to Auto Pilot\"):\"\"}"))

        return L

    L = LineOfSight()
    L.extend(ElevLines())
    L.extend(SpeedMeter())
    L.extend(AltMeter())
    L.extend(HdgMeter())
    L.extend(InfoPad())
    L.extend(Warnings())

    return GetArticle(L)


def Camo1():

    def dec2alp(dec):
        return "#" + hex(round(dec))[2:]

    # def shape(x, y) -> bool:
    #     return y < 0.8*x+20 and y > -0.5*x-20
    def shape(x, y) -> bool:
        return y < 0.8*x+8 and y > -0.5*x-8 and x < 8
    # def shape(x, y) -> bool:
    #         return np.abs(x) < 5 and np.abs(y) < 10
    R = -1

    L = []
    Lim = 2
    Nx = 15
    Lx = 15
    Ny = 10
    Ly = 20
    A0 = 100
    AR = 200-A0
    s0 = 2
    sR = 2

    xe = np.linspace(-Lx, Lx, Nx)
    ye = np.linspace(-Ly, Ly, Ny)
    xs, ys = np.meshgrid(xe, ye, indexing='ij')

    random.seed(1231)
    xs += (random.random_sample((Nx, Ny)) * 2 - 1) * Lim
    ys += (random.random_sample((Nx, Ny)) * 2 - 1) * Lim
    siz = random.random_sample((Nx, Ny)) * sR + s0
    alp = random.random_sample((Nx, Ny)) * AR + A0

    xs = np.reshape(xs, -1)
    ys = np.reshape(ys, -1)
    siz = np.reshape(siz, -1)
    alp = np.reshape(alp, -1)

    # "▒█"
    for i in range(xs.size):
        if(shape(xs[i], ys[i])):
            L.append(RTObject(nX=R*xs[i], nY=ys[i], nSpace=siz[i],
                              nSize=siz[i], ncolor="#101010", nalpha=dec2alp(alp[i]), nContent="█"))

    return GetArticle(L)


def TacMap():
    def F_Meter2Nm(m):
        return "(%s)/1000*0.54" % (m)

    FrameSiz = 0.15

    def Frame():
        L = []

        L.append(RTObject(nSize=0.1, nX=0+XC, nY=0+YC, nContent='Δ'))

        L.append(RTObject(nSize=FrameSiz, nSpace=FrameSiz*0.5,
                          nContent="┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐", nY=12/2*FrameSiz+YC, nX=XC))
        for i in range(11):
            L.append(RTObject(nSize=FrameSiz, nSpace=FrameSiz*0.5,
                              nContent="├<space={11.5*(%.3g)}px>┤" % (FrameSiz), nY=(12/2-1-i)*FrameSiz+YC, nX=XC))

        L.append(RTObject(nSize=FrameSiz, nSpace=FrameSiz*0.5,
                          nContent="└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘", nY=(12/2-1-11)*FrameSiz+YC, nX=XC))

        for Rot in [180, 135, 90, 45, 0, -90]:
            Rline = "───┤───┤───┤───┤───┤───┤"
            for i in range(len(Rline)):
                L.append(RTObject(nSize=FrameSiz*0.5, nSpace=FrameSiz*0.5*0.5, nX=0*FrameSiz + i * FrameSiz * 0.5*0.5 +
                                  XC, nY=YC, nContent=Rline[i], nR=-Rot, nRot=Rot))

        return L

    def TGT():
        L = []
        TGTR = "clamp((%s)*Zoom,0,5)" % (F_Meter2Nm("TargetDistance"))
        TGTT = "TargetHeading - Heading"

        dispX = "sin(%s)*(%s)*%.3g+%.3g" % (TGTT,
                                            TGTR, FrameSiz, XC+FrameSiz*0.8*0.75)
        dispY = "cos(%s)*(%s)*%.3g+%.3g" % (TGTT,
                                            TGTR, FrameSiz, YC-0.8*FrameSiz*0.5)

        L.append(RTObject(nSize=FrameSiz*0.8, nSpace=FrameSiz*0.8*0.5,
                          nX=dispX, nY=dispY,
                          ncolor="#FF0000", nalpha="{TargetSelected?((%s)*Zoom>=6?\"#4F\":\"#FF\"):\"#00\"}" % (F_Meter2Nm("TargetDistance")),
                          nContent="^TGT"))

        return L

    def LL2RT(Lat, Lon):
        R = "sqrt(pow((%s)-Latitude,2)+pow((%s)-Longitude,2))" % (Lat, Lon)
        return (R, "sign((%s)-Longitude) * acos(((%s)-Latitude)/(%s)) - Heading " % (Lon, Lat, R))

    def POI():
        L = []

        NameDat = {}
        NameDat["YGR"] = ["Yeager", 53186, 26393]
        NameDat["BDT"] = ["Bandit", 59149, 14605]
        NameDat["WRT"] = ["Wright", -5522, 6019]
        NameDat["AVL"] = ["Avalanche", 141011, 5582]
        NameDat["MWR"] = ["Maywar", -32116, 76747]
        NameDat["SPK"] = ["Skypark", -30768, -625]

        for k in NameDat:
            D, T = LL2RT(NameDat[k][1], NameDat[k][2])

            R = "clamp((%s)*Zoom,0,5)" % (F_Meter2Nm(D))
            dispX = "sin(%s)*(%s)*%.3g+%.3g" % (T,
                                                R, FrameSiz, XC+FrameSiz*0.8*0.75)
            dispY = "cos(%s)*(%s)*%.3g+%.3g" % (T,
                                                R, FrameSiz, YC-0.8*FrameSiz*0.5)

            L.append(RTObject(nSize=FrameSiz*0.8, nSpace=FrameSiz*0.8*0.5,
                              nX=dispX, nY=dispY,
                              ncolor="#004FFF", nalpha="{(%s)*Zoom>=6?\"#3F\":\"#BF\"}" % (F_Meter2Nm(D)),
                              nContent="^"+k))

        return L

    def WPT():
        L = []

        D, T = LL2RT("NavLat", "NavLon")

        R = "clamp((%s)*Zoom,0,5)" % (F_Meter2Nm(D))
        dispX = "sin(%s)*(%s)*%.3g+%.3g" % (T,
                                            R, FrameSiz, XC-FrameSiz*0.8*0.75)
        dispY = "cos(%s)*(%s)*%.3g+%.3g" % (T,
                                            R, FrameSiz, YC-0.8*FrameSiz*0.5)

        L.append(RTObject(nSize=FrameSiz*0.8, nSpace=FrameSiz*0.8*0.5,
                          nX=dispX, nY=dispY,
                          ncolor="#00FF4F", nalpha="{NAV>0?((%s)*Zoom>=6?\"#4F\":\"#FF\"):\"#00\"}" % (F_Meter2Nm(D)),
                          nContent="WPT^"))

        return L

    def NAVLine():
        L = []
        D, T = LL2RT("NavLat", "NavLon")
        R = "clamp((%s)*Zoom,0,6)" % (F_Meter2Nm(D))
        L.append(RTObject(nSize=FrameSiz*0.8, nSpace=FrameSiz*0.8*0.5,
                          nX=+XC, nY=(-12/2-0.8)*FrameSiz + YC,
                          nContent="WPT {NAV>0?\"\":\"NONE<alpha=#00>\"} DIST: {%s;0.0} NM TURN: {abs(%s)>180?(%s)-sign(%s)*360:(%s);00}" % (F_Meter2Nm(D), T, T, T, T)))
        L.append(RTObject(nSize=FrameSiz*0.8, nSpace=FrameSiz*0.8*0.5,
                          nX=+XC, nY=(-12/2+0.8)*FrameSiz + YC,
                          nContent="{NAV>0?\"\":\"<alpha=#00>\"}LAT {NavLat;000000}- LON {NavLon;000000}"))

        L.append(RTObject(nSize=FrameSiz*0.8, nSpace=FrameSiz*0.8*0.5,
                          nX=+XC, nY=(+12/2+0.8)*FrameSiz + YC,
                          nContent="TGT {TargetSelected?\"\":\"NONE<alpha=#00>\"} DIST: {%s;0.0} NM TURN: {abs(%s)>180?(%s)-sign(%s)*360:(%s);00}" % (F_Meter2Nm("TargetDistance"), "TargetHeading-Heading", "TargetHeading-Heading", "TargetHeading-Heading", "TargetHeading-Heading")))

        return L

    def Number():
        L = []
        L.append(RTObject(nSize=FrameSiz*0.5, nSpace=FrameSiz*0.5*0.5, nX=1 * FrameSiz + XC, nY=-.5 * FrameSiz + YC,
                          nContent="{1/Zoom;0.0}"))
        L.append(RTObject(nSize=FrameSiz*0.5, nSpace=FrameSiz*0.5*0.5, nX=3 * FrameSiz + XC, nY=-.5 * FrameSiz + YC,
                          nContent="{3/Zoom;0.0}"))
        L.append(RTObject(nSize=FrameSiz*0.5, nSpace=FrameSiz*0.5*0.5, nX=5 * FrameSiz + XC, nY=-.5 * FrameSiz + YC,
                          nContent="{5/Zoom;0.0}"))

        return L

    L = Frame()
    L.extend(TGT())
    L.extend(POI())
    L.extend(WPT())
    L.extend(NAVLine())
    L.extend(Number())

    return GetArticle(L)


def Plane():
    Flash = "repeat(Time*3,1)>0.5"
    FrameSiz = 0.15

    def Frame():
        L = []
        L.append(RTObject(nX=XC-3*FrameSiz, nY=YC-0.3*FrameSiz,
                 nSize=FrameSiz*2, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nSpace=FrameSiz/2, nContent="<"))
        L.append(RTObject(nX=XC-(3-0.5)*FrameSiz, nY=YC-0.4*FrameSiz, nSize=FrameSiz *
                 2.5, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nSpace=FrameSiz/2, nContent="="))
        L.append(RTObject(nX=XC-(3-1)*FrameSiz, nY=YC-0.6*FrameSiz, nSize=FrameSiz *
                 1, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nSpace=FrameSiz/2, nContent="\\"))
        L.append(RTObject(nX=XC-(3-1)*FrameSiz, nY=YC+0.6*FrameSiz, nSize=FrameSiz *
                 1, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nSpace=FrameSiz/2, nContent="/"))
        L.append(RTObject(nX=XC-(3-1.6)*FrameSiz, nY=YC-1.0*FrameSiz, nSize=FrameSiz *
                 1.5, nSpace=FrameSiz/2, nContent="--"))
        L.append(RTObject(nX=XC-(3-1.6)*FrameSiz, nY=YC+(1.0-0.25)*FrameSiz, nSize=FrameSiz *
                 1.5, nSpace=FrameSiz/2, nContent="--"))
        L.append(RTObject(nX=XC-(3-2.4)*FrameSiz, nY=YC+(-1.7)*FrameSiz, nSize=FrameSiz *
                 2, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nalpha="{%s&(!LandingGear)?\"#4F\":\"#FF\"}" % (Flash),
                          nSpace=FrameSiz/1, nContent="\\"))
        L.append(RTObject(nX=XC-(3-2.4)*FrameSiz, nY=YC+(1.7-0.5)*FrameSiz, nSize=FrameSiz *
                 2, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nalpha="{%s&(!LandingGear)?\"#4F\":\"#FF\"}" % (Flash),
                  nSpace=FrameSiz/1, nContent="/"))
        L.append(RTObject(nX=XC-(3-3.2)*FrameSiz, nY=YC-1.7*FrameSiz, nSize=FrameSiz *
                 2, nalpha="{%s&(abs(Roll)>0.8|!LandingGear)?\"#4F\":\"#FF\"}" % (Flash), 
                 nSpace=FrameSiz/2, nContent="/"))
        L.append(RTObject(nX=XC-(3-3.2)*FrameSiz, nY=YC+(1.7-0.5)*FrameSiz, nSize=FrameSiz *
                 2, nalpha="{%s&(abs(Roll)>0.8|!LandingGear)?\"#4F\":\"#FF\"}" % (Flash), 
                 nSpace=FrameSiz/2, nContent="\\"))

        L.append(RTObject(nX=XC-(3-1.6)*FrameSiz, nY=YC+(1.2)*FrameSiz, nSize=FrameSiz *
                 0.8, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nalpha="{%s&(abs(Roll)>0.8|abs(Pitch)>0.8)?\"#4F\":\"#FF\"}" % (Flash),
                 nSpace=FrameSiz/2, nContent="Δ", nRot=0))
        L.append(RTObject(nX=XC-(3-1.6)*FrameSiz, nY=YC-(1.1)*FrameSiz, nSize=FrameSiz *
                 0.8, ncolor="{TAS>900?\"#FFFF00\":\"#00FF00\"}", nalpha="{%s&(abs(Roll)>0.8|abs(Pitch)>0.8)?\"#4F\":\"#FF\"}" % (Flash),
                 nSpace=FrameSiz/2, nContent="Δ", nRot=180))

        L.append(RTObject(nX=XC-(3-3.4)*FrameSiz, nY=YC-0.7*FrameSiz, nSize=FrameSiz *
                 3.5,ncolor="{Activate5&Throttle>0.8?\"#FFFF00\":\"#00FF00\"}", nSpace=FrameSiz/2, nContent="="))

        L.append(RTObject(nX=XC-(3-4.2)*FrameSiz, nY=YC-0.4*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{Activate1?\"O\":\"•\"}"))
        L.append(RTObject(nX=XC-(3-4.2)*FrameSiz, nY=YC+0.4*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{Activate1?\"O\":\"•\"}"))
        L.append(RTObject(nX=XC-(3-1.2)*FrameSiz, nY=YC+0.*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{Activate1?\"O\":\"•\"}"))
        L.append(RTObject(nX=XC-(3-1.6)*FrameSiz, nY=YC+0.*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{Activate1?\"O\":\"•\"}"))


        L.append(RTObject(nX=XC-(3-2.8)*FrameSiz, nY=YC+0.8*FrameSiz+0.1*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{!LandingGear?\"«\":\"•\"}"))
        L.append(RTObject(nX=XC-(3-2.8)*FrameSiz, nY=YC-0.8*FrameSiz+0.1*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{!LandingGear?\"«\":\"•\"}"))
        L.append(RTObject(nX=XC-(3-0.8)*FrameSiz, nY=YC-0.0*FrameSiz+0.1*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{!LandingGear?\"«\":\"•\"}"))

        L.append(RTObject(nX=XC-(3-2.3)*FrameSiz, nY=YC+0.4*FrameSiz, nSize=FrameSiz *
                          1, nSpace=FrameSiz/2, nContent="{Activate2?\"¤¤\":\"•-\"}"))
        L.append(RTObject(nX=XC-(3-2.3)*FrameSiz, nY=YC-0.4*FrameSiz, nSize=FrameSiz *
                 1, nSpace=FrameSiz/2, nContent="{Activate2?\"¤¤\":\"•-\"}"))

        L.append(RTObject(nX=XC-(3-4.4)*FrameSiz, nY=YC-0.4*FrameSiz + 0.05*FrameSiz, nSize=FrameSiz *
                 1, nalpha="{%s&(abs(Roll)>0.8|abs(Pitch)>0.8)&Activate4?\"#4F\":\"#FF\"}" % (Flash), nSpace=FrameSiz/2, nContent="{Activate4?\"<\":\"-\"}"))
        L.append(RTObject(nX=XC-(3-4.4)*FrameSiz, nY=YC+0.4*FrameSiz + 0.05*FrameSiz, nSize=FrameSiz *
                 1, nalpha="{%s&(abs(Roll)>0.8|abs(Pitch)>0.8)&Activate4?\"#4F\":\"#FF\"}" % (Flash), nSpace=FrameSiz/2, nContent="{Activate4?\"<\":\"-\"}"))

        return L

    L = Frame()

    return GetArticle(L)

def SubsDoubles(txt):
    return re.sub(r"(?<!#)(?<!;)(\d*\.\d+)", lambda match:"%.3g"%(round(float(match.group(1)),3)), txt)
    

if __name__ == "__main__":
    # print(TacMap())
    print((HUD()))
    # print(Plane())
