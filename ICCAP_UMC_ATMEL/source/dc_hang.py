# -*-coding: utf-8 -*-


import os

def search():
    global pairs
    global pairs_index
    pairs_index=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    filelist=[]
    dirlist=[]
    index=[]
    for root,dirs,files in dircontent:
        files_n=files[:]
        for i in range(len(files)):
            files_n[i]=files[i].lower()
            findf=(files_n[i].find('idvg'))*(files_n[i].find('id_vg'))
            finds=(files_n[i].find('idvd'))*(files_n[i].find('id_vd'))
            if (findf<0 or finds<0) and files_n[i].endswith('dat') and files_n[i].find('rf')==-1:
                filelist.append(files_n[i])
                dirlist.append(os.path.join(root,files[i]))
                index.append(-findf*finds)

    #then find the paires
    pairs=[]
    for i in range(len(filelist)):
        temp=filelist[i][0:index[i]]
        for j in range(i+1,len(filelist)):
            if filelist[j][0:index[i]]==temp:
                templist=[dirlist[i],dirlist[j]]
                pairs.append(templist)
                pairs_index.append(index[i])

def combine():
    global pairs
    global pairs_index
    global combody
    global comdir
    if len(pairs)<>0:
        print 'Combine Id_Vg and Id_Vd data file'
    combody=[]
    comdir=[]
    for i in range(0,len(pairs)):
        f1=open(pairs[i][0],'r')
        f1con=f1.readlines()
        f1.close()
        f2=open(pairs[i][1],'r')
        f2con=f2.readlines()
        f2.close()
        # deal with the output problem
        templist=[]
        for k in range(0,len(f1con)):
            if f1con[k].find('Output')<>-1:
                begin=f1con[k].find('{')
                tempstr=f1con[k][begin:]
                tempstr=tempstr.strip('{}\n')
                templist.extend(tempstr.split(','))
        for k in range(0,len(f2con)):
            if f2con[k].find('Output')<>-1:
                begin=f2con[k].find('{')
                tempstr=f2con[k][begin:]
                tempstr=tempstr.strip('{}\n')
                templist.extend(tempstr.split(','))
        outputlist=list(set(templist))
        outputstr='Output{%s}\n'%(','.join(outputlist))
        # deal with the problem of order
        if (pairs[i][0].lower()).find('idvg')<>-1 or (pairs[i][0].lower()).find('id_vg')<>-1:
            startcon=f1con
            hangcon=f2con
        else:
            startcon=f2con
            hangcon=f1con
        for j in range(0,len(startcon)):
            if startcon[j].find('Output')<>-1:
                startcon[j]=outputstr
        tempcon=[]
        for j in range(0,len(hangcon)):
            if hangcon[j].startswith('{i'):
                hangcon[j]='\n'+hangcon[j]
                tempcon.extend(hangcon[j:])
                break
        startcon.extend(tempcon)
        combody.append(startcon)
    #made name
        basename=os.path.basename(pairs[i][0])
        dirname=os.path.join('Converted data\\dc_combine','%s_dc'%basename[0:pairs_index[i]])
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        basename=basename[0:pairs_index[i]]+'_dc.dat'
        path=os.path.join(dirname,basename)
        comdir.append(path)

def dchang():
    global combody
    global comdir
    search()
    combine()
    flag=1
    for i in range(0,len(comdir)):
        if os.path.exists(comdir[i]):
            comdir[i]=list(comdir[i])
            comdir[i].insert(-4,'(%s)'%flag)
            comdir[i]=''.join(comdir[i])
            flag=flag+1
        writepath=comdir[i]
        f=open(writepath,'w')
        f.writelines(combody[i])
        f.close()




