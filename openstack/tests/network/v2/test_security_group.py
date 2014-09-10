# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.network.v2 import security_group

IDENTIFIER = 'IDENTIFIER'
RULES = [
    {
        "remote_group_id": None,
        "direction": "egress",
        "remote_ip_prefix": None,
        "protocol": None,
        "ethertype":
        "IPv6",
        "tenant_id": "4",
        "port_range_max": None,
        "port_range_min": None,
        "id": "5",
        "security_group_id": IDENTIFIER,
    },
    {
        "remote_group_id": "9",
        "direction": "ingress",
        "remote_ip_prefix": None,
        "protocol": None,
        "ethertype": "IPv6",
        "tenant_id": "4",
        "port_range_max": None,
        "port_range_min": None,
        "id": "6",
        "security_group_id": IDENTIFIER,
    },
]
EXAMPLE = {
    'description': '1',
    'id': IDENTIFIER,
    'name': '3',
    'tenant_id': '4',
    'security_group_rules': RULES,
}


class TestSecurityGroup(testtools.TestCase):

    def test_basic(self):
        sot = security_group.SecurityGroup()
        self.assertEqual('security_group', sot.resource_key)
        self.assertEqual('security_groups', sot.resources_key)
        self.assertEqual('/v2.0/security-groups', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = security_group.SecurityGroup(EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['security_group_rules'],
                         sot.security_group_rules)
        self.assertEqual('SecurityGroupRule',
                         sot.security_group_rules[0].__class__.__name__)