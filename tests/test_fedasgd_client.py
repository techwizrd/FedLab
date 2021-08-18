# Copyright 2021 Peng Cheng Laboratory (http://www.szpclab.com/) and FedLab Authors (smilelab.group)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

import sys

from torch.utils.data import dataloader


sys.path.append("../")
from copy import deepcopy

from fedlab.core.client.trainer import ClientSGDTrainer
from fedlab.core.client.manager import ClientActiveManager
from fedlab.core.server.handler import AsyncParameterServerHandler
from fedlab.core.server.manager import ServerAsynchronousManager
from fedlab.core.network import DistNetwork

from tests.test_core.task_setting_for_test import (
    unittest_dataloader,
    model,
    criterion,
    optimizer,
    TestTrainer,
)


class FedAsgdClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        ip = "127.0.0.1"
        port = "3001"
        world_size = 2

        handler = AsyncParameterServerHandler(
            deepcopy(model), client_num_in_total=world_size - 1
        )
        self.server = ServerAsynchronousManager(
            handler=handler,
            network=DistNetwork(address=(ip, port), world_size=world_size, rank=0),
        )
        
        self.server.start()

        dataloader = unittest_dataloader()
        handler = ClientSGDTrainer(
            deepcopy(model),
            dataloader,
            epochs=1,
            optimizer=optimizer,
            criterion=criterion,
            cuda=False,
        )

        self.client = ClientActiveManager(
            handler=handler,
            network=DistNetwork(address=(ip, port), world_size=world_size, rank=1),
        )

    def test_fedavg(self):
        self.client.run()
        