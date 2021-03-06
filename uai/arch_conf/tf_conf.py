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

from .base_conf import ArchJsonConf, ArchJsonConfLoader

class TFJsonConf(ArchJsonConf):
    """TensorFlow Json Config class

    """

    def __init__(self, parser):
        """ TensorFlow Json Config Class, Use the super to init
        """
        super(TFJsonConf, self).__init__('tensorflow', parser)

    def _add_args(self):
        super(TFJsonConf, self)._add_args()

        self.params = vars(self.parser.parse_args())
        print self.params

    def _load_conf_params(self):
        """ Config the conf_params from the CMD
        """
        super(TFJsonConf, self)._load_conf_params()
        self.conf_params['http_server'] = {
            'exec': {
                'main_file': self.params['main_file'],
                'main_class': self.params['main_class']
            },
            'tensorflow': {
                'model_dir': self.params['model_dir']
            }
        }

    def get_conf_params(self):
        return self.conf_params

    def get_arg_params(self):
        return self.params

class TFJsonConfLoader(ArchJsonConfLoader):
    def __init__(self, conf):
        super(TFJsonConfLoader, self).__init__(conf)

    def _load(self):
        super(TFJsonConfLoader, self)._load()
        self.model_dir = self.server_conf['tensorflow']['model_dir']

    def get_model_dir(self):
        return self.model_dir
