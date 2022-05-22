bl_info = {
    "name": "Master Exporter",
    "author": "Hannah Ümit <twitter.com/HannahUmit>",
    "version": (1,0),
    "blender": (3, 0, 0),
    "category": "Edit",
    "location": "3D Viewport",
    "description": "I made an export to master button for my pipeline. Comes in handy, saves minutes.",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}


import bpy

def main(context):
    for ob in context.scene.objects:
        print(ob)


class MasterExport(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.master_exporterr"
    bl_label = "Master Exporter"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        path = bpy.path.abspath("//").split("\\")
        path[-2] = 'Master'
        path[-1] = f'{path[-2]}_Master.blend'
        master = '\\'.join(path)
        bpy.ops.wm.save_as_mainfile(filepath =str(master), check_existing = True, copy = True)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(MasterExport.bl_idname, text=MasterExport.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(MasterExport)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(MasterExport)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
