"""@package panoptes.state.mount
Holds the states for the mount
"""
import smach

from panoptes.state import state

class Parked(state.PanoptesState):
    def __init__(self):
        state.PanoptesState.__init__(self, outcomes=['shutdown', 'fail'])
        self.counter = 0

    def execute(self, userdata):
        self.logger.info("Executing {}".format(type(self).__name__))
        self.logger.info("Looking at observatory lat: {}".format(userdata.observatory_in.site.lat))
        if self.counter < 3:
            self.counter += 1
            return 'shutdown'
        else:
            return 'fail'

class Shutdown(state.PanoptesState):
    def __init__(self):
        state.PanoptesState.__init__(self, outcomes=['sleeping'])

    def execute(self, userdata):
        self.logger.info("Executing {}".format(type(self).__name__))
        return 'sleeping'

class Sleeping(state.PanoptesState):
    def __init__(self):
        state.PanoptesState.__init__(self, outcomes=['parked'])

    def execute(self, userdata):
        self.logger.info("Executing {}".format(type(self).__name__))
        self.logger.info("Sleeping until night")
        return 'parked'
