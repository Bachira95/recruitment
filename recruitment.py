def main():
	#write your code here
	skills=["Python", "C++", "JavaScript","Meeting", "Leeting", "Eating" ]
	cv={}
	name=input("Enter your name: ")
	cv["name"]=name
	age=int(input("Enter your age: "))
	cv["age"]=age
	expYears=int (input("how many years of experience you have? "))
	cv["experience"]=expYears
	cv["skills"]=[]
	x=1
	for i in skills:
		print(str(x)+"-"+i)
		x+=1
	skl=int (input("Choose a skill from above by entering its number: "))
	cv["skills"].append(skills[skl-1])
	skl2=int (input("Choose a skill from above by entering its number: "))
	cv["skills"].append(skills[skl2-1])
	
	if (age>=25 and age<=40 and "Eating"in cv["skills"]and expYears>5):
		print ("You have been accepted")
	else :
		print("You have been rejected")

if __name__ == '__main__':
	main()
