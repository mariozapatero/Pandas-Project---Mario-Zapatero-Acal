def activities (i):
    if 'surf' in str(i).lower():
        return 'surfing'
    
    elif "wave" in str(i).lower():
        return 'surfing'
    
    elif "board" in str(i).lower():
        return 'surfing'
    
    
    elif "swim" in str(i).lower():
        return 'swimming'
    
    elif "snorkel" in str(i).lower():
        return 'swimming'
    
    elif "bath" in str(i).lower():
        return 'swimming'
    
    
    elif "diving" in str(i).lower():
        return 'diving'
    
    
    elif "fish" in str(i).lower():
        return 'fishing'
    
    
    elif "shark" in str(i).lower():
        return 'shark_activities'
    
    
    elif "boat" in str(i).lower():
        return 'sailing'
    
    elif "ship" in str(i).lower():
        return 'sailing'
    
    elif "ferry" in str(i).lower():
        return 'sailing'
    
    elif "raft" in str(i).lower():
        return 'sailing'
    
    elif "rowing" in str(i).lower():
        return 'sailing'
    
    elif "paddling" in str(i).lower():
        return 'sailing'
    
    elif "kayak" in str(i).lower():
        return 'sailing'
    
    elif "sail" in str(i).lower():
        return 'sailing'
    
    
    else:
        return "other"




def standar (i):
    if 'N' in str(i).upper() and "UNKNOWN" not in str(i).upper() and "NAN" not in str(i).upper():
        return 'N'
    
    elif 'Y' in str(i).upper():
        return "Y"
    
    else:
        return str(i).upper()




def unknown (i):
    if i == "M":
        return "UNKNOWN"
    elif i == "2017":
        return "UNKNOWN"
    else:
        return i




def unknown2 (i):
    if i == "NAN":
        return "UNKNOWN"
    else:
        return i