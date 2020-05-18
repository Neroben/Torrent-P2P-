

class NetworkInfo(object):
    node_addr = list()

    def new_node(self, addr):
        self.node_addr.append(str(addr[0]) + ':' + str(addr[1]))
