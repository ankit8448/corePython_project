print("-"*50)
print("--------ıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı-------")
print("-"*50)
dic = {
	"Priyanshu":{"Hnd":56,"Math":89,"Sc":78,"Sst":69,"Eng":48},
	"Sonu":{"Hnd":69,"Math":85,"Sc":66,"Sst":51,"Eng":71},
	"Anmol":{"Hnd":66,"Math":49,"Sc":38,"Sst":61,"Eng":88},
	"Priya":{"Hnd":36,"Math":44,"Sc":49,"Sst":60,"Eng":90},
	"Ankit":{"Hnd":88,"Math":56,"Sc":88,"Sst":79,"Eng":88},
	"Mannu":{"Hnd":33,"Math":44,"Sc":58,"Sst":35,"Eng":53},
	"Aman":{"Hnd":23,"Math":31,"Sc":24,"Sst":31,"Eng":33}
}

r1 = {1:"Priyanshu",2:"Sonu",3:"Anmol",4:"Priya",5:"Ankit",6:"Mannu",7:"Aman"}

# How Extract Dict By Name
#------------------------------------------------------------
print("-"*50)


while True:
	rn = int(input("Enter Roll Number of Students : "))
	stn = r1.get(rn)

	if stn==None:
		print("Not Record Found!")
		print("Enter Correct roll Number!")


	else:
		st = dic.get(stn)
		v = st.values()
		tm = sum(v)
		per = tm/5
		print("-"*50)
		if per>=65:
			div = "First Division"
		elif per>=48:
			div = "Second Division"
		elif per>=35:
			div="Third Division"
		else:
			div = "Fail"

		#----------------------------------------
		print("Name of Student   :  ",stn)
		print("-"*50)
		print("Full marks        :   500")
		print("-"*50)
		print("Obtained Marks    :  ",tm)
		print("-"*50)
		print("Percentage        :  ",per)
		print("-"*50)
		print("Division          :  ",div)
		print("-"*50)
		if div=="Fail":
			print("Not Promoted\nNeeds Improvement!")
		else:
			print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")
			
		

	print("-"*50)
	loop = input("If Want Check The next Students of Result \nthen Press 1 \nExist Press 0 :")
	if loop=="1":
		continue
	else:
		break
