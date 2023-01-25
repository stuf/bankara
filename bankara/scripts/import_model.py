# Can't remember if this actually ever worked lmao
#
import bpy
import re

from bpy.types import Context, Object, Mesh
from mathutils import Vector
from os import listdir
from os.path import join, isfile

FileDir = str
FileName = str
FileEntry = tuple[FileDir, FileName]

IMPORT_DIR = r'X:\Assets\_Rip\_New\_Obj\BossGateway'
IMPORT_FILE = r'Obj_BossGateway.fbx'
TEXTURE_EXT = 'png'

NAME_PREFIX = 'Prefix'
NAME_SEPARATOR = '_'

DEFAULT_ARMATURE_SCALE = Vector((1, 1, 1))

# Cleanup / arrange
MAT_NAME_PATT = r'(?P<mname>\w+)\.(\d+)$'

matNameRe = re.compile(MAT_NAME_PATT)


def _import_fbx(filepath: FileEntry, context: Context):
    """Imports an FBX scene and returns the objects created from this"""
    try:
        bpy.ops.import_scene.fbx(filepath=join(*filepath), use_image_search=False)
    except Exception:
        pass

    return list(context.selected_objects)


def _handle_material(obj: Object):
    if obj.active_material_index == 0:
        print(f'obj {obj.name} has no active material; {obj=}')
        return

    mat = obj.active_material
    ms = re.match(r'^(?P<mat_name>\w+)', mat.name)

    if ms is None:
        print(f'No material for {mat.name}')


def main():
    context = bpy.context
    objects = {}

    files = [(IMPORT_DIR, IMPORT_FILE)]
    for d, f in files:
        objects[f] = objs = _import_fbx((d, f), context)

        for o in objs:
            if o.type == 'ARMATURE':
                o.scale = DEFAULT_ARMATURE_SCALE
                continue
            elif o.type == 'MESH':
                # Do some material magic here
                pass


if __name__ == '__main__':
    main()
