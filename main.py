# If you need to contact me in the future just send a request on github. (emarron)
# I'm running this using the cellpose v2 docker container
# https://hub.docker.com/layers/biocontainers/cellpose/2.1.1_cv2/images/sha256-cfe36943a49590da85c64bb8006330397193de2732faad06f41260296e35978c?context=explore
# cellpose - 2.1.1_cv2
from pathlib import Path

# basic parameters taken from cellpose collab page
# https://colab.research.google.com/github/MouseLand/cellpose/blob/main/notebooks/run_cellpose_2.ipynb#scrollTo=ldNwr_zxMVha

from cellpose import core

from scripts.log_wrapper import IOWrapper
from scripts.test_wrapper import test, test_blanks
from scripts.train_wrapper import train, get_masks
from pathlib import Path

io_wrapper = IOWrapper()
logger, log_file, log_handler = io_wrapper.logger_setup(log_directory="./data/log/")

# check if you have GPU on, see thread if using pycharm
# https://stackoverflow.com/questions/59652992/pycharm-debugging-using-docker-with-gpus
use_GPU = core.use_gpu()
yn = ['NO', 'YES']
logger.info(f'>>> GPU activated? {yn[use_GPU]}')

# train dirs
train_set_0_dir = Path('data/train/set_0/')  # 78 IMAGES
train_set_1_dir = Path('data/train/set_1/')  # 115 IMAGES
# test dirs
test_set_0_A_dir = Path('data/test/test_8_set_0_A/')  # 8 IMAGES
test_set_0_B_dir = Path('data/test/test_8_set_0_B/')  # 8 IMAGES
test_set_1_dir = Path('data/test/test_34_set_1/')  # 34 IMAGES
# empty dirs
empty_set_0_dir = Path('data/test/empty_set_0/')  # 21 IMAGES
empty_set_1_dir = Path('data/test/empty_set_1/')  # 12 IMAGES

"""
dataset = 99 images
dataset ge 5 masks = 62 images
dataset ge 1 masks = 78 images
"""
# replace variables A,B,C and x,y,z with your desired tests.
# training

# print("training model A with x,y,z param, on B image set.")
# model = train(train_dir=test_set_1_dir, model_type="CPx", use_GPU=True, n_epochs=10, test_dir=test_set_1_dir)
# model_path = io_wrapper.get_model_path(log_handler.logs)
# io_wrapper.plot_training_stats(io_wrapper.get_training_stats(log_handler.logs), model_name=model_path.name)
# test
nmasks = get_masks(train_set_0_dir, True)
print(nmasks)
print("model A trained with x,y,z param on B image set, testing on C image set")
# test(test_dir=test_set_0_A_dir,model_path=model_path, use_GPU=True)
# test(test_dir=test_set_0_B_dir,model_path=model_path, use_GPU=True)
# test_blanks(test_dir=empty_set_0_dir, model_path=model_path, use_GPU=True)
# test_blanks(test_dir=empty_set_1_dir, model_path=model_path, use_GPU=True)

# label_me = "data/Confidential_images_for_MIPAR_100_3folders_fullsize_bb/train"
# run(label_me, train_dir + "/models/honkler", use_GPU)

# test_multiple('data/Confidential_images_for_MIPAR_100_3folders_fullsize_bb/train/models')
