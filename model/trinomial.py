from .lattice import LatticeModel
from node import Node

import numpy as np



class TrinomialModel(LatticeModel):

    def __init__(self, market, option, mty_date, steps):
        super().__init__(market, option, mty_date, steps)

        self.initialize_parameters()

        self.build_trunk()
        self.build_tree()

    def _compute_alpha(self):
        return np.exp(self.volatility * np.sqrt(3 * self.dt))

    def _compute_probabilities(self):
        m = 1
        q = np.exp(self.volatility**2*self.dt)

        p_down = (q-1-(self.alpha+1)*(m-1))/((1-self.alpha)*((self.alpha**-2)-1))
        p_up = (m-1-((1/self.alpha)-1)*p_down)/(self.alpha-1)
        p_mid = 1-p_up-p_down

        return p_up,p_mid,p_down

    def _initialize_root(self):
        self.root_node = Node(self.S0,0)

        self.root.up_node = self.root_node
        self.root.mid_node = self.root_node
        self.root.down_node = self.root_node

        self.root_node.up_count = 0
        self.root_node.trunk_node = self.root

    def _node_count(self,step):
        return 2*step + 1

    def _node_price(self,next_trunk,nb_up,step):
        return next_trunk.forward*self.alpha**(nb_up-step)

    def _attach_trunk(self,next_trunk,children,step):
        next_trunk.up_node = children[step]
        next_trunk.mid_node = children[step]
        next_trunk.down_node = children[step]

    def _link_next_nodes(self,parent,children,index):
        parent.next_down = children[index]
        parent.next_mid = children[index + 1]
        parent.next_up = children[index + 2]