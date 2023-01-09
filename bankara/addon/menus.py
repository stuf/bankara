import bpy

ADD_MENU = 'VIEW3D_MT_add'


class VIEW3D_MT_bankarautils_main(bpy.types.Menu):
    """Main menu for adding assets"""

    bl_idname = 'VIEW3D_MT_bankarautils_main'
    bl_label = 'Bankara Utils'

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.separator()

        layout.label('Label text')


CLASSES = (
    VIEW3D_MT_bankarautils_main,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
