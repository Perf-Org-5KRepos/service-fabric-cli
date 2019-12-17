# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedApplicationIdentityDescription(Model):
    """Managed application identity description.

    :param token_service_endpoint: Token service endpoint.
    :type token_service_endpoint: str
    :param managed_identities: A list of managed application identity objects.
    :type managed_identities:
     list[~azure.servicefabric.models.ManagedApplicationIdentity]
    """

    _attribute_map = {
        'token_service_endpoint': {'key': 'TokenServiceEndpoint', 'type': 'str'},
        'managed_identities': {'key': 'ManagedIdentities', 'type': '[ManagedApplicationIdentity]'},
    }

    def __init__(self, *, token_service_endpoint: str=None, managed_identities=None, **kwargs) -> None:
        super(ManagedApplicationIdentityDescription, self).__init__(**kwargs)
        self.token_service_endpoint = token_service_endpoint
        self.managed_identities = managed_identities