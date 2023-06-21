import audiofile
import opensmile

# Load the features
def load_features(audioFile):

    # Read the file into memory.
    
    signal, sampling_rate = audiofile.read(
        audioFile
    )

    duration = audiofile.duration(audioFile)

    # Create the feature extractor for Compare 2016

    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.ComParE_2016,
        feature_level=opensmile.FeatureLevel.Functionals,
    )

    # And process the signal to extract features and create a dataframe

    featureDf = smile.process_signal(
        signal,
        sampling_rate
    )

    return featureDf, duration
