from dp import *
def renew_equip_state_choice(state,stage):
    stage_next=stage+1
    state_pos=[1]
    if state<5:
        state_pos.append(state+1)
    return([stage_next,state_pos])
def renew_equip_recur_equa(init_stage,init_state,next_stage,next_state):
    s=[None,50,25,10,5,2]
    c=[30,40,50,75,90]
    new_cost=[100,105,110,115,120]
    if next_state==1:
        return -new_cost[init_stage-1]+s[init_state]-c[0]
    else:
        #print(init_state)
        return -c[init_state]
renew_eq=Dynamic_Programme(renew_equip_recur_equa,renew_equip_state_choice,6)
print(renew_eq(1,2)[0])
print(renew_eq(1,2)[1])
