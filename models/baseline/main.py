import argparse

from trainingNew import training
from evaluateNew import evaluate

# from speakerDatasetNew import test
# test()

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--attribute', type=str, required=True)
parser.add_argument('--mode',type=str,required=True)
parser.add_argument('--lr',type=float,required=False)
parser.add_argument('--dropoutrate',type = float, required=True)
parser.add_argument('--batchSize',type = int, required=True)
parser.add_argument('--gadi', default=False, action='store_true')
args = parser.parse_args()

mode = args.mode
gadi = args.gadi
if mode == 'train':
    training(modelName = args.name,attribute = args.attribute,learning_rate = args.lr, dropout_rate= args.dropoutrate ,batch_size = args.batchSize,gadi=gadi)
elif mode == 'test':
    if gadi:
        evaluate(path=f"/scratch/wa66/dr2845/models/trainedModels/baseline/{args.attribute}/{args.name}_{args.lr}_{args.batchSize}.pth",model_name = args.name, attribute=args.attribute, batch_size = args.batchSize,gadi=gadi)
    else:
        evaluate(path=f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/baseline/valence/extras/valence_3_0.001_32.pth",model_name = args.name,attribute=args.attribute, batch_size = args.batchSize,gadi=gadi)

else:
    print("Error: Introduce mode = 'train' or 'test' ")