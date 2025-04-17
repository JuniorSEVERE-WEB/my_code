nomDuFichier = input("File name:").lower().strip()

if '.gif' in nomDuFichier:
  print("image/gif")
elif '.png' in nomDuFichier:
  print("image/png")
elif '.jpg' in nomDuFichier:
  print("image/jpg")
elif '.jpeg' in nomDuFichier:
  print("image/jpeg")
elif '.pdf' in nomDuFichier:
  print("application/pdf")
elif '.zip' in nomDuFichier:
  print("application/zip")  
elif '.txt' in nomDuFichier:
  print("text/plain")
else:
  print("application/octet-stream")            
