import re
from os import listdir
from os.path import join, isfile, basename
from dataclasses import dataclass, field

from bpy.types import NodeTree, Nodes, NodeLinks


@dataclass
class Material:
    name: str
    path: str
    basename: str
    nodes: Nodes = None
    links: NodeLinks = None
