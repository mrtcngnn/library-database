from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

from sqlalchemy.sql.elements import Null
islem_yapilan_kullanici=""
app = Flask(__name__)
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asy@localhost/'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
an = datetime.now()
gecici_id=0
uye=1
class Kitap(db.Model):
    __tablename__ = 'Kitap'
    KitapID= db.Column(db.Integer,unique=True,primary_key=True,nullable=False)
    YazarID= db.Column(db.Integer,nullable=False)
    YayinEviID= db.Column(db.Integer,nullable=False)    
    Isim= db.Column(db.String(30),unique=True,nullable=False)    
    BaskiNo= db.Column(db.Integer,nullable=False) 
    SayfaSayisi= db.Column(db.Integer,nullable=False)          
    def __init__(self,KitapID,YazarID, YayinEviID, Isim,BaskiNo,SayfaSayisi):
        self.KitapID= KitapID
        self.YazarID=YazarID
        self.YayinEviID=YayinEviID       
        self.Isim=Isim       
        self.BaskiNo=BaskiNo
        self.SayfaSayisi=SayfaSayisi
class YayinEvi(db.Model):
    __tablename__ = 'YayinEvi'   
    YayinEviID= db.Column(db.Integer,primary_key=True,nullable=False)     
    Isim= db.Column(db.String(30),unique=True,nullable=False) 
    KurulusTarihi= db.Column(db.String(30),nullable=False)
    KitapSayisi= db.Column(db.Integer,nullable=False)             
    def __init__(self, YayinEviID,Isim,KurulusTarihi,KitapSayisi):
        self.YayinEviID=YayinEviID       
        self.Isim=Isim
        self.KurulusTarihi=KurulusTarihi
        self.KitapSayisi=KitapSayisi    
class Yazar(db.Model):
    __tablename__ = 'Yazar'   
    YazarID= db.Column(db.Integer,primary_key=True,nullable=False)     
    Isim= db.Column(db.String(30),unique=True,nullable=False) 
    DogumTarihi= db.Column(db.String(30),nullable=False)
    KitapSayisi= db.Column(db.Integer,nullable=False)             
    def __init__(self, YayinEviID,Isim,DogumTarihi,KitapSayisi):
        self.YayinEviID=YayinEviID       
        self.Isim=Isim
        self.DogumTarihi=DogumTarihi
        self.KitapSayisi=KitapSayisi   
class Masa(db.Model):
    __tablename__ = 'Masa'   
    MasaID= db.Column(db.Integer,primary_key=True,unique=True,nullable=False)     
    S8_10= db.Column(db.Boolean,nullable=False) 
    S10_12= db.Column(db.Boolean,nullable=False)
    S12_14= db.Column(db.Boolean,nullable=False)
    S14_16= db.Column(db.Boolean,nullable=False)
    S16_18= db.Column(db.Boolean,nullable=False)
    S18_20= db.Column(db.Boolean,nullable=False)
            
    def __init__(self,MasaID, S8_10,S10_12,S12_14,S14_16, S16_18,S18_20,):
        self.MasaID=MasaID
        self.S8_10=S8_10       
        self.S10_12=S10_12       
        self.S12_14=S12_14
        self.S14_16=S14_16
        self.S16_18=S16_18  
        self.S18_20=S18_20    
class Iletisim(db.Model):
    __tablename__ = 'Iletisim'          
    uyeID= db.Column(db.Integer,unique=True,nullable=False)    
    Adres= db.Column(db.String(200),nullable=False) 
    E_Mail= db.Column(db.String(30),primary_key=True,unique=True,nullable=False)  
    TelNo= db.Column(db.Integer,nullable=False)          
    def __init__(self, uyeID,Adres,E_Mail,TelNo):
        self.uyeID=uyeID       
        self.Adres=Adres
        self.E_Mail=E_Mail 
        self.TelNo=TelNo
class Message(db.Model):
    __tablename__ = 'Message'          
    MesageID= db.Column(db.Integer,primary_key=True,unique=True,nullable=False)  
    kitapID=  db.Column(db.Integer,nullable=False) 
    fromID= db.Column(db.Integer,nullable=False) 
    toID= db.Column(db.Integer,nullable=False)  
    mesage= db.Column(db.String(300),nullable=False)          
    def __init__(self, MesageID,kitapID,fromID,toID,mesage):
        self.MesageID=MesageID       
        self.kitapID=kitapID
        self.fromID=fromID 
        self.toID=toID  
        self.mesage=mesage        
class AktifUser(db.Model):
    __tablename__ = 'AktifUser'          
    fromID= db.Column(db.Integer,primary_key=True,nullable=False)  
    kitapID=  db.Column(db.Integer,nullable=False)     
    toID= db.Column(db.Integer,nullable=False)           
    def __init__(self,fromID ,kitapID,toID,):               
        self.kitapID=kitapID
        self.fromID=fromID 
        self.toID=toID                   
      

class Calisan(db.Model):
    __tablename__ = 'Calisan'          
    uyeID= db.Column(db.Integer,unique=True,primary_key=True,nullable=False) 
    Sifre= db.Column(db.String(30),nullable=False)
    IseBaslama= db.Column(db.String(30),nullable=False)
    Isim= db.Column(db.String(30),unique=True,nullable=False) 
    DogumTarihi= db.Column(db.String(30),nullable=False)
    SigortaNo= db.Column(db.String(30),unique=True,nullable=False)
    Maas= db.Column(db.Integer,nullable=False) 
    Gorev= db.Column(db.String(30),nullable=False)
    Vardiya= db.Column(db.Boolean,nullable=False)            
    def __init__(self, uyeID,Sifre,IseBaslama,Isim,DogumTarihi,SigortaNo,Maas,Gorev,Vardiya):
        self.uyeID=uyeID 
        self.Sifre=Sifre       
        self.IseBaslama=IseBaslama
        self.Isim=Isim
        self.DogumTarihi=DogumTarihi   
        self.SigortaNo=SigortaNo       
        self.Maas=Maas
        self.Gorev=Gorev
        self.Vardiya=Vardiya 

class Uye(db.Model):
    __tablename__ = 'Uye'          
    uyeID= db.Column(db.Integer,unique=True,primary_key=True,nullable=False) 
    Sifre= db.Column(db.String(30),nullable=False)
    UyelikBaslama= db.Column(db.String(30),nullable=False)
    UyelikBitis= db.Column(db.String(30),nullable=False)
    Isim= db.Column(db.String(30),unique=True,nullable=False) 
    DogumTarihi= db.Column(db.String(30),nullable=False)
    CezaPuani= db.Column(db.Integer,nullable=False)
    OduncKitapSayisi= db.Column(db.Integer,nullable=False)              
    def __init__(self, uyeID,Sifre,UyelikBaslama,UyelikBitis,Isim,DogumTarihi,CezaPuani,OduncKitapSayisi):
        self.uyeID=uyeID  
        self.Sifre=Sifre     
        self.UyelikBaslama=UyelikBaslama
        self.UyelikBitis=UyelikBitis
        self.Isim=Isim
        self.DogumTarihi=DogumTarihi   
        self.CezaPuani=CezaPuani       
        self.OduncKitapSayisi=OduncKitapSayisi
class Odunc(db.Model):
    __tablename__ = 'Odunc'   
    OduncID= db.Column(db.Integer,unique=True,primary_key=True,nullable=False)       
    uyeID= db.Column(db.Integer,unique=True,nullable=False) 
    KitapID= db.Column(db.Integer,unique=True,nullable=False)
    AlmaTarihi= db.Column(db.String(30),nullable=False)
    VermeTarihi= db.Column(db.String(30),nullable=True)
    Yorum= db.Column(db.String(200),nullable=True) 
    YorumPuan= db.Column(db.Integer,nullable=True)                
    def __init__(self, OduncID,uyeID,KitapID,AlmaTarihi,UyVermeTarihielikBitis,Yorum,YorumPuan):
        self.OduncID=OduncID 
        self.uyeID=uyeID           
        self.KitapID=KitapID
        self.AlmaTarihi=AlmaTarihi
        self.UyVermeTarihielikBitis=UyVermeTarihielikBitis
        self.Yorum=Yorum   
        self.YorumPuan=YorumPuan              
                                                  
@app.route('/')  
def home():    
    if(request.method == "GET"):
        return render_template('Home.html')                 
@app.route('/Giris', methods=['GET', 'POST'])  
def Giris():        
    if(request.method == "POST"):
        Kulanici = request.form.get("kullaniciadi")
        if Kulanici.isdigit()==False:
            return render_template('Home.html',mesaj="hatali id")  
        sifre=request.form.get("sifre")
        uye=db.session.query(Uye.uyeID).filter(Uye.uyeID==Kulanici).first()  
              
        if uye is not None:
            data=db.session.query(Uye.Sifre).filter(Uye.uyeID==Kulanici).first()
            data=str(data)           
            data=data[2:len(data)-3]             
            if data==sifre: 
                if Kulanici=="0":
                     return render_template('SistemYoneticisi.html',mesaj="")  
                datum=db.session.query(AktifUser.toID).first()                
                datum=str(datum)
                uye=str(uye)
                datum=int(datum[1:len(datum)-2])  
                uye=int(uye[1:len(uye)-2] )                                         
                personel =AktifUser.query.filter_by(toID=datum).first()  
                personel.fromID = uye                    
                db.session.commit()   
                data=db.session.query(Message.mesage).filter(Message.toID==Kulanici).first()
                if data is not None:                    
                    nmbr=Message.query.filter_by(toID=Kulanici).first()                   
                    data=str(data)  
                    data=data[2:len(data)-3]     
                    db.session.delete(nmbr)
                    db.session.commit()                      
                    return render_template('UyeIslem.html',mesaj="Hosgeldiniz "+str(Kulanici)+" \U0001F917	",ileti=data)
                else:
                    return render_template('UyeIslem.html',mesaj="Hosgeldiniz "+str(Kulanici)+" \U0001F917	",ileti="")    
            else:               
                return render_template('Home.html',mesaj="hatali Sifre")               
        return render_template('Home.html',mesaj="hatali id")    
@app.route('/returnGiris', methods=['GET', 'POST'])  
def returnGiris():     
    return render_template('UyeIslem.html',mesaj="hosgeldiniz",ileti="")              
@app.route('/Kayit', methods=['GET', 'POST'])
def Kayit():          
    if(request.method == "POST"):        
        return render_template('YeniUyeKaydi.html')   
@app.route('/KayitOl', methods=['GET', 'POST'])
def KayitOl():      
    if(request.method == "POST"): 
        isim = request.form.get("isim")        
        email=request.form.get("email")
        cepno = request.form.get("cepno")      
        dogumtarihi=request.form.get("dogumtarihi")    
        adres=request.form.get("adres")  
        data=db.session.query(Iletisim.uyeID).filter(Iletisim.E_Mail==email).first()  
        if data is not None:
            return render_template('YeniUyeKaydi.html',mesaj="bu e-mail zaten alınmış")  
        top=int(db.session.query(Uye.uyeID).count())+1
        date1=""+str(an.day)+"/"+str(an.month)+"/"+str(an.year)
        date2=""+str(an.day)+"/"+str(an.month)+"/"+str(an.year+3)               
        data=Uye( top,0,date1,date2,isim,dogumtarihi,0,0)
        db.session.add(data)
        db.session.commit()
        data2=Iletisim( top,adres,email,cepno)
        gecici_id=top        
        
        db.session.add(data2)
        db.session.commit()        
        return render_template('IdveSifre.html',mesaj="sisteme hos geldiniz uye idniz:"+str(gecici_id)+"\nSifrenizi 8 karekterden fazla olmalı")
@app.route('/Sifre', methods=['GET', 'POST'])
def Sifre():      
    if(request.method == "POST"): 
        sifre = request.form.get("sifre")
        top=int(db.session.query(Uye.uyeID).count())
        if len(sifre)<8:
           return render_template('IdveSifre.html',mesaj="Sifreniz 8 karekterden fazla degil tekrar giriniz\nuye idniz:"+str(top))           
        personel =Uye.query.filter_by(uyeID=top).first()  
        personel.Sifre = sifre                    
        db.session.commit()       
        return render_template('Home.html')        
@app.route('/Sorgu', methods=['GET', 'POST'])
def Sorgu():      
    if(request.method == "POST"): 
        kitap=request.form.get("isim")
        data=db.session.query(Kitap.KitapID).filter(Kitap.Isim==kitap).first()        
        if data is not None:
            data=str(data)
            data=int(data[1:len(data)-2]) 
            datum=db.session.query(AktifUser.fromID).first() 
            print(datum)              
            datum=str(datum)                
            datum=int(datum[1:len(datum)-2]) 
            print(datum)  
            data2=db.session.query(Odunc.uyeID).filter(Odunc.KitapID==data).first()
            dataKontrol=str(db.session.query(Odunc.VermeTarihi).filter(Odunc.KitapID==data).all())
            if (data2 is  None) or (dataKontrol==False) :                              
                top=int(db.session.query(Odunc.uyeID).count())+1               
                date1=""+str(an.day)+"/"+str(an.month)+"/"+str(an.year)
                data2=Odunc( top,datum,data,date1,None,None,None) 
                db.session.add(data2)
                db.session.commit()   
                if an.day>20:
                    date2=""+str(an.day-20)+"/"+str(an.month+1)+"/"+str(an.year) 
                else :
                    date2=""+str(an.day+10)+"/"+str(an.month)+"/"+str(an.year) 
                personel =Uye.query.filter_by(uyeID=datum).first()  
                personel.OduncKitapSayisi = personel.OduncKitapSayisi+1                                     
                db.session.commit()              
                return render_template('OduncAlmaP.html',tarih1=date1,tarih2=date2)           
            else :
                data2=str(data2)
                data2=int(data2[1:len(data2)-2]) 
                print(datum)  
                personel =AktifUser.query.filter_by(fromID=datum).first()  
                personel.toID = data2   
                personel.kitapID = data                    
                db.session.commit()       
                return render_template('OduncAlmaN.html')  
        return render_template('UyeIslem.html',mesaj="bu kitap yok")   
@app.route('/Mesaj', methods=['GET', 'POST'])
def Mesaj():      
    if(request.method == "POST"): 
        mesaj=request.form.get("mesaj")
        datum=db.session.query(AktifUser.toID).first()                
        datum=str(datum)                
        datum=int(datum[1:len(datum)-2]) 
        personel =AktifUser.query.filter_by(toID=datum).first()
        nmbr=int(db.session.query(Message.MesageID).count())+1
        data=Message(nmbr,personel.kitapID,personel.fromID,personel.toID,mesaj)       
        db.session.add(data)
        db.session.commit()        
        return render_template('UyeIslem.html',mesaj="")  
@app.route('/Saat', methods=['GET', 'POST'])
def Saat():      
    if(request.method == "POST"): 
        saat=str(request.form.get("saat")) 
        if saat.isdigit():
            saat=int(saat)
        else:
            return render_template('UyeIslem.html',mesaj="saat seçiniz")                    
        data=db.session.query(Masa.MasaID).filter_by(S8_10=False).first()
        if saat==10:            
            data=db.session.query(Masa.MasaID).filter_by( S10_12=False).first()         
        elif saat==12:
            data=db.session.query(Masa.MasaID).filter_by(S12_14=False).first()
        elif saat==14:
            data=db.session.query(Masa.MasaID).filter_by(S14_16=False).first()
        elif saat==16:
            data=db.session.query(Masa.MasaID).filter_by(S16_18=False).first()
        elif saat==18:
            data=db.session.query(Masa.MasaID).filter_by(S18_20=False).first()               
        if  data is None:
            return render_template('UyeIslem.html',mesaj="seçtiğiniz saatte bos masa yok")
        else :
            data=str(data)                
            data=int(data[1:len(data)-2]) 
            MasaTutma =Masa.query.filter_by(MasaID=data).first()
            print(data)
            if saat==8:
                MasaTutma.S8_10=True        
            elif saat==10:
                MasaTutma.S10_12=True
            elif saat==12:
                MasaTutma.S12_14=True
            elif saat==14:
                MasaTutma.S14_16=True
            elif saat==16:
               MasaTutma.S16_18=True
            elif saat==18:
                MasaTutma.S18_20=True        
        db.session.commit()  
              
        return render_template('Rezervasyon.html',mesaj=str(saat)+"-"+str(saat+2)+" saatleri için "+str(data)+". masa sizin için ayrılmıştır")          
@app.route('/Yorum', methods=['GET', 'POST'])
def Yorum():       
    return render_template('Yorum.html',mesaj="")
 
@app.route('/Yorumyapma', methods=['GET', 'POST'])
def Yorumyapma():     
    if(request.method == "POST"): 
        kitapismi=request.form.get("kitapismi")
        mesaj=request.form.get("mesaj")
        age=request.form.get("age")
        data=db.session.query(Kitap.KitapID).filter(Kitap.Isim==kitapismi).first()
        if data is None:
            return render_template('Yorum.html',mesaj="Böyle bir kitap kütüphanemizde yok")
        data=str(data)
        data=int(data[1:len(data)-2])  
        oduncler=db.session.query(Odunc.uyeID).filter(Odunc.KitapID==data).all() 
        if oduncler is None:
            return render_template('Yorum.html',mesaj="Almadığınız kitabı değerlendiremezsiniz")
        oduncler=str(oduncler)
        datum=db.session.query(AktifUser.toID).first()                
        datum=str(datum)                
        datum=datum[1:len(datum)-2]         
        if datum in oduncler:
            datum=int(datum)
            oduncYorum =Odunc.query.filter_by(KitapID=data).first()
            oduncYorum.Yorum=mesaj
            oduncYorum.YorumPuan=int(age)             
            db.session.commit()
            return render_template('UyeIslem.html',mesaj="")
        return render_template('Yorum.html',mesaj="Almadığınız kitabı değerlendiremezsiniz") 
@app.route('/sistemdon', methods=['GET', 'POST'])
def sistemdon():                                    
    return render_template('SistemYoneticisi.html',mesaj="")        
@app.route('/CalisanEkle', methods=['GET', 'POST'])
def CalisanEkle():                                    
    return render_template('CalisanEkleme.html',mesaj="") 
@app.route('/CalisanEkleD', methods=['GET', 'POST'])
def CalisanEkleD():
    if(request.method == "POST"):
        isim=request.form.get("isim") 
        if isim=="":
             return render_template('CalisanEkleme.html',mesaj="isim bos")
        dogumtarihi=request.form.get("dogumtarihi")
        if dogumtarihi=="":
             return render_template('CalisanEkleme.html',mesaj="dogum tarihi bos")
        telefon=request.form.get("telefon")
        if telefon=="":
             return render_template('CalisanEkleme.html',mesaj="telefon bos")
        email=request.form.get("email")
        if email=="":
             return render_template('CalisanEkleme.html',mesaj="email bos")
        deger=db.session.query(Iletisim.E_Mail).filter(Iletisim.E_Mail==email).first()
        if deger is not None:
             return render_template('CalisanEkleme.html',mesaj="eposta var")
        sigortano=request.form.get("sigortano")
        if sigortano=="":
             return render_template('CalisanEkleme.html',mesaj="sigortano bos")
        maas=request.form.get("maas")
        if maas=="":
             return render_template('CalisanEkleme.html',mesaj="maas bos")
        if maas.isdigit()==False:
             return render_template('CalisanEkleme.html',mesaj="maas sayi olmalı") 
        maas=int(maas)         
        gorev=request.form.get("gorev")
        if gorev=="":
             return render_template('CalisanEkleme.html',mesaj="gorev bos")
        vardiya=request.form.get("vardiya")
        adres=request.form.get("adres")
        if adres=="":
             return render_template('CalisanEkleme.html',mesaj="adre bos")
        vardiyaDeger=True
        if vardiya=="1":
            vardiya=False            
        maas=request.form.get("maas")
        top=int(db.session.query(Calisan.uyeID).count())+71
        sifrenmbr=random.randint(1,100)
        sifre=str(top)+"Sifrec"+str(sifrenmbr)        
        date1=""+str(an.day)+"/"+str(an.month)+"/"+str(an.year) 
        data=Calisan(top,sifre,date1,isim,dogumtarihi,sigortano,maas,gorev,vardiyaDeger)
        db.session.add(data)
        db.session.commit()  
        data=Iletisim(None,adres,email,telefon,top)   
        db.session.add(data)
        db.session.commit()      
        return render_template('SistemYoneticisi.html',mesaj="")      
@app.route('/CezaPuaniVer', methods=['GET', 'POST'])
def CezaPuaniVer():
    deger=db.session.query(Odunc.uyeID,Odunc.AlmaTarihi).filter(Odunc.VermeTarihi==None).all()        
    if deger is None:                            
        return render_template('CezaPuaniVer.html',mesaj="ceza verilecek herhangi biri yok",control="")  
    return render_template('CezaPuaniVer.html',mesaj=deger)    

@app.route('/CezaPuaniVerD', methods=['GET', 'POST'])
def CezaPuaniVerD():      
    if(request.method == "POST"): 
        id=int(request.form.get("id")) 
        deger=db.session.query(Uye.uyeID).filter(Uye.uyeID==id).first() 
        if deger is None:
            deger=db.session.query(Odunc.uyeID,Odunc.AlmaTarihi).filter(Odunc.VermeTarihi==None).all()             
            return render_template('CezaPuaniVer.html',mesaj=deger) 
        oduncYorum =Uye.query.filter_by(uyeID=id).first()
        oduncYorum.CezaPuani= oduncYorum.CezaPuani+1
        db.session.commit()  
        return render_template('SistemYoneticisi.html',mesaj="")
@app.route('/KitapEkle', methods=['GET', 'POST'])
def KitapEkle():                                   
    return render_template('KitapEkle.html',mesaj="")              
@app.route('/KitapEkleD', methods=['GET', 'POST'])
def KitapEkleD():    
    if(request.method == "POST"):  
        yazarisim=request.form.get("yazarisim")
        if yazarisim=="":
            return render_template('KitapEkle.html',mesaj="yazar ismini giriniz")          
        deger1=db.session.query(Yazar.YazarID).filter(Yazar.Isim==yazarisim).first()  
        if deger1 is None:
            return render_template('KitapEkle.html',mesaj="böyle bir yazar yok")
        deger1=str(deger1)
        deger1=int(deger1[1:len(deger1)-2])     
        yayineviisim=request.form.get("yayineviisim")
        if yayineviisim=="":
            return render_template('KitapEkle.html',mesaj="yayıenevi ismini giriniz")         
        deger2=db.session.query(YayinEvi.YayinEviID).filter(YayinEvi.Isim==yayineviisim).first()  
        if deger2 is None:
            return render_template('KitapEkle.html',mesaj="böyle bir yayınevi yok")
        deger2=str(deger2)
        deger2=int(deger2[1:len(deger2)-2])
        isim=request.form.get("isim")
        if isim=="":
            return render_template('KitapEkle.html',mesaj="isim bos") 
        baskino=request.form.get("baskino")
        if baskino.isdigit()==False:
            return render_template('KitapEkle.html',mesaj="baski no sadece sayı olmalı") 
        baskino=int(baskino)       
        sayfasayisi=request.form.get("sayfasayisi")
        if sayfasayisi.isdigit()==False:
            return render_template('KitapEkle.html',mesaj="sayfa sayisi  sadece sayı olmalı") 
        sayfasayisi=int(sayfasayisi) 
        top=int(db.session.query(Kitap.KitapID).count())+1
        data=Kitap(top,deger1,deger2,isim,baskino,sayfasayisi)  
        db.session.add(data)
        db.session.commit()  
        yazarA =Yazar.query.filter_by(YazarID=deger1).first()
        yazarA.KitapSayisi= yazarA.KitapSayisi+1
        db.session.commit() 
        YayinEviA =YayinEvi.query.filter_by(YayinEviID=deger2).first()
        YayinEviA.KitapSayisi= YayinEviA.KitapSayisi+1
        db.session.commit()
        return render_template('SistemYoneticisi.html',mesaj="") 
@app.route('/YazarEkleme', methods=['GET', 'POST'])
def YazarEkleme():                                     
    return render_template('YazarEkleme.html',mesaj="") 
@app.route('/YazarEklemeD', methods=['GET', 'POST'])
def YazarEklemeD():      
    if(request.method == "POST"):  
        isim=request.form.get("isim")
        if isim=="":
            return render_template('YazarEkleme.html',mesaj="isim bos") 
        dogumtarihi=request.form.get("dogumtarihi") 
        if dogumtarihi=="":
            return render_template('YazarEkleme.html',mesaj="dogum tarihi bos")   
        top=int(db.session.query(Yazar.YazarID).count())+1
        data=Yazar(top,isim,dogumtarihi,0)  
        db.session.add(data)
        db.session.commit()                               
        return render_template('SistemYoneticisi.html',mesaj="")      
@app.route('/YayineviEkle', methods=['GET', 'POST'])
def YayineviEkle():                                    
    return render_template('YayineviEkle.html',mesaj="") 
@app.route('/YayineviEkleD', methods=['GET', 'POST'])
def YayineviEkleD():      
    if(request.method == "POST"):  
        isim=request.form.get("isim")
        if isim=="":
            return render_template('YazarEkleme.html',mesaj="isim bos")
        kurulustarihi=request.form.get("kurulustarihi")   
        if kurulustarihi=="":
            return render_template('YazarEkleme.html',mesaj="kurulus tarihi bos")
        top=int(db.session.query(Yazar.YazarID).count())+1
        data=YayinEvi(top,isim,kurulustarihi,0)  
        db.session.add(data)
        db.session.commit()                               
        return render_template('SistemYoneticisi.html',mesaj="")     
@app.route('/IadeEtme', methods=['GET', 'POST'])
def IadeEtme():                                   
    return render_template('IadeEtme.html',mesaj="")  
@app.route('/IadeEtmeD', methods=['GET', 'POST'])
def IadeEtmeD():      
    if(request.method == "POST"): 
        kullaniciid=request.form.get("kullaniciid")
        if kullaniciid.isdigit==False:
            return render_template('IadeEtme.html',mesaj="yazar id sadece sayı olmalı")  
        kullaniciid=int(kullaniciid)    
        deger=db.session.query(Odunc.uyeID).filter(Odunc.uyeID==kullaniciid).first()  
        if deger is None:
            return render_template('IadeEtme.html',mesaj="böyle bir kullanici yok")
        kitapismi=request.form.get("kitapismi") 
        data=db.session.query(Kitap.KitapID).filter(Kitap.Isim==kitapismi).first()        
        if data is not None:
            data=str(data)
            data=int(data[1:len(data)-2])                          
            data2=db.session.query(Odunc.OduncID).filter(Odunc.KitapID==data and Odunc.uyeID==kullaniciid).first()
            if data2 is not  None :
                data2=str(data2)
                data2=int(data2[1:len(data2)-2]) 
                Guncelleme =Odunc.query.filter_by(OduncID=data2).first()
                Guncelleme.VermeTarihi =""+str(an.day)+"/"+str(an.month)+"/"+str(an.year) 
                db.session.commit()
                uyeGuncelleme =Uye.query.filter_by(uyeID=kullaniciid).first()
                uyeGuncelleme.OduncKitapSayisi= uyeGuncelleme.OduncKitapSayisi-1
                db.session.commit() 
                return render_template('SistemYoneticisi.html',mesaj="")
    return render_template('IadeEtme.html',mesaj="hatali iade")                                                   
if __name__ == '__main__':
    app.run()
