import numpy as np

def create_brownian_motion(maturity = 1, steps = 255, no_realisations = 100):
    
    dt = maturity/steps
    
    timerange = np.linspace(0, maturity, steps + 1, endpoint=True)
    timerange = timerange[:,None]

    Wt = np.zeros((steps + 1, no_realisations))
    
    dW = np.sqrt(dt) * np.random.randn(steps, no_realisations)
    
    Wt[1:,:] = np.cumsum(dW,0)
    
    return Wt, timerange




def underlying_asset(S0, mu, sigma, t, Wt):
  """ Rend les realisations de St une fois donne le tmps et Wt
  avec la formule St = S0 * exp( (mu-sigma*sigma/2.0)*t + sigma*Wt)  """ 
  return S0 * np.exp( (mu-sigma**2.0/2.0)*t+ sigma*Wt)