happyFace = ":-)"
sadFace = ":-("

strInput = str(input())

happyCount = strInput.count(happyFace)
sadCount = strInput.count(sadFace)

if happyCount==0 or sadCount==0:
  print("none")
elif happyCount==sadCount:
  print("unsure")
elif happyCount>sadCount:
  print("happy")
else:
  print("sad")