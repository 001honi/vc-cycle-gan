# HYPER-PARAMETERS
#================================================================================
# Training
num_epochs = 5000
mini_batch_size = 1 

generator_learning_rate = 0.001
generator_learning_rate_decay = generator_learning_rate / 50000
discriminator_learning_rate = 0.0005
discriminator_learning_rate_decay = discriminator_learning_rate / 50000
decay_threshold = 500

lambda_cycle = 10
lambda_identity = 5

# Loop-Control
check_epoch = 1000

# Audio Processing
sampling_rate = 16000
num_mcep = 24
frame_period = 5.0
n_frames = 128

# DEFAULT PATHS
#================================================================================
# Common
train_A_dir_default = './data/train/A1'
train_B_dir_default = './data/train/B'
model_dir_default = './model/A1_to_B'
model_name_default = 'A1_to_B.ckpt'
random_seed_default = 0
validation_A_dir_default = './data/test/A1'
output_dir_default = './data/validation_output'
tensorboard_log_dir_default = './log'
# Conversion
data_dir_default = './data/test/A1'
conversion_direction_default = 'A2B'
conv_output_dir_default = './data/converted_voices'
