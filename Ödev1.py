'''
1. Tane sozluk olustur
2. Bu sozlugun icine 3 tane rakam ekle (keyler: rakam1, rakam2, rakam3)
3. if deyimiyle bu 3 rakam içerisinde ne buyugunu bul ve ekrana yazdir.
'''


dictionary = {"Mehmet Akif":37,
              "Cahit Sitki":35,
              "Hatice Zehra":21 
              }

if dictionary["Mehmet Akif"]>dictionary["Cahit Sitki"]:
  
    if dictionary["Cahit Sitki"]> dictionary["Hatice Zehra"]:
        print("Biggest => ", dictionary["Mehmet Akif"])
      
    elif dictionary["Cahit Sitki"]<dictionary["Hatice Zehra"]:
        print("Biggest => ", dictionary["Hatice Zehra"])

elif dictionary["Mehmet Akif"]<dictionary["Cahit Sitki"]:
  
    if dictionary["Cahit Sitki"]>dictionary["Hatice Zehra"]:
        print("Biggest => ", dictionary["Cahit Sitki"])
