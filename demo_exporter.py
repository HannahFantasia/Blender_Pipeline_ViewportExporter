bl_info = {
    "name": "Demo Exporter",
    "author": "Hannah Ümit <twitter.com/HannahUmit>",
    "version": (1,0),
    "blender": (3, 0, 0),
    "category": "Edit",
    "location": "3D Viewport",
    "description": "I made an export to Demo button for my pipeline. Comes in handy, saves minutes.",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}


import bpy
from pathlib import Path

def main(context):
    for ob in context.scene.objects:
        print(ob)


class DemoExport(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.demo_exporterr"
    bl_label = "Demo Exporter"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        path = bpy.path.abspath("//").split("\\")
        filenumber = bpy.data.filepath.split("\\")
        path[-3] = 'Demo'
        path[-1] = filenumber[-1]
        demopath = '\\'.join(path)
        filename = Path(demopath)
        renderpath = filename.with_suffix('.mp4')
        scene = bpy.context.scene
        bpy.data.scenes["Scene"].render.filepath = str(renderpath)

        camera_toggled = []
        for c in bpy.context.screen.areas:
            if c.type == 'VIEW_3D':
                camera_toggled = c.spaces[0].region_3d.view_perspective == "CAMERA"
        if camera_toggled == True:
            pass
        else:
            bpy.ops.view3d.view_camera()

        bpy.context.space_data.overlay.show_overlays = False
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.format = "MPEG4"
        bpy.context.scene.render.ffmpeg.codec = "H264"
        bpy.context.scene.render.ffmpeg.use_max_b_frames = False
        bpy.context.scene.render.ffmpeg.constant_rate_factor = 'NONE'
        bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'REALTIME'
        bpy.context.scene.render.ffmpeg.video_bitrate = 500
        bpy.context.scene.render.ffmpeg.maxrate = 500
        bpy.context.scene.render.ffmpeg.minrate = 0
        bpy.context.scene.render.ffmpeg.buffersize = 224 * 8
        bpy.context.scene.render.ffmpeg.packetsize = 2048
        bpy.context.scene.render.ffmpeg.muxrate = 10080000

        bpy.context.scene.render.ffmpeg.audio_codec = "MP3"
        bpy.context.scene.render.ffmpeg.audio_channels = "STEREO"
        bpy.context.scene.render.ffmpeg.audio_bitrate = 192
        bpy.context.scene.render.ffmpeg.audio_mixrate = 48000

        bpy.ops.render.opengl(animation=True)
        bpy.context.space_data.overlay.show_overlays = True
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(DemoExport.bl_idname, text=DemoExport.bl_label)


def register():
    bpy.utils.register_class(DemoExport)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(DemoExport)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
