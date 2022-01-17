import qrcode

url="https://treasure-hunt-english-iut-rodez.000webhostapp.com/index.php" 
code = input("Code : ")
if len(code) == 5:
    code = code.upper()
    img = qrcode.make(f"{url}?code={code}")
    img.save(f"{code}.png")
    print("[QRcode] Successful generated")
else:
    print("[Error] code need to make 5 characters")