from bpy.props import BoolProperty, IntProperty
from bpy.types import PropertyGroup

from . base import BaseTabProperties


class PreferencesProperties(BaseTabProperties, PropertyGroup):

    is_persistent: BoolProperty(
        name='Persistent preferences',
        description='With persistent preferences, you can do multiple ' +
                    'rounds of rating materials. The recommender will get ' +
                    'better at recommending materials after each round.',
        default=False
    )

    threshold: IntProperty(
        name='Threshold',
        description='Minimum rating for a material to be recommended. ' +
                    'Search tab will use the materials rated above ' +
                    'this threshold.',
        default=7,
        min=0,
        max=10
    )

    is_gpr_trained: BoolProperty(
        name='Is GPR Trained',
        description='To track if the grp model was trained',
        default=False
    )

    @property
    def next_id(self):
        current_id = 'Prefs{}'.format(self.unique_index)
        self.unique_index += 1
        return current_id
