def leapYear(start,end):
    startDate=start.split("/")
    endDate=end.split("/")
    startYear = int(startDate[2])
    endYear = int(endDate[2])

    leapYear=[]
    nonleapYear=[]

    for i in range(startYear,endYear+1):
        if (i%400==0 or i%100!=0) and i%4==0:
            leapYear.append(i)
        else:
            nonleapYear.append(i)
    print("Leap Years: ",end=" ")
    for j in range(len(leapYear)):
        if j==len(leapYear)-1:
            print(leapYear[j],end=".")
            print()
        else:
            print(leapYear[j],end=",")
    print("Non Leap Years: :",end=" ")
    for k in range(len(nonleapYear)):
        if k==len(nonleapYear)-1:
            print(nonleapYear[k],end=".")
        else:
            print(nonleapYear[k],end=",")
start=input("Enter start date: ")
end=input("Enter end date: ")

leapYear(start,end)