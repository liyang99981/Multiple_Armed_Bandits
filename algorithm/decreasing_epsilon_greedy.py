
import numpy as np

class DecreasingEpsilonGreedy:
    '''
        if (random value < epsilon) then select random arms
        else select the best arms mean in history
        and then in each round to decreasing epsilon (by epsilon = 1/log( times + 0.0000001) )
    '''
    def __init__(self,mu):
        self.mu= mu
        self.mean =0
        self.n=0 # how many times run
    
    def pull(self):
        return np.random.randn() + self.mu
    
    def update(self,xn):
        self.n +=1
        self.mean = ( 1 - 1.0/self.n ) * self.mean + 1.0/self.n * xn

    def run(mu1,mu2,mu3,epsilon=0.1,N=100000):
        bandits=[DecreasingEpsilonGreedy(mu1),
                DecreasingEpsilonGreedy(mu2),
                DecreasingEpsilonGreedy(mu3)]       
        data=np.empty(N)
        
        for i in range(N):
            epsilon = 1 / np.log( i+1 + 0.0000001)
            p=np.random.random()
            if p<epsilon: j = np.random.choice(3)
            else: j = np.argmax([b.mean for b in bandits])
                
            x=bandits[j].pull()
            bandits[j].update(x)
            data[i] =x

        cumul_average =np.cumsum(data)/(np.arange(N)+1)
        return cumul_average