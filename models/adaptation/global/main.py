import argparse

from globalAdaptation import adaptation
from speakerDataset import test


parser = argparse.ArgumentParser()
parser.add_argument('--gadi', default=False, action='store_true')
parser.add_argument('--mode',type=str, choices= ['adaptation','test'],required=True)

parser.add_argument('--name', type=str, required=True)
parser.add_argument('--attribute', type=str, choices= ['arousal','dominance','valence'],required=True)
parser.add_argument('--batch_size',type = int, required=True)
parser.add_argument('--approach',type=str, choices= ['Unique','Oversampling'],required=True)
parser.add_argument('--plain',type=str,choices=['plain','diverse'])
parser.add_argument('--pc',type=int,choices=[35,58])
parser.add_argument('--random_seed', type= int,required=True)

args = parser.parse_args()

mode = args.mode
gadi = args.gadi

if mode == 'adaptation':
    adaptation(modelName = args.name,attribute = args.attribute, batch_size = args.batch_size, plain= args.plain, approach = args.approach, pc = args.pc, random_seed= args.random_seed , gadi = gadi)
elif mode == 'test':
    # evaluate(path=f"/scratch/wa66/dr2845/models/trainedModels/baseline/{args.attribute}/{args.name}_{args.lr}_{args.batch_size}.pth",attribute=args.attribute, batch_size = args.batchSize)
    print("Eval not implemented")
else:
    print("Error: Introduce mode = 'train' or 'test' ")


# test()