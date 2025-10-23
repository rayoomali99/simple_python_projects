salary = int(input("what is the monthly salary in SAR"))
hours_per_week =int(input("how many hours do you work per week?"))
remote =input("is it remote? (yes/no): ")
growth =input("are there learning/growth opportunities ? (yes/no):")

score = 0

if salary >= 8000:
    score += 2
elif salary >= 5000:
    score += 1

if hours_per_week <= 40:
    score += 2
if hours_per_week <=50:
    score += 1

if remote.lower() == "yes":
    score += 2

if growth.lower() == "yes":
    score += 2

if score >=6 :
    print("take it,queen!")
elif 4 <= score <6:
    print ("think twice,princess.....")
else:
    print("run.now.")