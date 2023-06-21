import argparse

from individualAdaptation import adaptation

parser = argparse.ArgumentParser()
parser.add_argument('--gadi', default=False, action='store_true')
parser.add_argument('--name',type=str,required=True)

parser.add_argument('--speaker', type=int, required=True)
parser.add_argument('--attribute', type=str, choices= ['arousal','dominance','valence'],required=True)
parser.add_argument('--batch_size',type = int, required=True)
parser.add_argument('--plain',type=str,choices=['plain','diverse'])
parser.add_argument('--pc', type= int, choices= [35,58], required=True)

args = parser.parse_args()

gadi = args.gadi

adaptation(modelName= args.name, attribute= args.attribute, batch_size= args.batch_size, plain= args.plain, pc= args.pc, speaker= args.speaker, gadi= gadi)

