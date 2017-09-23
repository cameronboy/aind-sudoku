from solution import *





def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    print('Before')
    print(display(values))
    #Getting the potential twins, those boxes wtih two values

    candidates = [box for box in values.keys() if len(values[box]) == 2]
    print('Candidates')
    print(candidates)

    # from the candidates that have 2 values, run through each box
    naked_twins = [[box1, box2] for box1 in candidates
                        #and then that boxes' peers
                                for box2 in peers[box1] \
                                # and add that combination of B1,B2 if
                                #the two boxes values are essentially equal!
                                if set(values[box1]) == set(values[box2])]

    print('Naked Twins!')
    print(naked_twins)

    #For the naked_twins, run through each twin's peers
    #and remove the twin's values from that peer
    for i in range(len(naked_twins)):
        #define our twins for easy reference
        box1 = naked_twins[i][0]
        box2 = naked_twins[i][1]
        #Gather each twin's peers
        peers1 = set(peers[box1])
        peers2 = set(peers[box2])
        peers_int = peers1 & peers2
        #Run through all the peers
        for peer_val in peers_int:
            #by passing peers that are already solved
            if len(values[peer_val]) > 2:
                #run through the values for that peer
                for rm_val in values[box1]:
                    #"reassign"/remove the values from that peer that are contained
                    #in the twin
                    values = assign_value(values, peer_val, values[peer_val].replace(rm_val,''))
    print('After')
    print(display(values))
    #return values


naked_twins(tst)


tst = dict({"G7": "2345678",
            "G6": "1236789",
            "G5": "23456789",
            "G4": "345678",
            "G3": "1234569",
            "G2": "12345678",
            "G1": "23456789",
            "G9": "24578",
            "G8": "345678",
            "C9": "124578",
            "C8": "3456789",
            "C3": "1234569",
            "C2": "1234568",
            "C1": "2345689",
            "C7": "2345678",
            "C6": "236789",
            "C5": "23456789",
            "C4": "345678",
            "E5": "678",
            "E4": "2",
            "F1": "1",
            "F2": "24",
            "F3": "24",
            "F4": "9",
            "F5": "37",
            "F6": "37",
            "F7": "58",
            "F8": "58",
            "F9": "6",
            "B4": "345678",
            "B5": "23456789",
            "B6": "236789",
            "B7": "2345678",
            "B1": "2345689",
            "B2": "1234568",
            "B3": "1234569",
            "B8": "3456789",
            "B9": "124578",
            "I9": "9",
            "I8": "345678",
            "I1": "2345678",
            "I3": "23456",
            "I2": "2345678",
            "I5": "2345678",
            "I4": "345678",
            "I7": "1",
            "I6": "23678",
            "A1": "2345689",
            "A3": "7",
            "A2": "234568",
            "E9": "3",
            "A4": "34568",
            "A7": "234568",
            "A6": "23689",
            "A9": "2458",
            "A8": "345689",
            "E7": "9",
            "E6": "4",
            "E1": "567",
            "E3": "56",
            "E2": "567",
            "E8": "1",
            "A5": "1",
            "H8": "345678",
            "H9": "24578",
            "H2": "12345678",
            "H3": "1234569",
            "H1": "23456789",
            "H6": "1236789",
            "H7": "2345678",
            "H4": "345678",
            "H5": "23456789",
            "D8": "2",
            "D9": "47",
            "D6": "5",
            "D7": "47",
            "D4": "1",
            "D5": "36",
            "D2": "9",
            "D3": "8",
            "D1": "36"
})
