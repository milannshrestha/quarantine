#!/usr/bin/env python3

import argparse
import requests

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--email", required=True,
        help="Email Address")
args = vars(ap.parse_args())

res = requests.get('http://emailrep.io/{}'.format(args["email"]))
intxt = res.text
data = res.json()

print (intxt)

