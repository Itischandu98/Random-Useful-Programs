months = {1:1, 2:4, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
days = {1:"Sunday" ,2:"Monday" , 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"friday", 0:"Saturday"}
date=(input("Enter the month and date in m/d format")).split("/")
print(f"The give date '{int(date[0])}/{int(date[1])}' is {days[(months[int(date[0])]+int(date[1])+6)%7]}")
