def towers(w = 1, o = 3, s = 2, count: int = 3):
    if count > 1:
        towers(w, s, o, count - 1)
    
    print(f"{w} >> {o}")

    if count > 1:
      towers(s, o, w, count - 1)

towers()