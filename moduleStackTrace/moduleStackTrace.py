class moduleStackTrace:
    def __init__(self):
        self.callstack = ''
        print('moduleStackTrace__init__')
    def show(self, call):
        self.callstack += call
        print('called from', __name__, 'trying', call)