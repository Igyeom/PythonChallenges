data = [i.split(', ') for i in  """Alabama, AL
Alaska, AK
Arizona, AZ
Arkansas, AR
California, CA
Colorado, CO
Connecticut, CT
Delaware, DE
Florida, FL
Georgia, GA
Hawaii, HI
Idaho, ID
Illinois, IL
Indiana, IN
Iowa, IA
Kansas, KS
Kentucky, KY
Louisiana, LA
Maine, ME
Maryland, MD
Massachusetts, MA
Michigan, MI
Minnesota, MN
Mississippi, MS
Missouri, MO
Montana, MT
Nebraska, NE
Nevada, NV
New Hampshire, NH
New Jersey, NJ
New Mexico, NM
New York, NY
North Carolina, NC
North Dakota, ND
Ohio, OH
Oklahoma, OK
Oregon, OR
Pennsylvania, PA
Rhode Island, RI
South Carolina, SC
South Dakota, SD
Tennessee, TN
Texas, TX
Utah, UT
Vermont, VT
Virginia, VA
Washington, WA
West Virginia, WV
Wisconsin, WI
Wyoming, WY
District of Columbia, DC
American Samoa, AS
Guam, GU
Northern Mariana Islands, MP
Puerto Rico, PR
U.S. Virgin Islands, VI""".splitlines()]

name = input("Enter the name of your area: ")
for i in data:
  if i[0] == name:
    print(i[1])
    break
else:
  print("Invalid area.")
