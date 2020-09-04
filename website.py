from flask import Flask, render_template, request, redirect, url_for
from datetime import timedelta
import csv
import random

def randomlink():
    s='/'
    q=random.randint(11,15)
    for i in range(q):
        k=random.randint(0,3)
        if k==0:
            w=random.randint(65,90)
            s+=chr(w)    
        if k==1:
            r=random.randint(0,9)
            s+=str(r)  
        if k==2:
            l=['!','@','#','%','^','&','*']
            w=random.randint(0,6)
            s+=l[w]
        if k==3:
            o=random.randint(97,122)
            s+=chr(o)
    return s
app=Flask(__name__)
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        a='h#f@l*m@o!x@o@s&l^e^'
        j=''
        for i in range(len(a)):
            if i%2==0:
                j+=a[i]
            else:
                pass
        w=''
        for i in range(len(j)):
            k=j[i]
            if i%2==0:
                w+=k
            else:
                w+=chr(ord(k)-1)

        if user == w:
            return redirect(url_for('home'))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route(randomlink(), methods=["POST","GET"])
def home():
    l=[]
    if request.method=='POST':
        if request.form['submit_button']=='Add/Gen Password':
            return redirect(url_for('add'))
        elif request.form['submit_button']=='Search':
            return redirect(url_for('search'))
        else:
            return redirect(url_for('remove'))
        
    f=open("TopSecrets.csv",'r')
    k=csv.reader(f)
    for b in k:
        a=b[2]
        j=''
        for i in range(len(a)):
            if i%2==0:
                j+=a[i]
            else:
                pass
        w=''
        for i in range(len(j)):
            k=j[i]
            if i%2==0:
                w+=k
            else:
                w+=chr(ord(k)-1)
        r=[b[0],b[1],w]
        l.append(r)
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j][0].lower()>l[j+1][0].lower():
                l[j],l[j+1]=l[j+1],l[j]
    return render_template("index.html", l=l)
@app.route(randomlink(),methods=['POST','GET'])
def add():
    if request.method=='POST':
        if request.form['submit_button']=='Add':
            sitename=request.form['site']
            username=request.form['uname']
            a=request.form['password']

            if len(sitename)==0 or len(username)==0 or len(a)==0:
                return render_template("details.html")
            else:
                w=''
                for i in range(len(a)):
                    k=a[i]
                    if i%2==0:
                        w+=k
                    else:
                        w+= chr(ord(k)+1)
                j=''
                for i in range(len(w)):
                    j+=w[i]
                    l=['!','@','#','%','^','&','*']
                    g=random.randint(0,6)
                    j+=l[g]
                
                w=[sitename,username,j]
                f=open("TopSecrets.csv",'a+')
                writer=csv.writer(f)
                
                writer.writerow(w)
                return redirect(url_for('home'))
        elif request.form['submit_button']=='Generate':
            sitename=request.form['site']
            username=request.form['uname']
            password=request.form['password']
            if len(password)!=0:
                return render_template('details.html')
            elif len(sitename)!=0 or len(username)!=0 or len(password)==0:
                a=''
                q=random.randint(11,15)
                for i in range(q):
                    k=random.randint(0,3)
                    if k==0:
                        w=random.randint(65,90)
                        a+=chr(w)
                    if k==1:
                        r=random.randint(0,9)
                        a+=str(r)
                    if k==2:
                        l=['!','@','#','%','^','&','*']
                        w=random.randint(0,6)
                        a+=l[w]
                    if k==3:
                        o=random.randint(97,122)
                        a+=chr(o)
                m=a
                w=''
                for i in range(len(a)):
                    k=a[i]
                    if i%2==0:
                        w+=k
                    else:
                        w+= chr(ord(k)+1)
                j=''
                for i in range(len(w)):
                    j+=w[i]
                    l=['!','@','#','%','^','&','*']
                    g=random.randint(0,6)
                    j+=l[g]
            
                w=[sitename,username,j]
                f=open("TopSecrets.csv",'a+')
                writer=csv.writer(f)
            
                writer.writerow(w)
                return redirect(url_for('home'))
            
        elif request.form['submit_button']=='Home':
            return redirect(url_for('home'))
                
                

    else:
        return render_template('details.html')
@app.route(randomlink(),methods=['POST','GET'])
def remove():
    l=[]
    f=open("TopSecrets.csv",'r')
    k=csv.reader(f)
    for b in k:
        a=b[2]
        j=''
        for i in range(len(a)):
            if i%2==0:
                j+=a[i]
            else:
                pass
        w=''
        for i in range(len(j)):
            k=j[i]
            if i%2==0:
                w+=k
            else:
                w+=chr(ord(k)-1)
        r=[b[0],b[1],w]
        l.append(r)

        for i in range(len(l)):
            for j in range(len(l)-1):
                if l[j][0].lower()>l[j+1][0].lower():
                    l[j],l[j+1]=l[j+1],l[j]

    if request.method=='POST':
        l=[]
        f=open("TopSecrets.csv",'r')
        k=csv.reader(f)
        for i in k:
            l.append(i)
        f.close()
        sitename=request.form['site']
        username=request.form['uname']
        if sitename=='Site Name':
            return redirect(url_for('home'))
        else:
            l2=[]
            for i in l:

                if (i[0]!=sitename or i[1]!=username) :
                    l2.append(i)
                
            print(l2)
            f=open('TopSecrets.csv','w')
            writer=csv.writer(f)
            writer.writerows(l2)
            return redirect(url_for('home'))
    else:
        return render_template('remove.html',l=l)
@app.route(randomlink(),methods=['POST','GET'])   
def search():
    if request.method=='POST':
        if request.form['submit_button']=='Search':
            return redirect(url_for('result'))

    else:
        return render_template('search.html')        
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        if request.form['submit_button']=='Home':
            return redirect(url_for('home'))
    else:
        l=[["Site Name", "Username", "Password"]]
        sitename=request.form['site']
        f=open("TopSecrets.csv",'r')
        k=csv.reader(f)
        for b in k:
            if b[0].lower() ==sitename.lower():
                a=b[2]
                j=''
                for i in range(len(a)):
                    if i%2==0:
                        j+=a[i]
                    else:
                        pass
                w=''
                for i in range(len(j)):
                    k=j[i]
                    if i%2==0:
                        w+=k
                    else:
                        w+=chr(ord(k)-1)
                r=[b[0],b[1],w]
                l.append(r)
        return render_template('searchresult.html',l=l)
        


if __name__=="__main__":
    app.run(debug=True)