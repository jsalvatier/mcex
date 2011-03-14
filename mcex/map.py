'''
Created on Mar 12, 2011

@author: johnsalvatier
'''
from scipy.optimize import fmin_bfgs

def find_map(mapping, model_eval, chain_state, disp = False):
    
    def logp(x):
        mapping.update_with_inverse(chain_state.values_considered, x)
        
        return (model_eval.evalute_as_vector(chain_state))[0]

    def grad_logp(x):
        mapping.update_with_inverse(chain_state.values_considered, x)
        
        return (model_eval.evalute_as_vector(chain_state))[1]
    
    fmin_bfgs(logp, mapping.apply_to_dict(chain_state.values), grad_logp, disp = disp)
    chain_state.accept() 

    