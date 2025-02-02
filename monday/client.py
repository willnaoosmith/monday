"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import (
    CustomResource,
    ItemResource,
    ColumnsResource,
    UpdateResource,
    TagResource,
    BoardResource,
    UserResource,
    GroupResource,
    ComplexityResource,
    WorkspaceResource,
    NotificationResource,
    MeResource
)


class MondayClient:
    def __init__(self, token, headers={}):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.custom = CustomResource(token=token, headers=headers)
        self.items = ItemResource(token=token, headers=headers)
        self.columns = ColumnsResource(token=token, headers=headers)
        self.updates = UpdateResource(token=token, headers=headers)
        self.tags = TagResource(token=token, headers=headers)
        self.boards = BoardResource(token=token, headers=headers)
        self.users = UserResource(token=token, headers=headers)
        self.groups = GroupResource(token=token, headers=headers)
        self.complexity = ComplexityResource(token=token, headers=headers)
        self.workspaces = WorkspaceResource(token=token, headers=headers)
        self.notifications = NotificationResource(token=token, headers=headers)
        self.me = MeResource(token=token, headers=headers)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'