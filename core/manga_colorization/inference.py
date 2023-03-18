import matplotlib.pyplot as plt


def process_image(image, colorizator):
    colorizator.set_image(image, 576, "denoiser", 25)

    return colorizator.colorize()


def colorize_single_image(image_path, save_path, colorizator):
    image = plt.imread(image_path)

    colorization = process_image(image, colorizator)

    plt.imsave(save_path, colorization)

    return True
