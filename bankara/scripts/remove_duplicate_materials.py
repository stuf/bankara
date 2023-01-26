"""
Script for finding duplicate-looking material names and replacing their usage with the
basename version of it.

E.g. you have materials 'Material' and 'Material.001' and you want all users of 'Material.001'
     to actually use 'Material'.

     Optionally you also want to remove 'Material.001' to not mess up your Blender mats.
"""
import bpy
import re

DUPLICATE_PATTERN = r'\.\d{3}$'
"""Pattern for matching a duplicate name"""

CLEAR_DUPLICATES = True
"""Whether or not duplicates should be cleared after searching"""

duplicatePattern = re.compile(DUPLICATE_PATTERN)


def do_thing():
    replaced = set()

    # Look at all objects currently in Blender
    # If you have multiple scenes this will go through them too, so that might be a problem.
    # TODO: maybe use `bpy.context.scene.objects` instead?
    # TODO: Also maybe use `o.active_material` instead?
    for o in bpy.data.objects:
        # For every object, look at the material slots
        for mslot in o.material_slots:
            if re.search(DUPLICATE_PATTERN, mslot.name):
                # Ok so we found a duplicate
                # Should first check if the non-duplicate exists or if this
                # is just derpy naming
                basename = re.sub(DUPLICATE_PATTERN, '', mslot.name)

                if basename in bpy.data.materials:
                    # Great, it exists! Then point this slot to use that material instead
                    # and take note of this name for removal
                    replaced.add(mslot.name)

                    mslot.material = bpy.data.materials[basename]

    # After we're done, we should remove any duplicates that we had reassigned
    if len(replaced):
        for mat_name in replaced:
            bpy.data.materials.remove(bpy.data.materials[mat_name])


if __name__ == '__main__':
    do_thing()
