"""Using both .lower() and .upper()"""
s = "The Man Just Arrived Too Late To Save His Beloved"
#decrease the string
print(s.lower())
#increase it
print(s.upper())

#abstract
print(s.lower().startswith("the man")) #note that I call (.startswith(.lower""")) after (.lower(""))
print(s.upper().endswith("To Save"))


