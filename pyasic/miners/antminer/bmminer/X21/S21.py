# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.backends import AntminerModern
from pyasic.miners.device.models import S21, S21Hydro, S21Plus, S21PlusHydro, S21Pro


class BMMinerS21(AntminerModern, S21):
    pass


class BMMinerS21Plus(AntminerModern, S21Plus):
    pass


class BMMinerS21PlusHydro(AntminerModern, S21PlusHydro):
    pass


class BMMinerS21Pro(AntminerModern, S21Pro):
    pass


class BMMinerS21Hydro(AntminerModern, S21Hydro):
    pass
