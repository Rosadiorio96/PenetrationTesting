from .Action import *
import numpy as np
class Host:
    def __init__(self, name, ip):
        self.host_name = name
        self.host_ip = ip
    
    def perform_action(self, state, action):

        if isinstance(action,np.int64) or isinstance(action,int):
            action = generate_action(action)

        if action.is_exploit():
            print("Exploit")
            val = action.executeExploit(self.host_name)
            if state.vectorState.vector[2] == -1:
                print("OOOOOK6")
                state.set_compromised(2)
                result = ActionResult(-1, action)
                print("No scansione totale fatta")
                print("R", result.success)
                return result, state
                
            else:
                print("Scansione totale fatta")
                print(val)
                if action.id == 4:
                    if state.vectorState.vector[12] != 1:
                        print("OOOOOK")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK2")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                    
                if action.id == 3:
                    if state.vectorState.vector[13] != 1:
                        print("OOOOOK3")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK4")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                if action.id == 1:
                    if state.vectorState.vector[10] != 1:
                        print("OOOOOK5")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK6")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                if action.id == 5:
                    if state.vectorState.vector[11] != 1:
                        print("OOOOOK7")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK8")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                if action.id == 0:
                    if state.vectorState.vector[14] != 1:
                        print("OOOOOK7")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK8")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                if action.id == 6:
                    if state.vectorState.vector[15] != 1:
                        print("OOOOOK9")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK10")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                if action.id == 2:
                    if state.vectorState.vector[16] != 1:
                        print("OOOOOK11")
                        state.set_compromised(-1)
                        result = ActionResult(-1, action)
                        print("No scansione")
                        print("R", result)
                        return result, state
                    else:
                        print("OOOOOK12")
                        result = ActionResult(val, action)
                        state.set_compromised(val)
                        print("Si scansione")
                        print("R", result)
                        return result, state
                
            result = ActionResult(val, action)
            state.set_compromised(val)
            return result, state 
        elif action.is_scanVuln():         
            if action.id != 11 :                          
                if state.vectorState.vector[2] == -1 and action.id != 11:      
                    print("Scansione totale NON fatta")
                    val = -1
                    result = ActionResult(val, action)
                    return result, state
                else:
                    val = action.executeScan(self.host_name)
                    print("Scansione totale fatta")
                    result = ActionResult(val, action)
                    state.config_vulnerabilities(result) 
                    return result, state          
            else:  
                val = action.executeScan(self.host_name)
                print("OOOOOK45")             
                state.config_ports(val)
                state.config_services(val)
                state.config_os(val)
                result = ActionResult(0, action)

            
            
                return result, state
        else:
            print("error")