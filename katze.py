meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey"
    "LOL": "Komik bir şeye verilen cevap"
    "ROFL":"Bir şakaya karşılık cevap"
    "SHEESH":"Onaylamak"
    "CREEPY":"korkunç"
    "GG":"İyi Oyun"
    "EZ":"Kolay/kolaydı"
    "İDC":"Umursamıyorum"
    "İDK":"Bilmiyorum"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Böyle bir kelime yok ki")
