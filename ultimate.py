#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:29:16 2017

@author: Ivan_Antonov
"""

import numpy as np
import matplotlib.pyplot as plt

class properties:
    """ This class is for all the functions of cmb, fppy & loops"""
    def __init__(self,p=None,s=None,v=None,o=None,g=None,phys=None,spin=None,sys=None,M=None,Fe=None,T=None):
        """initiating variables"""
        self.p=p
        self.s=s
        self.v=v
        self.o=o
        self.g=g
        self.phys=phys
        self.spin=spin
        self.sys=sys
        self.M=M
        self.Fe=Fe
        self.T=T
        
    def graph (self,p,s,g):
        #open the file (change just the name for each one)(pyrolite, hartzburgite, basalt)
        myFile = open(s, 'r')

        #read the file. splitlines = split by row into an array
        cutText = myFile.read().splitlines() #split line into rows
        cutText.pop(0) #delete first entry


        #lists for storing data
        t=[]
        d=[]
        vs=[]
        vp=[]

        #we go through the text line be line (row). We split each row into individual entries (columns)
        for i in cutText: #make into columns 
            t.append(float(i.split()[2]))
            d.append(float(i.split()[3]))
            vs.append(float(i.split()[5]))
            vp.append(float(i.split()[6]))
        
        
        t0=np.array(t[p::1401])
        d0=np.array(d[p::1401])
        vs0=np.array(vs[p::1401])
        vp0=np.array(vp[p::1401])
        
        a1=np.polyfit(t0,d0,2)
        d1=a1[0]*t0**2+a1[1]*t0+a1[2]
        
        a2 =np.polyfit(t0,d0,5)
        d2= a2[0]*t0**5+a2[1]*t0**4+a2[2]*t0**3+a2[3]*t0**2+a2[4]*t0+a2[5]
        
        a3=np.polyfit(t0,d0,7)
        d3=a3[0]*t0**7+a3[1]*t0**6+a3[2]*t0**5+a3[3]*t0**4+a3[4]*t0**3+a3[5]*t0**2+a3[6]*t0+a3[7]
        
        
        b1=np.polyfit(t0,vs0,2)
        vs1=b1[0]*t0**2+b1[1]*t0+b1[2]

        b2 =np.polyfit(t0,vs0,5)
        vs2= b2[0]*t0**5+b2[1]*t0**4+b2[2]*t0**3+b2[3]*t0**2+b2[4]*t0+b2[5]

        b3=np.polyfit(t0,vs0,7)
        vs3=b3[0]*t0**7+b3[1]*t0**6+b3[2]*t0**5+b3[3]*t0**4+b3[4]*t0**3+b3[5]*t0**2+b3[6]*t0+b3[7]
        
        c1=np.polyfit(t0,vp0,2)
        vp1=c1[0]*t0**2+c1[1]*t0+c1[2]

        c2 =np.polyfit(t0,vp0,5)
        vp2= c2[0]*t0**5+c2[1]*t0**4+c2[2]*t0**3+c2[3]*t0**2+c2[4]*t0+c2[5]

        c3=np.polyfit(t0,vp0,7)
        vp3=c3[0]*t0**7+c3[1]*t0**6+c3[2]*t0**5+c3[3]*t0**4+c3[4]*t0**3+c3[5]*t0**2+c3[6]*t0+c3[7]

        
        if g in ['D','d','density']:
            plt.figure()
            plt.plot(t0,d0,'.r')
            plt.plot(t0,d1,'-b')
            plt.plot(t0,d2,'-g')
            plt.plot(t0,d3,'-y')
            plt.legend(['Raw data','Order 2','Order 5','Order 7'])
            plt.title('Density (P='+str(p/10)+'GPa)')
            plt.xlabel('Temperature(K)')
            plt.ylabel('Density (g/cm^3)')#check
            plt.show()
        
        elif g in ['Vs','vs']:
            plt.figure()
            plt.plot(t0,vs0,'.r')
            plt.plot(t0,vs1,'-b')
            plt.plot(t0,vs2,'-g')
            plt.plot(t0,vs3,'-y')
            plt.legend(['Raw data','Order 2','Order 5','Order 7'])
            plt.title('Vs (P='+str(p/10)+'GPa)')
            plt.xlabel('Temperature(K)')
            plt.ylabel('Vs (km/s)')
            plt.show()
            
        elif g in ['Vp','vp']:
            plt.figure()
            plt.plot(t0,vp0,'.r')
            plt.plot(t0,vp1,'-b')
            plt.plot(t0,vp2,'-g')
            plt.plot(t0,vp3,'-y')
            plt.legend(['Raw data','Order 2','Order 5','Order 7'])
            plt.title('Vp (P='+str(p/10)+'GPa)')
            plt.xlabel('Temperature(K)')
            plt.ylabel('Vp (km/s)')
            plt.show()
            
        elif g in ['All','A','a']:
            plt.figure()
            plt.plot(t0,d0,'.r')
            plt.plot(t0,d1,'-b')
            plt.plot(t0,d2,'-g')
            plt.plot(t0,d3,'-y')
            plt.legend(['Raw data','Order 2','Order 5','Order 7'])
            plt.title('Density (P='+str(p/10)+'GPa)')
            plt.xlabel('Temperature(K)')
            plt.ylabel('Density (g/cm^3)')#check
            plt.show()
            
            plt.figure()
            plt.plot(t0,vs0,'.r')
            plt.plot(t0,vs1,'-b')
            plt.plot(t0,vs2,'-g')
            plt.plot(t0,vs3,'-y')
            plt.legend(['Raw data','Order 2','Order 5','Order 7'])
            plt.title('Vs (P='+str(p/10)+'GPa)')
            plt.xlabel('Temperature(K)')
            plt.ylabel('Vs (km/s)')
            plt.show()

            plt.figure()
            plt.plot(t0,vp0,'.r')
            plt.plot(t0,vp1,'-b')
            plt.plot(t0,vp2,'-g')
            plt.plot(t0,vp3,'-y')
            plt.legend(['Raw data','Order 2','Order 5','Order 7'])
            plt.title('Vp (P='+str(p/10)+'GPa)')
            plt.xlabel('Temperature(K)')
            plt.ylabel('Vp (km/s)')
            plt.show()
            
    def matrix(self,p,s,v,o):
        #open the file (change just the name for each one)(pyrolite, hartzburgite, basalt)
        myFile = open(s, 'r')

        #read the file. splitlines = split by row into an array
        cutText = myFile.read().splitlines() #split line into rows
        cutText.pop(0) #delete first entry


        #lists for storing data
        t=[]
        d=[]
        vs=[]
        vp=[]

        #we go through the text line be line (row). We split each row into individual entries (columns)
        for i in cutText: #make into columns 
            t.append(float(i.split()[2]))
            d.append(float(i.split()[3]))
            vs.append(float(i.split()[5]))
            vp.append(float(i.split()[6]))
        
        t0=np.array(t[p::1401])
        d0=np.array(d[p::1401])
        vs0=np.array(vs[p::1401])
        vp0=np.array(vp[p::1401])
        
        if o in ['2']:
            
            a1=np.polyfit(t0,d0,2)
            d1=a1[0]*t0**2+a1[1]*t0+a1[2]
            d1rmse=np.sqrt(np.mean((d1-d0)**2))
        
            b1=np.polyfit(t0,vs0,2)
            vs1=b1[0]*t0**2+b1[1]*t0+b1[2]
            vs1rmse=np.sqrt(np.mean((vs1-vs0)**2))
        
            c1=np.polyfit(t0,vp0,2)
            vp1=c1[0]*t0**2+c1[1]*t0+c1[2]
            vp1rmse=np.sqrt(np.mean((vp1-vp0)**2))
        
            po2=np.array([a1[0],a1[1],a1[2],b1[0],b1[1],b1[2],c1[0],c1[1],c1[2]])
            po2.reshape(3,3)
            
            po2a=np.matrix(np.array([a1[0],b1[0],c1[0],a1[1],b1[1],c1[1],a1[2],b1[2],c1[2]]))
            po2a.resize(3,3)
        
            if v in ['m','matrix']:
                
                np.savetxt(s[0:2]+'2o'+str(p)+'.txt',po2a,header='Density, Vs, Vp')
                return[po2a]
        
            elif v in ['r','read']:
            
                with open(s[0:2]+'2or'+str(p)+'.txt','w') as fname:
                    fname.write('No.\t   Density\t              Vs\t                Vp\n')
                    fname.write('RMSE\t%2.10e\t%2.10e\t%2.10e\n'%(d1rmse,vs1rmse,vp1rmse))
                    fname.write('0\t%2.10e\t%2.10e\t%2.10e\n1\t%2.10e\t%2.10e\t%2.10e\n2\t%2.10e\t%2.10e\t%2.10e\n'%(po2[0],po2[3],po2[6],po2[1],po2[4],po2[7],po2[2],po2[5],po2[8]))
        
                return[po2a]
            
            elif v in ['b','both']:
                np.savetxt(s[0:2]+'2o'+str(p)+'.txt',po2a,header='Density, Vs, Vp')
                
                with open(s[0:2]+'2or'+str(p)+'.txt','w') as fname:
                    fname.write('No.\t   Density\t              Vs\t                Vp\n')
                    fname.write('RMSE\t%2.10e\t%2.10e\t%2.10e\n'%(d1rmse,vs1rmse,vp1rmse))
                    fname.write('0\t%2.10e\t%2.10e\t%2.10e\n1\t%2.10e\t%2.10e\t%2.10e\n2\t%2.10e\t%2.10e\t%2.10e\n'%(po2[0],po2[3],po2[6],po2[1],po2[4],po2[7],po2[2],po2[5],po2[8]))
            
                return[po2a]
            
        elif o in ['5']:    
            a2 =np.polyfit(t0,d0,5)
            d2= a2[0]*t0**5+a2[1]*t0**4+a2[2]*t0**3+a2[3]*t0**2+a2[4]*t0+a2[5]
            d2rmse=np.sqrt(np.mean((d2-d0)**2))
        
            b2 =np.polyfit(t0,vs0,5)
            vs2= b2[0]*t0**5+b2[1]*t0**4+b2[2]*t0**3+b2[3]*t0**2+b2[4]*t0+b2[5]
            vs2rmse=np.sqrt(np.mean((vs2-vs0)**2))
        
            c2 =np.polyfit(t0,vp0,5)
            vp2= c2[0]*t0**5+c2[1]*t0**4+c2[2]*t0**3+c2[3]*t0**2+c2[4]*t0+c2[5]
            vp2rmse=np.sqrt(np.mean((vp2-vp0)**2))
        
            po5=np.array([a2[0],a2[1],a2[2],a2[3],a2[4],a2[5],b2[0],b2[1],b2[2],b2[3],b2[4],b2[5],c2[0],c2[1],c2[2],c2[3],c2[4],c2[5]])
            po5.reshape(6,3)
        
            po5a=np.matrix(np.array([a2[0],b2[0],c2[0],a2[1],b2[1],c2[1],a2[2],b2[2],c2[2],a2[3],b2[3],c2[3],a2[4],b2[4],c2[4],a2[5],b2[5],c2[5]]))
            po5a.resize(6,3)
        
    
            if v in ['m','matrix']:
                
                np.savetxt(s[0:2]+'5o'+str(p)+'.txt',po5a,header='Density, Vs, Vp')
                return[po5a]
        
            elif v in ['r','read']:
                with open(s[0:2]+'5or'+str(p)+'.txt','w') as fname:
                    fname.write('No.\t   Density\t              Vs\t                Vp\n')
                    fname.write('RMSE\t%2.10e\t%2.10e\t%2.10e\n'%(d2rmse,vs2rmse,vp2rmse))
                    fname.write('0\t%2.10e\t%2.10e\t%2.10e\n1\t%2.10e\t%2.10e\t%2.10e\n2\t%2.10e\t%2.10e\t%2.10e\n3\t%2.10e\t%2.10e\t%2.10e\n4\t%2.10e\t%2.10e\t%2.10e\n5\t%2.10e\t%2.10e\t%2.10e\n'%(po5[0],po5[6],po5[12],po5[1],po5[7],po5[13],po5[2],po5[8],po5[14],po5[3],po5[9],po5[15],po5[4],po5[10],po5[16],po5[5],po5[11],po5[17]))
            
                return[po5a]
        
            elif v in ['b','both']:
                np.savetxt(s[0:2]+'5o'+str(p)+'.txt',po5a,header='Density, Vs, Vp')
                
                with open(s[0:2]+'5or'+str(p)+'.txt','w') as fname:
                    fname.write('No.\t   Density\t              Vs\t                Vp\n')
                    fname.write('RMSE\t%2.10e\t%2.10e\t%2.10e\n'%(d2rmse,vs2rmse,vp2rmse))
                    fname.write('0\t%2.10e\t%2.10e\t%2.10e\n1\t%2.10e\t%2.10e\t%2.10e\n2\t%2.10e\t%2.10e\t%2.10e\n3\t%2.10e\t%2.10e\t%2.10e\n4\t%2.10e\t%2.10e\t%2.10e\n5\t%2.10e\t%2.10e\t%2.10e\n'%(po5[0],po5[6],po5[12],po5[1],po5[7],po5[13],po5[2],po5[8],po5[14],po5[3],po5[9],po5[15],po5[4],po5[10],po5[16],po5[5],po5[11],po5[17]))
            
                return[po5a]
        
        elif o in ['7']:
            a3=np.polyfit(t0,d0,7)
            d3=a3[0]*t0**7+a3[1]*t0**6+a3[2]*t0**5+a3[3]*t0**4+a3[4]*t0**3+a3[5]*t0**2+a3[6]*t0+a3[7]
            d3rmse=np.sqrt(np.mean((d3-d0)**2))
        
            b3=np.polyfit(t0,vs0,7)
            vs3=b3[0]*t0**7+b3[1]*t0**6+b3[2]*t0**5+b3[3]*t0**4+b3[4]*t0**3+b3[5]*t0**2+b3[6]*t0+b3[7]
            vs3rmse=np.sqrt(np.mean((vs3-vs0)**2))
        
            c3=np.polyfit(t0,vp0,7)
            vp3=c3[0]*t0**7+c3[1]*t0**6+c3[2]*t0**5+c3[3]*t0**4+c3[4]*t0**3+c3[5]*t0**2+c3[6]*t0+c3[7]
            vp3rmse=np.sqrt(np.mean((vp3-vp0)**2))
        
            po7=np.array([a3[0],a3[1],a3[2],a3[3],a3[4],a3[5],a3[6],a3[7],b3[0],b3[1],b3[2],b3[3],b3[4],b3[5],b3[6],b3[7],c3[0],c3[1],c3[2],c3[3],c3[4],c3[5],c3[6],c3[7]])
            po7.reshape(8,3)
        
        
            po7a=np.matrix(np.array([a3[0],b3[0],c3[0],a3[1],b3[1],c3[1],a3[2],b3[2],c3[2],a3[3],b3[3],c3[3],a3[4],b3[4],c3[4],a3[5],b3[5],c3[5],a3[6],b3[6],c3[6],a3[7],b3[7],c3[7]]))
            po7a.resize(8,3)
        
    
            if v in ['m','matrix']:
                
                np.savetxt(s[0:2]+'7o'+str(p)+'.txt',po7a,header='Density, Vs, Vp')
                return[po7a]
        
            elif v in ['r','read']:
                with open(s[0:2]+'7or'+str(p)+'.txt','w') as fname:
                    fname.write('No.\t   Density\t              Vs\t                Vp\n')
                    fname.write('RMSE\t%2.10e\t%2.10e\t%2.10e\n'%(d3rmse,vs3rmse,vp3rmse))
                    fname.write('0\t%2.10e\t%2.10e\t%2.10e\n1\t%2.10e\t%2.10e\t%2.10e\n2\t%2.10e\t%2.10e\t%2.10e\n3\t%2.10e\t%2.10e\t%2.10e\n4\t%2.10e\t%2.10e\t%2.10e\n5\t%2.10e\t%2.10e\t%2.10e\n6\t%2.10e\t%2.10e\t%2.10e\n7\t%2.10e\t%2.10e\t%2.10e\n'%(po7[0],po7[8],po7[16],po7[1],po7[9],po7[17],po7[2],po7[10],po7[18],po7[3],po7[11],po7[19],po7[4],po7[12],po7[20],po7[5],po7[13],po7[21],po7[6],po7[14],po7[22],po7[7],po7[15],po7[23]))
        
                return[po7a]
        
            elif v in ['b','both']:
                np.savetxt(s[0:2]+'7o'+str(p)+'.txt',po7a,header='Density, Vs, Vp')
                
                with open(s[0:2]+'7or'+str(p)+'.txt','w') as fname:
                    fname.write('No.\t   Density\t              Vs\t                Vp\n')
                    fname.write('RMSE\t%2.10e\t%2.10e\t%2.10e\n'%(d3rmse,vs3rmse,vp3rmse))
                    fname.write('0\t%2.10e\t%2.10e\t%2.10e\n1\t%2.10e\t%2.10e\t%2.10e\n2\t%2.10e\t%2.10e\t%2.10e\n3\t%2.10e\t%2.10e\t%2.10e\n4\t%2.10e\t%2.10e\t%2.10e\n5\t%2.10e\t%2.10e\t%2.10e\n6\t%2.10e\t%2.10e\t%2.10e\n7\t%2.10e\t%2.10e\t%2.10e\n'%(po7[0],po7[8],po7[16],po7[1],po7[9],po7[17],po7[2],po7[10],po7[18],po7[3],po7[11],po7[19],po7[4],po7[12],po7[20],po7[5],po7[13],po7[21],po7[6],po7[14],po7[22],po7[7],po7[15],po7[23]))
        
                return[po7a]
    
    def calculate(self,p,s,phys,spin,M,Fe,sys,T):
        #Melt values (peridotite melt)
        pe=2.40
        p0=3.30
        K=555.28


        md=pe*p0 #density of melt (g/cm^3)
        mvp=(K/md)**0.5 #speed of Vp in melt (km/s)
        mvs=0 #speed of Vs in melt (km/s)
        tp=T #K temp.
        
        
        myFile = open(s, 'r')
        cutText = myFile.read().splitlines() 
        cutText.pop(0) 

        #lists for storing data
        t=[]
        d=[]
        vs=[]
        vp=[]

        #we go through the text line be line (row). We split each row into individual entries (columns)
        for i in cutText: #make into columns 
            t.append(float(i.split()[2]))
            d.append(float(i.split()[3]))
            vs.append(float(i.split()[5]))
            vp.append(float(i.split()[6]))
        
        t0=np.array(t[p::1401])
        d0=np.array(d[p::1401])
        vs0=np.array(vs[p::1401])
        vp0=np.array(vp[p::1401])
        
        a3=np.polyfit(t0,d0,7)
        b3=np.polyfit(t0,vs0,7)
        c3=np.polyfit(t0,vp0,7)
        
        if phys in ['Density','D','d']:
            
            dpy=a3[0]*tp**7+a3[1]*tp**6+a3[2]*tp**5+a3[3]*tp**4+a3[4]*tp**3+a3[5]*tp**2+a3[6]*tp+a3[7]
        
            if spin in ['AFM','afm']:
                Fec=np.array([0,0.5,1])
                DAFM=np.array([5.27,5.94,6.57])
                dAFM=np.polyfit(Fec,DAFM,1) 
                dc=dAFM[0]*Fe+dAFM[1]
                
            elif spin in ['FM','fm']:
                Fec=np.array([0,0.5,1])
                DFM=np.array([5.27,5.96,6.57])
                dFM=np.polyfit(Fec,DFM,1)
                dc=dFM[0]*Fe+dFM[1]
                
            elif spin in ['NS','ns']:
                Fec=np.array([0,0.5,1])
                DNS=np.array([5.27,6.06,6.85])
                dNS=np.polyfit(Fec,DNS,1)
                dc=dNS[0]*Fe+dNS[1]
            
            
                
            D=M*md+(1-M)*(Fe*dc+(1-Fe)*dpy)
            return(D)
        
        elif phys in ['Vp','VP','vp']:
            vppy=c3[0]*tp**7+c3[1]*tp**6+c3[2]*tp**5+c3[3]*tp**4+c3[4]*tp**3+c3[5]*tp**2+c3[6]*tp+c3[7]
            
            if sys in['iso','ISO']:
                if spin in ['AFM','afm']:
                    Fec=np.array([0,0.5,1])
                    VpisAFM=([13.710,12.339,11.116])
                    vpisAFMc=np.polyfit(Fec,VpisAFM,1)
                    vp=vpisAFMc[0]*Fe+vpisAFMc[1]
                
                elif spin in ['FM','fm']:
                    Fec=np.array([0,0.5,1])
                    VpisFM=([13.710,12.400,11.149])
                    vpisFMc=np.polyfit(Fec,VpisFM,1)
                    vp=vpisFMc[0]*Fe+vpisFMc[1]
                
                elif spin in ['NS','ns']:
                    Fec=np.array([0,0.5,1])
                    VpisNS=([13.710,12.693,11.802])
                    vpisNSc=np.polyfit(Fec,VpisNS,1)
                    vp=vpisNSc[0]*Fe+vpisNSc[1]
                
            elif sys in ['adi','ADI']:
                if spin in ['AFM','afm']:
                    Fec=np.array([0,0.5,1])
                    VpadAFM=([13.837,12.480,11.252])
                    vpadAFMc=np.polyfit(Fec,VpadAFM,1)
                    vp=vpadAFMc[0]*Fe+vpadAFMc[1]
                
                elif spin in ['FM','fm']:
                    Fec=np.array([0,0.5,1])
                    VpadFM=([13.837,12.521,11.301])
                    vpadFMc=np.polyfit(Fec,VpadFM,1)
                    vp=vpadFMc[0]*Fe+vpadFMc[1]
                
                elif spin in ['NS','ns']:
                    Fec=np.array([0,0.5,1])
                    VpadNS=([13.837,12.856,11.939])
                    vpadNSc=np.polyfit(Fec,VpadNS,1)
                    vp=vpadNSc[0]*Fe+vpadNSc[1]
                    
            Vp=M*mvp+(1-M)*(Fe*vp+(1-Fe)*vppy)
            return (Vp)
        
        elif phys in ['Vs','VS','vs']:
            vspy=b3[0]*tp**7+b3[1]*tp**6+b3[2]*tp**5+b3[3]*tp**4+b3[4]*tp**3+b3[5]*tp**2+b3[6]*tp+b3[7]
        
            if spin in ['AFM','afm']:
                Fec=np.array([0,0.5,1])
                VsAFM=([7.107,5.984,4.854])
                vsAFMc=np.polyfit(Fec,VsAFM,1)
                vs=vsAFMc[0]*Fe+vsAFMc[1]
                
            elif spin in ['FM','fm']:
                Fec=np.array([0,0.5,1])
                VsFM=([7.107,5.979,4.705])
                vsFMc=np.polyfit(Fec,VsFM,1)
                vs=vsFMc[0]*Fe+vsFMc[1]
                
            elif spin in ['NS','ns']:
                Fec=np.array([0,0.5,1])
                VsNS=([7.107,6.150,5.344])
                vsNSc=np.polyfit(Fec,VsNS,1)
                vs=vsNSc[0]*Fe+vsNSc[1]
            
            
                
            Vs=M*mvs+(1-M)*(Fe*vs+(1-Fe)*vspy)
            return (Vs)
    def colourmap(self,p,s,phys,spin,sys,T):
        #Melt values (peridotite melt)
        pe=2.40
        p0=3.30
        K=555.28


        md=pe*p0 #density of melt (g/cm^3)
        mvp=(K/md)**0.5 #speed of Vp in melt (km/s)
        mvs=0 #speed of Vs in melt (km/s)
        tp=T #K temp.
        
        myFile = open(s, 'r')
        cutText = myFile.read().splitlines() 
        cutText.pop(0) 

        #lists for storing data
        t=[]
        d=[]
        vs=[]
        vp=[]

        #we go through the text line be line (row). We split each row into individual entries (columns)
        for i in cutText: #make into columns 
            t.append(float(i.split()[2]))
            d.append(float(i.split()[3]))
            vs.append(float(i.split()[5]))
            vp.append(float(i.split()[6]))
        
        t0=np.array(t[p::1401])
        d0=np.array(d[p::1401])
        vs0=np.array(vs[p::1401])
        vp0=np.array(vp[p::1401])
        
        a3=np.polyfit(t0,d0,7)
        b3=np.polyfit(t0,vs0,7)
        c3=np.polyfit(t0,vp0,7)
            
        if phys in ['Density','D','d']:
            dpy=a3[0]*tp**7+a3[1]*tp**6+a3[2]*tp**5+a3[3]*tp**4+a3[4]*tp**3+a3[5]*tp**2+a3[6]*tp+a3[7]
            
            list=[]
            for m in range(0,11,1):
                for fe in range(0,11,1):
                    if spin in ['AFM','afm']:
                        Fec=np.array([0,0.5,1])
                        DAFM=np.array([5.27,5.94,6.57])
                        dAFM=np.polyfit(Fec,DAFM,1) 
                        d=dAFM[0]*fe*0.1+dAFM[1]
                
                    elif spin in ['FM','fm']:
                        Fec=np.array([0,0.5,1])
                        DFM=np.array([5.27,5.96,6.57])
                        dFM=np.polyfit(Fec,DFM,1)
                        d=dFM[0]*fe*0.1+dFM[1]
                
                    elif spin in ['NS','ns']:
                        Fec=np.array([0,0.5,1])
                        DNS=np.array([5.27,6.06,6.85])
                        dNS=np.polyfit(Fec,DNS,1)
                        d=dNS[0]*fe*0.1+dNS[1]
            
                    y=m*0.1*md+(1-m*0.1)*(fe*0.1*d+(1-fe*0.1)*dpy)
                    list.append(y)
                
            matrix=np.matrix(np.asarray(list))
            matrix.resize([11,11])



            plt.imshow(matrix)
            plt.colorbar(label=phys,orientation='vertical')
            plt.xlabel('Fe(10%)')
            plt.ylabel('Melt(10%)')
            plt.title('Colour map ('+spin+')')
            plt.show()
            
        
        elif phys in ['Vp','VP','vp']:
            vppy=c3[0]*tp**7+c3[1]*tp**6+c3[2]*tp**5+c3[3]*tp**4+c3[4]*tp**3+c3[5]*tp**2+c3[6]*tp+c3[7]
            
            list=[]
            for m in range(0,11,1):
                for fe in range(0,11,1):
                    if sys in['iso','ISO']:
                        if spin in ['AFM','afm']:
                            Fec=np.array([0,0.5,1])
                            VpisAFM=([13.710,12.339,11.116])
                            vpisAFMc=np.polyfit(Fec,VpisAFM,1)
                            vp=vpisAFMc[0]*fe*0.1+vpisAFMc[1]
                
                        elif spin in ['FM','fm']:
                            Fec=np.array([0,0.5,1])
                            VpisFM=([13.710,12.400,11.149])
                            vpisFMc=np.polyfit(Fec,VpisFM,1)
                            vp=vpisFMc[0]*fe*0.1+vpisFMc[1]
                
                        elif spin in ['NS','ns']:
                            Fec=np.array([0,0.5,1])
                            VpisNS=([13.710,12.693,11.802])
                            vpisNSc=np.polyfit(Fec,VpisNS,1)
                            vp=vpisNSc[0]*fe*0.1+vpisNSc[1]
                
                    elif sys in ['adi','ADI']:
                        if spin in ['AFM','afm']:
                            Fec=np.array([0,0.5,1])
                            VpadAFM=([13.837,12.480,11.252])
                            vpadAFMc=np.polyfit(Fec,VpadAFM,1)
                            vp=vpadAFMc[0]*fe*0.1+vpadAFMc[1]
                
                        elif spin in ['FM','fm']:
                            Fec=np.array([0,0.5,1])
                            VpadFM=([13.837,12.521,11.301])
                            vpadFMc=np.polyfit(Fec,VpadFM,1)
                            vp=vpadFMc[0]*fe*0.1+vpadFMc[1]
                
                        elif spin in ['NS','ns']:
                            Fec=np.array([0,0.5,1])
                            VpadNS=([13.837,12.856,11.939])
                            vpadNSc=np.polyfit(Fec,VpadNS,1)
                            vp=vpadNSc[0]*fe*0.1+vpadNSc[1]
                    
                    y=m*0.1*mvp+(1-m*0.1)*(fe*0.1*vp+(1-fe*0.1)*vppy)
                    list.append(y)
                 
            matrix=np.matrix(np.asarray(list))
            matrix.resize([11,11])



            plt.imshow(matrix)
            plt.colorbar(label=phys,orientation='vertical')
            plt.xlabel('Fe(10%)')
            plt.ylabel('Melt(10%)')
            plt.title('Colour map ('+spin+')')
            plt.show()
           
        
        elif phys in ['Vs','VS','vs']:
            vspy=b3[0]*tp**7+b3[1]*tp**6+b3[2]*tp**5+b3[3]*tp**4+b3[4]*tp**3+b3[5]*tp**2+b3[6]*tp+b3[7]
            
            list=[]
            for m in range(0,11,1):
                for fe in range(0,11,1):
                    if spin in ['AFM','afm']:
                        Fec=np.array([0,0.5,1])
                        VsAFM=([7.107,5.984,4.854])
                        vsAFMc=np.polyfit(Fec,VsAFM,1)
                        vs=vsAFMc[0]*fe*0.1+vsAFMc[1]
                
                    elif spin in ['FM','fm']:
                        Fec=np.array([0,0.5,1])
                        VsFM=([7.107,5.979,4.705])
                        vsFMc=np.polyfit(Fec,VsFM,1)
                        vs=vsFMc[0]*fe*0.1+vsFMc[1]
                
                    elif spin in ['NS','ns']:
                        Fec=np.array([0,0.5,1])
                        VsNS=([7.107,6.150,5.344])
                        vsNSc=np.polyfit(Fec,VsNS,1)
                        vs=vsNSc[0]*fe*0.1+vsNSc[1]
                        
                    y=m*0.1*mvs+(1-m*0.1)*(fe*0.1*vs+(1-fe*0.1)*vspy)
                    list.append(y)
            
            matrix=np.matrix(np.asarray(list))
            matrix.resize([11,11])



            plt.imshow(matrix)
            plt.colorbar(label=phys,orientation='vertical')
            plt.xlabel('Fe(10%)')
            plt.ylabel('Melt(10%)')
            plt.title('Colour map ('+spin+')')
            plt.show()
        
