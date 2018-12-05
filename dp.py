class Dynamic_Programme:
    def __init__(self,recur_equa,state_choice,stage_final):
        '''
        recur_equa:a function take current_stage,current_state,next_stage,next_state as input and return return
        state_choice:return a 2-item list.the first item is next stage and the second item is possible next state
        '''
        self.recur_equa=recur_equa
        self.state_choice=state_choice
        self.stage_final=stage_final
    def __call__(self,init_stage,init_state):
        '''
        return two item:decision path (a str) and max return 
        '''
        s=[None,50,25,10,5,2]
        c=[30,40,50,75,90]
        new_cost=[100,105,110,115,120]
        if init_stage==self.stage_final:
            return ['stage:'+str(init_stage)+';state:'+str(init_state)+'\n',0]
        next_stage,state_list=self.state_choice(init_state,init_stage)
        max_ret=float('-inf')
        state_str='stage:'+str(init_stage)+';state:'+str(init_state)+'\n'
        for next_state in state_list:
            out=self(next_stage,next_state)
            ret=self.recur_equa(init_stage,init_state,next_stage,next_state)+out[1]
            if ret>max_ret:
                max_ret=ret
                dec_paths=state_str+out[0]
        return[dec_paths,max_ret]
