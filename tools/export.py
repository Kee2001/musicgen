from audiocraft.utils import export
from audiocraft import train

# from https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md#importing--exporting-models
import sys
model_path = sys.argv[1]
name = model_path.split('/')[-1].split('.')[0]
export.export_lm('models/chroma_ckpt9.th', f'models/{name}/state_dict.bin')
# export.export_pretrained_compression_model('facebook/encodec_32khz', '/content/checkpoints/finetune/compression_state_dict.bin')
