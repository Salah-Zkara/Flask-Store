import subprocess as sp
from server import db,Product,Message
def Show_Products():
	Products=Product.query.all()
	for prd in Products:
		print(str(prd.id)+"- "+prd.titre)
	print('\n')
def Add_Product():
	titre=input("Product Title: ")
	description=input("Product description: ")
	prix=float(input("Product price: "))
	image=input("Product image name: ")
	specs=input("Product specs: ")
	db.session.add(Product(titre=titre,description=titre,prix=prix,image=image,specs=specs))
	db.session.commit()
	print('\n')
def Edit_product(Id):
	Products=Product.query.all()
	for prd in Products:
		if(prd.id==Id) :
			prd.titre=input("Product Title: ")
			prd.description=input("Product description: ")
			prd.prix=float(input("Product price: "))
			prd.image=input("Product image name: ")
			prd.specs=input("Product specs: ")
			db.session.commit()
			return True
	return False
def Delete_product(Id):
	Products=Product.query.all()
	for prd in Products:
		if(prd.id==Id):
			Product.query.filter(Product.id == Id).delete()
			db.session.commit()
			return True
	return False
	
def Show_Messages():
	Messages=Message.query.all()
	for msg in Messages:
		print(str(msg.id)+"- "+"\nName: "+msg.nom+"\nEmail: "+msg.mail+"\nDate: "+str(msg.mdate)+"\nRate: "+str(msg.rate)+"/5"+"\nMessage: "+msg.message+"\n\n")
	print('\n\n')

def Delete_Message(Id):
	Messages=Message.query.all()
	for msg in Messages:
		if(msg.id==Id):
			Message.query.filter(Message.id == Id).delete()
			db.session.commit()
			return True
	return False


def main():
	sp.call('cls',shell=True)
	print("1)- Create DataBase\n2)- Products\n3)- Messages\n4)- Delete DataBase\n5)- Exit")
	n=input()
	while(n!='5') :
		if(n=='1') :
			db.create_all()
			print("DataBase Created Successfully !")
			for i in range(99999999):
				pass
			sp.call('cls',shell=True)
		elif(n=='2'):
			sp.call('cls',shell=True)
			#view_products()
			print("1)- View Products\n2)- Add New Product\n3)- Edit Product\n4)- Delete Product\n5)- Exit")
			n1=input()
			while(n1!='5') :
				if(n1=='1') :
					#view function
					sp.call('cls',shell=True)
					Show_Products()
					input("\nPress ENTRER !!")
					sp.call('cls',shell=True)
				elif(n1=='2'):
					#Add New Product function
					Add_Product()
					print("The Product Has Been Added Successfully !")
					for i in range(99999999):
						pass
					sp.call('cls',shell=True)
				elif(n1=='3'):
					#Edit Product function
					Show_Products()
					Id=int(input("Product ID to Edit: "))
					if(Edit_product(Id)==False) :
						sp.call('cls',shell=True)
						print("Product ID Not Found !")
						for i in range(99999999):
							pass
						sp.call('cls',shell=True)
					else:
						print("The Product Has Been Edited Successfully !")
						for i in range(99999999):
							pass
						sp.call('cls',shell=True)

				elif(n1=='4'):
					#Delete Product function
					sp.call('cls',shell=True)
					Show_Products()
					Id=int(input("Product ID to Delete: "))
					if(Delete_product(Id)==True) :
						print("The Product Has Been Deleted Successfully !")
						for i in range(99999999):
							pass
						sp.call('cls',shell=True)
					else:
						print("Product ID Not Found !")
						for i in range(99999999):
							pass
						sp.call('cls',shell=True)
				else:
					print("Please Enter Your Choice Correctly !!!")
					for i in range(99999999):
						pass
				print("1)- View Products\n2)- Add New Product\n3)- Edit Product\n4)- Delete Product\n5)- Exit")
				n1=input()
				sp.call('cls',shell=True)
				
		elif(n=='3'):
			sp.call('cls',shell=True)
			print("1)- View Messages\n2)- Delete Message\n3)- Exit")
			n2=input()
			sp.call('cls',shell=True)
			while(n2!='3') :
				if(n2=='1') :
					Show_Messages()
					input("\nPress ENTER !!")
					sp.call('cls',shell=True)
				elif(n2=='2'):
					#Delete Message function
					sp.call('cls',shell=True)
					Show_Messages()
					Id=int(input("Message ID to Delete: "))
					if(Delete_Message(Id)==True) :
						print("The Message Has Been Deleted Successfully !")
						for i in range(99999999):
							pass
						sp.call('cls',shell=True)
					else:
						print("Message ID Not Found !")
						for i in range(99999999):
							pass
						sp.call('cls',shell=True)
				else:
					print("Please Enter Your Choice Correctly !!!")
					for i in range(99999999):
						pass
				print("1)- View Messages\n2)- Delete Message\n3)- Exit")
				n2=input()
				sp.call('cls',shell=True)

		elif(n=='4'):
			db.drop_all()
			print("DataBase Deleted Successfully !")
			for i in range(99999999):
				pass
			sp.call('cls',shell=True)
		else:
			print("Please Enter Your Choice Correctly !!!")
			for i in range(99999999):
				pass
		sp.call('cls',shell=True)
		print("1)- Create DataBase\n2)- Products\n3)- Messages\n4)- Delete DataBase\n5)- Exit")
		n=input()


main()