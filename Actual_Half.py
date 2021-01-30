rotations1 = {"InSrv1": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU":4, "OB1": 8, "PedC": 4, "InSrv2": 4, "NICU": 4, "Nuro": 4, "Clinic": 33, "OB2": 2}
electives = ["InSrv1", "Card1", "Surg", "Emed", "ICU", "OB1", "PedC", "InSrv2", "NICU", "Nuro", "Clinic", "OB2"]
sessions = [4, 4, 14, 23, 4, 8, 4, 4, 4, 4, 33, 2]
z = list(zip(electives, sessions))

    #print("The original schedule for resident 1, year 1 is:" + str(rotations1))

    #step 2 on chart
def random_shuffle():
    '''Shuffles the values randomly'''
    random.shuffle(z)
    electives[:], sessions[:] = zip(*z)
        #print("the shuffled rotations are ")
        # print(electives, sessions)

def half():
    '''Splits the values in half and runs range check'''
    first_half = sessions[:len(sessions)//2]
    second_half = sessions[len(sessions)//2:]
    # print(quarter_range)
    max_first = max(first_half)
    min_first = min(first_half)
    max_second = max(second_half)
    min_second = min(second_half)
    quarter_range = max_first - max_second
    if quarter_range > max_second:
        max_first, max_second = min_second, min_first
        #print("Check works")
        half()
    else:
        #print("passed check")
        results = first_half + second_half
        #finalResults = dict(results)
        print("the new schedule is:" + str(results))
        #keys = electives
        #values = session
                
def test_run():
    '''Runs the algorithim a set number of times'''
    random_shuffle()
    half()
test_run()
