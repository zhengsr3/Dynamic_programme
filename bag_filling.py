from dp import *
weight_group=[1,2,3.5,4.3]
value_group=[1.5,3.2,5.8,0]
def bag_filling_state_choice(state,stage):
    stage_next=stage+1
    state_pos=[state]
    while state_pos[-1]-weight_group[stage]>0:
        state_pos.append(state_pos[-1]-weight_group[stage])
    return ([stage_next,state_pos])
def bag_filling_recur_equa(init_stage,init_state,next_stage,next_state):
    return value_group[init_stage]*(init_state-next_state)/weight_group[init_stage]
bag_fill=Dynamic_Programme(bag_filling_recur_equa,bag_filling_state_choice,4)
print(bag_fill(0,53)[0])
print(bag_fill(0,53)[1])
