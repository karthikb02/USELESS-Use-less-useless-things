from flask import Flask,render_template,request,redirect,url_for,flash
from database import DataBase
import smtplib
from datetime import date, timedelta

def sendSuccessReg(name,email):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("teamuseless2020@gmail.com", "Useless@2020")
	text="""Hello """+name+"\n\n"+"""Welcome to our family.We are extremely happy that you have come forward to take part in our initiative to save mother earth!\n\"Little drops make a mighty ocean\"  we all know that! Your small part can make wonders to our society!! Using Use-less will definitely help you and make you feel that you are doing something for the benefit of a healthy living! We keep track of your waste so that you can reduce unnecessary usage of products and implement more of reusing and recycling!"""
	message = """From: Team USE-LESS\nSubject:Registration Successful! \n\n"""+text
	s.sendmail("teamuseless2020@gmail.com", email, message)
	print("Mail sent Successfully")
	s.quit()

def redeemMail(name,accNo,bank,branch,ifsc,points):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("teamuseless2020@gmail.com", "Useless@2020")
	text="""Hello Team USE-LESS!"""+"\n\n"+"I take immense pleasure in contributing something good for the welfare of our society. I wish to harvest my yield by converting my redeem points to cash. Please do the needful. My details are listed below\n\n"+"Beneficiary name : "+name+"\nAccount number : "+accNo+"\nBank name : "+bank+"\nBranch : "+branch+"\nIFSC code : "+ifsc+"\nPoints : "+points+"\n\nThank you!"
	message = """From: Team USE-LESS\nSubject:REDEEM POINTS \n\n"""+text
	s.sendmail("teamuseless2020@gmail.com","teamuseless2020@gmail.com", message)
	print("Mail sent Successfully")
	s.quit()
	
def passResetMail(name,email):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("teamuseless2020@gmail.com", "Useless@2020")
	text="""Hello """+name+"\n\n"+"Your USE-LESS account Password has been updated successfully!"
	message = """From: Team USE-LESS\nSubject:Password Resetted Successfully! \n\n"""+text
	s.sendmail("teamuseless2020@gmail.com", email, message)
	print("Mail sent Successfully")
	s.quit()

def orderSuccessMail(email):
	name=db.users[email][1]
	bioDeg=db.users[email][4]
	nonBioDeg=db.users[email][5]
	metal=db.users[email][6]
	electronic=db.users[email][7]
	medical=db.users[email][8]
	totalWaste=db.users[email][9]
	points=db.users[email][10]
	dt = date.today() + timedelta(4)
	y,m,d=str(dt).split('-')
	dat=d+'-'+m+'-'+y
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("teamuseless2020@gmail.com", "Useless@2020")
	text="""Hello """+name+","+"\n\n"+"Hooray!\n"+"You have done something good for your society! What you sow you shall reap!! We have received your order. Our agent will come to your place and collect your waste on or before "+dat+". Agent details will be updated to you as soon as he is assigned. \nThank you!\n\n\n"+"Order Summary:-\nBio-Degradable : "+bioDeg+" Kg\nNon-BioDegradable : "+nonBioDeg+" Kg\nMetal : "+metal+" Kg\nElectronics : "+electronic+" Kg\nMedical : "+medical+" Kg\nTotal Weight : "+totalWaste+" Kg\nTotal Points Earned : "+points+"\n\nHaving any queries? Please feel free to contact us !"
	message = """From: Team USE-LESS\nSubject:PickUp Generated Successfully! \n\n"""+text
	s.sendmail("teamuseless2020@gmail.com", email, message)
	print("Mail sent Successfully")
	s.quit()
	
def comOrderSuccessMail(email):
	name=db.users[email][1]
	bioDeg=db.users[email][4]
	nonBioDeg=db.users[email][5]
	metal=db.users[email][6]
	electronic=db.users[email][7]
	medical=db.users[email][8]
	totalWaste=db.users[email][9]
	points=db.users[email][10]
	dt = date.today() + timedelta(4)
	y,m,d=str(dt).split('-')
	dat=d+'-'+m+'-'+y
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("teamuseless2020@gmail.com", "Useless@2020")
	text="""Hello """+name+","+"\n\n"+"Hooray!\n"+"Thank you for purchasing goods from us! We know that you have the potential to discard waste in the right method!! Thank you for taking part with us to see a change in our world. Please send your agent details who will be picking up products from us.\n\n Your Order Summary is given below:-\nBio-Degradable : "+bioDeg+" Kg\nNon-BioDegradable : "+nonBioDeg+" Kg\nMetal : "+metal+" Kg\nElectronics : "+electronic+" Kg\nMedical : "+medical+" Kg\nTotal Weight : "+totalWaste+" Kg\nTotal Points : "+points+"\n\nHaving any queries? Please feel free to contact us !"
	message = """From: Team USE-LESS\nSubject:Order Placed Successfully! \n\n"""+text
	s.sendmail("teamuseless2020@gmail.com", email, message)
	print("Mail sent Successfully")
	s.quit()
db=DataBase("users.txt")


app = Flask(__name__)

app.secret_key = 'random string'

@app.route('/')
def homePage():
    return render_template("homepage.html")
    
@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/passReset.html')
def passReset():
	return render_template('passReset.html')
	
@app.route('/resetPopup.html',methods=['POST'])
def resetPopup():
	email=request.form['userName']
	password=request.form['newPass']
	conPass=request.form['confirmNewPass']
	if email not in db.users:
		flash("Please Enter Valid Email ID")
		return redirect(url_for('passReset'))
	elif password!=conPass:
		flash("Password must be same")
		return redirect(url_for('passReset'))
	lis=list(db.users[email])
	lis[0]=str(password)
	db.users[email]=tuple(lis)
	db.save()
	passResetMail(db.users[email][1],email)
	return render_template('resetPopup.html')
	
@app.route('/homepage.html')
def homePageReload():
    return render_template("homepage.html")

@app.route('/popupreg.html')
def popup():
    return render_template("popupreg.html")

@app.route('/detailsPopup.html',methods=['POST'])
def detailsPopup():
	name=request.form['name']
	accNo=request.form['accNo']
	bank=request.form['bankName']
	branch=request.form['branch']
	ifsc=request.form['ifsc']
	redeemMail(name,accNo,bank,branch,ifsc,db.users[email][-2])
	lis=list(db.users[email])
	lis[-2]=str(0)
	db.users[email]=tuple(lis)
	db.save()
	return render_template('detailsPopup.html')
	
@app.route('/companyprofile.html')
def companyProfile():
	name=db.users[email][1]
	address=db.users[email][3]
	mobile=db.users[email][2]
	bioDeg=db.users[email][4]
	nonBioDeg=db.users[email][5]
	metal=db.users[email][6]
	electronic=db.users[email][7]
	medical=db.users[email][8]
	totalWaste=db.users[email][9]
	points=db.users[email][10]
	return render_template('/companyprofile.html',email=email,name=name,mobile=mobile,address=address,bioDeg=bioDeg,nonBioDeg=nonBioDeg,metal=metal,electronic=electronic,medical=medical,totalWaste=totalWaste, points=points)
	
@app.route('/profile.html')
def profile():
	name=db.users[email][1]
	address=db.users[email][3]
	mobile=db.users[email][2]
	bioDeg=db.users[email][4]
	nonBioDeg=db.users[email][5]
	metal=db.users[email][6]
	electronic=db.users[email][7]
	medical=db.users[email][8]
	totalWaste=db.users[email][9]
	points=db.users[email][10]
	return render_template('/profile.html',email=email,name=name,mobile=mobile,address=address,bioDeg=bioDeg,nonBioDeg=nonBioDeg,metal=metal,electronic=electronic,medical=medical,totalWaste=totalWaste, points=points)

@app.route('/purchase.html',methods=['POST','GET'])
def companyLoggedIn():
	global email
	email=request.form['userName']
	password=request.form['userPass']
	if db.validate(email,password)==True:
		name=db.users[email][1]
		bioDeg=db.users['leftcornerz@gmail.com'][4]
		nonBioDeg=db.users['leftcornerz@gmail.com'][5]
		metal=db.users['leftcornerz@gmail.com'][6]
		electronic=db.users['leftcornerz@gmail.com'][7]
		medical=db.users['leftcornerz@gmail.com'][8]
		return render_template("purchase.html",userName=name,bioDeg=bioDeg,nonBioDeg=nonBioDeg,metal=metal,electronic=electronic,medical=medical)
	else:
		flash("Invalid Login Credentials")
		return redirect(url_for('companyLoginPage'))

@app.route('/sellingPage.html',methods=['POST','GET'])
def loggedIn():
	global email
	email=request.form['userName']
	password=request.form['userPass']
	if db.validate(email,password)==True:
		name=db.users[email][1]
		return render_template("sellingPage.html",userName=name)
	else:
		flash("Invalid Login Credentials")
		return redirect(url_for('loginPage'))

@app.route('/confirmationpopup.html',methods=['POST'])
def confirmationPage():
    bioDeg=request.form['bioDeg']
    nonBioDeg=request.form['nonBioDeg']
    metal=request.form['metal']
    electronic=request.form['electronic']
    medical=request.form['medical']
    com=list(db.users['leftcornerz@gmail.com'])
    com[-4]=str(int(com[-4])+int(medical))
    com[-5]=str(int(com[-5])+int(electronic))
    com[-6]=str(int(com[-6])+int(metal))
    com[-7]=str(int(com[-7])+int(nonBioDeg))
    com[-8]=str(int(com[-8])+int(bioDeg))
    db.users['leftcornerz@gmail.com']=tuple(com)
    lis=list(db.users[email])
    lis[-2]=str(int(lis[-2])+int(bioDeg)*7+int(nonBioDeg)*10+int(metal)*8+int(electronic)*5+int(medical)*8)
    lis[-3]=str(int(lis[-3])+int(bioDeg)+int(nonBioDeg)+int(metal)+int(electronic)+int(medical))
    lis[-4]=str(int(lis[-4])+int(medical))
    lis[-5]=str(int(lis[-5])+int(electronic))
    lis[-6]=str(int(lis[-6])+int(metal))
    lis[-7]=str(int(lis[-7])+int(nonBioDeg))
    lis[-8]=str(int(lis[-8])+int(bioDeg))
    db.users[email]=tuple(lis)
    db.save()
    orderSuccessMail(email)
    return render_template("confirmationpopup.html")
    
@app.route('/comconfirmationpopup.html',methods=['POST'])
def companyConfirmationPage():
    bioDeg=request.form['bioDeg']
    nonBioDeg=request.form['nonBioDeg']
    metal=request.form['metal']
    electronic=request.form['electronic']
    medical=request.form['medical']
    com=list(db.users['leftcornerz@gmail.com'])
    com[-4]=str(int(com[-4])-int(medical))
    com[-5]=str(int(com[-5])-int(electronic))
    com[-6]=str(int(com[-6])-int(metal))
    com[-7]=str(int(com[-7])-int(nonBioDeg))
    com[-8]=str(int(com[-8])-int(bioDeg))
    db.users['leftcornerz@gmail.com']=tuple(com)
    lis=list(db.users[email])
    lis[-2]=str(int(lis[-2])+int(bioDeg)*8+int(nonBioDeg)*11+int(metal)*9+int(electronic)*6+int(medical)*7)
    lis[-3]=str(int(lis[-3])+int(bioDeg)+int(nonBioDeg)+int(metal)+int(electronic)+int(medical))
    lis[-4]=str(int(lis[-4])+int(medical))
    lis[-5]=str(int(lis[-5])+int(electronic))
    lis[-6]=str(int(lis[-6])+int(metal))
    lis[-7]=str(int(lis[-7])+int(nonBioDeg))
    lis[-8]=str(int(lis[-8])+int(bioDeg))
    db.users[email]=tuple(lis)
    db.save()
    comOrderSuccessMail(email)
    return render_template("comconfirmationpopup.html")

@app.route('/companyLogin.html')
def companyLoginPage():
	return render_template("companyLogin.html")

@app.route('/companyRegister.html')
def companyRegister():
	return render_template("companyRegister.html")

@app.route('/companyforget.html')
def companyPassReset():
	return render_template("companyforget.html")

@app.route('/forgetpopup.html',methods=['POST'])
def companyResetPopup():
	email=request.form['userName']
	password=request.form['userPass']
	if email not in db.users:
		flash("Please Enter Valid Email ID")
		return redirect(url_for('companyPassReset'))
	lis=list(db.users[email])
	lis[0]=str(password)
	db.users[email]=tuple(lis)
	db.save()
	passResetMail(db.users[email][1],email)
	return render_template('forgetpopup.html')

@app.route('/companyRegPopUp.html',methods=['POST','GET'])
def companyRegisterValue():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    confirm_password=request.form['conPass']
    phone_number=request.form['phone']
    address=request.form['address']
    postalcode=request.form['code']
    tandc=request.form['tick']
    bioDeg,nonBioDeg,metal,electronic,medical,totalWaste, points=0,0,0,0,0,0,0
    if request.method=='POST' and request.form['password']==request.form['conPass']:
        if db.add_user(email, password, name, phone_number, address, bioDeg,nonBioDeg,metal,electronic,medical,totalWaste,points)==-1:
            flash("User already Exist")
            return redirect(url_for('companyRegister'))
        sendSuccessReg(name,email)
    else:
        flash("Password must be same")
        return redirect(url_for('companyRegister'))
    return render_template("companyRegPopUp.html")

@app.route('/popupreg.html',methods=['POST','GET'])
def userRegisterValue():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    confirm_password=request.form['conPass']
    phone_number=request.form['phone']
    address=request.form['address']
    postalcode=request.form['code']
    tandc=request.form['tick']
    bioDeg,nonBioDeg,metal,electronic,medical,totalWaste, points=0,0,0,0,0,0,0
    if request.method=='POST' and request.form['password']==request.form['conPass']:
        if db.add_user(email, password, name, phone_number, address, bioDeg,nonBioDeg,metal,electronic,medical,totalWaste,points)==-1:
            flash("User already Exist")
            return redirect(url_for('register'))
        sendSuccessReg(name,email)
        return redirect(url_for('popup'))
    else:
        flash("Password must be same")
        return redirect(url_for('register'))
    return render_template("popupreg.html")
    
@app.route('/login.html')
def loginPage():
    return render_template("login.html")
    
if __name__=="__main__":
    app.run(debug=True)
