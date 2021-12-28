import matplotlib.pyplot as plt
import random
import os
# If you want to save plot pass save_fig=True And a string as fig id
# for example below code saves figure as fig02.png 
# plot_history(history=history, fig_id="fig02", fig_size=4, save_fig=True)

# If just want to plot history use below code
# plot_history(history)

def plot_history(history, fig_size=4, save_fig=False, fig_id="fig"):
  plt.figure(figsize=(2 * fig_size,fig_size))
  plt.subplot(121)
  plt.plot(history.history['acc'], label='train', c='b')
  plt.plot(history.history['val_acc'], label='validation', c='r')
  plt.xlabel("#epochs")
  plt.ylabel("Accuracy")
  plt.grid(True)
  plt.legend()

  plt.subplot(122)
  plt.plot(history.history['loss'], label='train', c='b')
  plt.plot(history.history['val_loss'], label='validation', c='r')
  plt.xlabel("#epochs")
  plt.ylabel("Loss")
  plt.grid(True)
  plt.legend()
  
  if save_fig:
    FIG_EXTENSION = 'png'
    RESOLUTION = 100
    IMAGES_PATH = './images'

    try:
      os.mkdir(IMAGES_PATH)
    except OSError as err:
      pass
      
    path = os.path.join(IMAGES_PATH, fig_id + "." + FIG_EXTENSION)
    print("Saving figure", fig_id)
    plt.tight_layout()
    plt.savefig(path, format=FIG_EXTENSION, dpi=RESOLUTION)

  plt.show()
