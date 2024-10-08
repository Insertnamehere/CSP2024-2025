ageInYears = int(input("Please enter you age in years:  "))

ageInWeeks = ageInYears * 56
ageInDays = ageInYears * 365
ageInDecades = ageInYears / 10
ageInMinutes = (ageInDays * 24) * 60

print('You have lived aproximatly:   ')
print(ageInDays, 'days.')
print(ageInDecades, 'decades.')
print(ageInWeeks, 'weeks')
print(ageInMinutes, 'minutes')