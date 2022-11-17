import trackerclass

# List of tracking numbers - just paste yours.
tr_numberlist = ['Trackingnumber1', 'Trackingnumber2']

tr = trackerclass.Tracker()

for n in tr_numberlist:
    print(n, tr.getstatus(n)['status'])
