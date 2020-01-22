# Module: A file with List of functions...

# Find your choice of music
def Music_Type(*usr_input):
    collection=["Indian", "Classical", "Folk", "Sufi", "Rock", "Pop", "Latest", "Bollywood"]
    for item in usr_input:
        if item in collection:
            your_choice = []
            your_choice.append(item)
            for choice in your_choice:
                print "%s Music is added to your playlist" % choice
        else:
            print "Your Music choice %s is not found" % item

# Find your choice of Fragrance
def Fragrance_type(*usr_input):
    collection=["Perfume", "Deo", "NoGas Deo", "Ittar", "Fruity", "Floral", "Oceanic", "Woody"]
    for item in usr_input:
        if item in collection:
          your_choice = []
          your_choice.append(item)
          for choice in your_choice:
             print "%s Fragrance is added to your Cart" % choice
        else:
          print "Your Fragrance choice %s is not found" % item




