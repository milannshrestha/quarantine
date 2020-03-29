import re
ip = input("Your public ip: ")
k = ("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")

z = re.match(k , ip) #validating IP address
if z:
        a = list(reversed(ip.split('.')))
        x, y  = int(a[1]), int(a[0])
        maths = (256 * x) + y
        new = ("{}.{}.{}".format(a[3], a[2], str(maths)))
        print ("Spoffed: {}".format(new))
else:
        print ("Invalid IP")
