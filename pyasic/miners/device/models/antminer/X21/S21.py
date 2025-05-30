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
from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import AntMinerMake


class S21(AntMinerMake):
    raw_model = MinerModel.ANTMINER.S21

    expected_chips = 108
    expected_fans = 4
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class S21Plus(AntMinerMake):
    raw_model = MinerModel.ANTMINER.S21Plus

    expected_chips = 55
    expected_fans = 4
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class S21PlusHydro(AntMinerMake):
    raw_model = MinerModel.ANTMINER.S21PlusHydro

    expected_chips = 95
    expected_fans = 0
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class S21Pro(AntMinerMake):
    raw_model = MinerModel.ANTMINER.S21Pro

    expected_chips = 65
    expected_fans = 4
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class S21Hydro(AntMinerMake):
    raw_model = MinerModel.ANTMINER.S21Hydro

    expected_chips = 216
    expected_hashboards = 3
    expected_fans = 0
    algo = MinerAlgo.SHA256
