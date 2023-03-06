dict = {
    'Leg_1_L': 'DEF-thigh.L',
    'Leg_1_R': 'DEF-thigh.R',
    'Leg_Assist_L': 'DEF-thigh.L.001',
    'Leg_Assist_R': 'DEF-thigh.R.001',
    'Leg_2_L': 'DEF-shin.L',
    'Leg_2_R': 'DEF-shin.R',
    'Ankle_L': 'DEF-foot.L',
    'Ankle_R': 'DEF-foot.R',
    'Ankle_Assist_L': 'DEF-shin.L.001',
    'Ankle_Assist_R': 'DEF-shin.R.001',
    'Toe_L': 'DEF-toe.L',
    'Toe_R': 'DEF-toe.R',
    'Waist': 'DEF-spine',
    'Spine_1': 'DEF-spine.001',
    'Spine_2': 'DEF-spine.002',
    'Spine_3': 'DEF-spine.003',
    'Neck': 'DEF-spine.004',
    'Head': 'DEF-spine.006',
    'Clavicle_L': 'DEF-shoulder.L',
    'Clavicle_R': 'DEF-shoulder.R',
    'Arm_Assist_L': 'DEF-upper_arm.L',
    'Arm_Assist_R': 'DEF-upper_arm.R',
    'Arm_1_L': 'DEF-upper_arm.L.001',
    'Arm_1_R': 'DEF-upper_arm.R.001',
    'Arm_2_L': 'DEF-forearm.L',
    'Arm_2_R': 'DEF-forearm.R',
    'Wrist_Assist_L': 'DEF-forearm.L.001',
    'Wrist_Assist_R': 'DEF-forearm.R.001',
    'Wrist_L': 'DEF-hand.L',
    'Wrist_R': 'DEF-hand.R',
}

if __name__ == '__main__':
    import bpy

    for g in bpy.context.object.vertex_groups:
        if g.name in dict.keys():
            g.name = dict[g.name]
