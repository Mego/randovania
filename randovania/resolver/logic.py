import collections
from typing import Dict

from randovania.game_description.game_description import GameDescription
from randovania.game_description.node import Node
from randovania.game_description.requirements import RequirementSet
from randovania.resolver.game_patches import GamePatches
from randovania.resolver.layout_configuration import LayoutConfiguration


class Logic:
    """Extra information that persists even after a backtrack, to prevent irrelevant backtracking."""

    game: GameDescription
    configuration: LayoutConfiguration
    patches: GamePatches
    additional_requirements: Dict[Node, RequirementSet]
    node_sightings: Dict[Node, int]

    def __init__(self, game: GameDescription, configuration: LayoutConfiguration, patches: GamePatches):
        self.game = game
        self.configuration = configuration
        self.patches = patches
        self.additional_requirements = {}
        self.node_sightings = collections.defaultdict(int)

    def get_additional_requirements(self, node: Node) -> RequirementSet:
        return self.additional_requirements.get(node, RequirementSet.trivial())
