#-------------------------------------------------------------------
    def info_from_trace(self,trace):
        final_dict={}
        for i in range(len(trace)):
            if (trace[i][0],trace[i][1]) not in final_dict.keys(): #have to see the else part later whether req or not
                inner_tr_dict={}
                temp_keylist=list(trace[i][2].keys())
                for k in range(len(temp_keylist)):
                    new_key=temp_keylist[k].strip(' ').strip('"').strip("'")
                    if new_key not in inner_tr_dict.keys():
                        inner_tr_dict[new_key]=[trace[i][2][temp_keylist[k]]]
                    else:
                        inner_tr_dict[new_key].append(trace[i][2][temp_keylist[k]])
                # final_dict[(trace[i][0],trace[i][1])]=trace[i][2]
                final_dict[(trace[i][0],trace[i][1])]=inner_tr_dict
        #print(final_dict)      
        #print('final_dict=',final_dict[list(final_dict.keys())[0]]) # has the structured trace without the impl of colon issue..!
        self.variable_trace(final_dict)
#-------------------------------------------------------------------
    def variable_trace(self,final_dict):
        var_dict = {}
        for i in list(final_dict.keys()):
            for j in list(final_dict[i].keys()):
                a_dict = final_dict[i]
                if(j not in list(var_dict.keys())):
                    var_dict[j] = []
                    var_dict[j].append(a_dict[j])
                else:
                    var_dict[j].append(a_dict[j])
        res = 1
        while(res):
            print('Do you want to view the trace of any variable? Type yes or no ')
            response = input()
            if((response == 'YES') or (response == 'Yes') or (response == 'y') or (response == 'Y') or (response == 'yes')):
                res = 1
                print('The variables are =',list(var_dict.keys()),'\nEnter the variable whose trace you want to see')
                user_varible = input()
                #print(user_varible)
                print('The variables trace of',user_varible,' is =',var_dict[user_varible])
            else:
                res = 0
            
        

#-------------------------------------------------------------------
