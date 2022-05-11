from flask import Flask,render_template,redirect,url_for,request,session,flash,json
import numpy as np
import pickle
app=Flask(__name__)


app.secret_key="lucky"
@app.route("/")
def home():
        return render_template("home.html")
@app.route('/predict',methods=['POST'])
def predict():
     if request.method == "POST":
         session.permanent = True
         vals=[]
         area_map={'Anupperpalayam': 60,
 'Avarampalayam': 36,
 'Avinashi Road': 56,
 'Bharathi Nagar': 0,
 'GN Mills': 21,
 'Ganapathy': 45,
 'Gandhipuram': 41,
 'K K Pudur': 15,
 'Kalapatti': 26,
 'Kalapatti road': 7,
 'Kalikkanaicken Palayam': 18,
 'Kallimadai': 40,
 'Kavundampalayam': 48,
 'Keeranatham': 38,
 'Koundampalayam': 42,
 'Kovaipudur': 11,
 'Kuniyamuthur': 20,
 'MULLAI NAGAR MARUTHAMALAI ROAD': 4,
 'Mettupalayam Road': 25,
 'NGGO Colony': 16,
 'Nallampalayam': 30,
 'Nanjundapuram': 39,
 'New Siddhapudur': 2,
 'New Thillai Nagar': 22,
 'Ondiputhur': 9,
 'P.N.Palayam': 28,
 'PN PUDHUR': 55,
 'Pappanaicken Pudur': 27,
 'Peelamedu': 43,
 'Peelamedu Pudur': 57,
 'Perur': 24,
 'Podanur': 47,
 'R.S.Puram': 51,
 'Race Course': 59,
 'Ramanathapuram': 37,
 'Ramnagar': 46,
 'Saibaba Colony': 52,
 'Saravanampatti': 44,
 'Saravannapatti': 6,
 'Selvapuram': 14,
 'Singanallur': 33,
 'Sowripalayam': 32,
 'Sridevi Nagar': 17,
 'Subramaniyampalayam': 12,
 'Sundarapuram': 19,
 'Sungam': 58,
 'TVS nagar': 29,
 'Tardeo': 34,
 'Tatabad': 49,
 'Telungupalayam': 1,
 'Thondamuthur': 23,
 'Thudiyalur': 3,
 'Thudiyalur Road': 8,
 'Town Hall': 13,
 'Trichy Road': 50,
 'Udayampalayam': 53,
 'Uppilipalayam': 54,
 'Vadavalli': 31,
 'Vedapatti': 5,
 'Vellakinar': 35,
 'Vilankurichi': 10}
         location_map={'Karjat': 0,'Bhavnagar': 1,'Rudrapur': 2,'Palghar': 3,'Junagadh': 4,'Durgapur': 5,'Ratnagiri': 6,
                       'Bharuch': 7,'Vapi': 8,'Neemrana': 9,'Bhiwadi': 10,'Valsad': 11,'Bhilai': 12,'Navsari': 13,'Asansol': 14,
                       'Vizianagaram': 15,'Tirunelveli': 16,'Haridwar': 17,'Mathura': 18,'Raigad': 19,'Meerut': 20,'Sindhudurg': 21,
                       'Bilaspur': 22,'Solan': 23,'Dhanbad': 24,'Bhopal': 25,'Aurangabad': 26,'Nellore': 27,'Hubli': 28,'Raipur': 29,
                       'Amravati': 30,'Ajmer': 31,'Dharuhera': 32,'Solapur': 33,'Kolhapur': 34,'Siliguri': 35,'Gwalior': 36,'Others': 37,
                       'Ahmednagar': 38,'Agra': 39,'Udupi': 40,'Aligarh': 41,'Jodhpur': 42,'Gandhinagar': 43,'Guntur': 44,'Anand': 45,
                       'Bahadurgarh': 46,'Belgaum': 47,'Indore': 48,'Jamshedpur': 49,'Margao': 50,'Rajkot': 51,'Palakkad': 52,'Madurai': 53,
                       'Sonipat': 54,'Kota': 55,'Vijayawada': 56,'Jabalpur': 57,'Pondicherry': 58,'Guwahati': 59,'Jalandhar': 60,'Allahabad': 61,
                       'Tirupati': 62,'Udaipur': 63,'Secunderabad': 64,'Vadodara': 65,'Visakhapatnam': 66,'Ghaziabad': 67,'Jaipur': 68,'Thrissur': 69,
                       'Patna': 70,'Faridabad': 71,'Bhubaneswar': 72,'Surat': 73,'Shimla': 74,'Varanasi': 75,'Mysore': 76,'Mangalore': 77,'Dehradun': 78,
                       'Nagpur': 79,'Coimbatore': 80,'Ernakulam': 81,'Ludhiana': 82,'Panchkula': 83,'Lucknow': 84,'Chandigarh': 85,'Kolkata': 86,'Kanpur': 87,
                       'Kottayam': 88,'Panaji': 89,'Jalgaon': 90,'Mohali': 91,'Pune': 92,'Kochi': 93,'Ranchi': 94,'Noida': 95,'Chennai': 96,'Bangalore': 97,
                       'Goa': 98,'Lalitpur': 99,'Mumbai': 100,'Maharashtra': 101,'Gurgaon': 102}
         posted_map = {'Owner': 0, 'Dealer': 1, 'Builder': 2}
         yes_map = {"Yes": 1, "No": 0}
         posted = request.form["posted"]
         vals.append(posted_map[posted])
         rera=request.form["rera"]
         vals.append(yes_map[rera])
         rooms=request.form["rooms"]
         vals.append(rooms)
         square_foot=request.form["foot"]
         vals.append(square_foot)
         ready=request.form["ready_to_move"]
         vals.append(yes_map[ready])
         resale=request.form["resale"]
         vals.append(yes_map[resale])
         city=request.form["city"]
         
         print(city)
         if(city=="Coimbatore"):
            with open("coimbatore_model.pkl","rb") as f:
                model=pickle.load(f)
            with open("coimbatore_scalar.pkl","rb") as f:
                scalar=pickle.load(f)
            location=request.form["area"]
            vals.append(area_map[location])
            vals1=vals
            vals=scalar.transform([vals])
            res=model.predict(vals)
            fvals=[]
            for i in area_map.keys():
                vals2=vals1
                vals2.pop()
                vals2.append(area_map[i])
                vals=scalar.transform([vals2])
                res=model.predict(vals)
                for val in res:
                    fvals.append(round(float(val),2))
                    
            
            if location=="Gandhipuram":
                factor=0.15
                res=res*factor+res
            elif(location=="R.S.Puram" or location=="Saibaba Colony"):
                 res+=10
            
         else:
             with open("my_model.pkl","rb") as f:
                model=pickle.load(f)
             with open("my_scalar.pkl","rb") as f:
                scalar=pickle.load(f)
             city=request.form["city"]
             vals.append(location_map[city])
             vals=scalar.transform([vals])
             res=model.predict(vals)
         for val in res:
             flash(f"The Price of the House is around {int(val)} Lacs","info")
         area_list=list(area_map.keys())
         if(city=="Coimbatore"):
            print(fvals)
            return render_template("index.html",result=[fvals,area_list])
         else:
            return render_template("index2.html")
        
if __name__=="__main__":
    app.run(debug=True)
