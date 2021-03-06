# Copyright 2012, Nachi Ueno, NTT MCL, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# Copyright (c) 2013-2014,2017 Wind River Systems, Inc.
#


from oslo_config import cfg

from neutron._i18n import _


security_group_opts = [
    cfg.StrOpt(
        'firewall_driver',
        help=_('Driver for security groups firewall in the L2 agent')),
    cfg.BoolOpt(
        'enable_security_group',
        default=True,
        help=_(
            'Controls whether the neutron security group API is enabled '
            'in the server. It should be false when using no security '
            'groups or using the nova security group API.')),
    cfg.BoolOpt(
        'enable_ipset',
        default=True,
        help=_('Use ipset to speed-up the iptables based security groups. '
               'Enabling ipset support requires that ipset is installed on L2 '
               'agent node.')),
    cfg.BoolOpt(
        'ensure_default_security_group',
        default=True,
        help=_("Enable/Disable association of default security group "
               "on port during port creation")),
    cfg.IntOpt(
        'notify_interval',
        default=0,
        help=_('Throttled firewall rule update notification interval')),
]


def register_securitygroups_opts(cfg=cfg.CONF):
    cfg.register_opts(security_group_opts, 'SECURITYGROUP')
