# ============================================================
# ComfyUI Custom Node Pack
# Author: xb1n0ry
# Description: Resolution, Aspect Ratio, and Frame tools for Wan 2.2
# ============================================================

__author__ = "xb1n0ry"

# ------------------------------------------------------------
# NODE 1: Max Long Edge Picker
# ------------------------------------------------------------
class MaxLongEdgePicker:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "long_edge": ([
                    "512 (LoRA bucket / Best with 1:1)", 
                    "704 (WAN native 480p Alt / Best with 3:2/2:3)",
                    "768 (LoRA bucket / Best with 3:2/2:3)", 
                    "832 (WAN native 480p / Best with 16:9/9:16)", 
                    "960 (LoRA bucket / Best with 16:9/9:16)", 
                    "1024 (LoRA bucket / Best with 1:1)", 
                    "1280 (WAN native 720p / LoRA bucket / Best with 16:9/9:16)", 
                    "1920 (WAN native 1080p / Best with 16:9/9:16 !THIS IS MADNESS!)"
                ], {}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("long_edge",)
    FUNCTION = "get_value"
    CATEGORY = "xb1n0ry-Tools"

    def get_value(self, long_edge):
        clean_number = int(long_edge.split()[0])
        return (clean_number,)


# ------------------------------------------------------------
# NODE 2: Aspect Ratio Picker
# ------------------------------------------------------------
class AspectRatioPicker:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "aspect_ratio": ([
                    "16:9 (Horizontal / Cinematic)",
                    "9:16 (Portrait / Social)",
                    "3:2 (Horizontal / Photography)",
                    "2:3 (Portrait / Photography)",
                    "1:1 (Perfect Square)"
                ], {}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("aspect_ratio",)
    FUNCTION = "get_value"
    CATEGORY = "xb1n0ry-Tools"

    def get_value(self, aspect_ratio):
        clean_ratio = aspect_ratio.split()[0]
        return (clean_ratio,)


# ------------------------------------------------------------
# NODE 3: Frame Count Picker
# ------------------------------------------------------------
class FrameCountPicker:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "frame_count": ([
                    "33 (~2s)",
                    "49 (~3s)",
                    "81 (Native ~5s)",
                    "97 (~6s)",
                    "129 (~8s - 24GB VRAM Limit)",
                    "161 (~10s - Heavy VRAM)"
                ], {}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("frames",)
    FUNCTION = "get_value"
    CATEGORY = "xb1n0ry-Tools"

    def get_value(self, frame_count):
        # Extracts just the number (e.g., "81") before the space
        clean_frames = int(frame_count.split()[0])
        return (clean_frames,)


# ------------------------------------------------------------
# REGISTRATION MAPPINGS
# ------------------------------------------------------------
NODE_CLASS_MAPPINGS = { 
    "MaxLongEdgePicker": MaxLongEdgePicker,
    "AspectRatioPicker": AspectRatioPicker,
    "FrameCountPicker": FrameCountPicker
}

NODE_DISPLAY_NAME_MAPPINGS = { 
    "MaxLongEdgePicker": "Max Long Edge Picker",
    "AspectRatioPicker": "Aspect Ratio Picker",
    "FrameCountPicker": "Frame Count Picker"
}
