"""Using (not in, in + .upper(), .lower() together)"""
s = "Julian and Ricky are hanging out with friends this night"
print("JULIAN" in s.upper())#True,'cause firt, s.upper() works, then the search of "JULIAN" in s
print("julian"not in s.lower())#false, it's actually there