# Copyright 2017 The UAI-SDK Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from base_tool import UaiDeployTool
from uai.arch_conf.keras_conf import KerasJsonConf


class KerasDeployTool(UaiDeployTool):
    def __init__(self, parser):
        super(KerasDeployTool, self).__init__('keras', parser)

    def _add_args(self):
        """Keras specific _add_args tool to parse Keras params through KerasJsonConf
        """
        keras_json_conf = KerasJsonConf(self.parser)
        self.conf_params = keras_json_conf.get_conf_params()

    def deploy(self):
        super(KerasDeployTool, self).deploy()
