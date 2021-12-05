happyFace = ":-)"
sadFace = ":-("

strInput = str(input())

happyCount = strInput.count(happyFace)
sadCount = strInput.count(sadFace)

if happyCount>sadCount:
  print("happy")
elif happyCount<sadCount:
  print("sad")
elif happyCount==0 or sadCount==0:
  print("none")
else:
  print("unsure")