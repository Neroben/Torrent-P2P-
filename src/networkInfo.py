

class NetworkInfo(object):
    node_addr = set()

    def new_node(self, addr):
        self.node_addr.add(addr)
