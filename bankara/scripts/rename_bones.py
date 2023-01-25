# This script originally from https://www.vg-resource.com/thread-41208.html
# Big shoutouts to Jasper7438 for putting this together.
#
# This script renames Splatoon clothing model bone names/vertex groups to match those of Splatoon 3 clothing models.
# To use this script, select the armature of a S2 clothing model, then run the script.
# This script is based on this script: https://blender.stackexchange.com/questions/69505/renaming-bones-with-python.

import bpy


def rename_bones():
    dict = {
        'root': 'Root',
        'head': 'Head',
        'neck': 'Neck',
        'ear_L': 'Ear_L',
        'ear_R': 'Ear_R',
        ## Merge Chest with Spine2 vertex group, then remove Chest vertex group
        'spine2': 'Spine_3',
        'spine1': 'Spine_2',
        'hip': 'Waist',
        'joint_root': 'Spine_1',
        'thumb_L': 'Finger_A_1_L',
        'thumb_R': 'Finger_A_1_R',
        'fingerA1_L': 'Finger_B_1_L',
        'fingerA1_R': 'Finger_B_1_R',
        'fingerA2_L': 'Finger_B_2_L',
        'fingerA2_R': 'Finger_B_2_R',
        'fingerB1_L': 'Finger_D_1_L',
        'fingerB1_R': 'Finger_D_1_R',
        'fingerB2_L': 'Finger_D_2_L',
        'fingerB2_R': 'Finger_D_2_R',
        'hand_L': 'Wrist_L',
        'hand_R': 'Wrist_R',
        'arm2sub_L': 'Wrist_Assist_L',
        'arm2sub_R': 'Wrist_Assist_R',
        'arm2_L': 'Arm_2_L',
        'arm2_R': 'Arm_2_R',
        'arm1sub_L': 'Arm_Assist_L',
        'arm1sub_R': 'Arm_Assist_R',
        'arm1_L': 'Arm_1_L',
        'arm1_R': 'Arm_1_R',
        'shoulder_L': 'Clavicle_L',
        'shoulder_R': 'Clavicle_R',
        ## Merge Crotch vertex groups with respective Leg1 vertex groups, then remove Crotch vertex groups
        'leg1_L': 'Leg_1_L',
        'leg1_R': 'Leg_1_R',
        'leg1sub_L': 'Leg_Assist_L',
        'leg1sub_R': 'Leg_Assist_R',
        'leg2_L': 'Leg_2_L',
        'leg2_R': 'Leg_2_R',
        'leg2sub_L': 'Ankle_Assist_L',
        'leg2sub_R': 'Ankle_Assist_R',
        'foot_L': 'Ankle_L',
        'foot_R': 'Ankle_R',
        'toe_L': 'Toe_L',
        'toe_R': 'Toe_R',
    }

    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]


if __name__ == '__main__':
    rename_bones()
