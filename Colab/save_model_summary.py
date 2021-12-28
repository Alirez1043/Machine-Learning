from contextlib import redirect_stdout
import os

def save_model_summery(model, history, train_acc=None, file_name='model-summary.txt'):
  SUMMARY_PATH = './summary'
  try:
    os.mkdir(SUMMARY_PATH)
  except OSError as err:
    pass

  with open(os.path.join(SUMMARY_PATH, file_name), 'a') as f:
    with redirect_stdout(f):
        model.summary()
        print("\nBest accuracy on train set: %" , (max(history.history['acc']) * 100))
        print("Last accuracy on train set: %", history.history['acc'][-1] * 100)

        print("\nBest accuracy on validation set: %" , (max(history.history['val_acc']) * 100))
        print("Last accuracy on validation set: %", history.history['val_acc'][-1] * 100)

        print("\nAccuracy on test set: %", train_acc)
        print('\n=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n\n')
