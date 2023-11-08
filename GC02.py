hours,minutes=map(int,input("Time: ").split(':'));meridian=input("AM or PM: ");print('0'*((hours%12)+12*(meridian=="PM")<10),(hours%12)+12*(meridian=="PM"),':','0'*(minutes<10),minutes,sep='')
# easy one-liner (192B/192C)
