## Test results with 100 class

Each class contains only 30 images.

Since we are using a very small number of images (in order to be as realistic as possible), we need to modify `retrain.py`.
If we don't modify it, validation list will be empty for several characters, which will cause division by zero exception.

https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/image_retraining/retrain.py#L193-L198:

```
      if len(validation_images) == 0:
        validation_images.append(base_name)
      elif len(testing_images) == 0:
        testing_images.append(base_name)
      elif percentage_hash < validation_percentage:
        validation_images.append(base_name)
      elif percentage_hash < (testing_percentage + validation_percentage):
        testing_images.append(base_name)
      else:
        training_images.append(base_name)
```

This mechanism allows validation & testing percentage somewhere between 10% - 15%, but it guarantees at least 1 image exists in each category.

## Results

- learning rate = 0.01, training steps = 4000 (default)
```
INFO:tensorflow:2017-11-18 09:32:51.111815: Step 3999: Train accuracy = 89.0%
INFO:tensorflow:2017-11-18 09:32:51.112015: Step 3999: Cross entropy = 1.283925
INFO:tensorflow:2017-11-18 09:32:51.184739: Step 3999: Validation accuracy = 50.0% (N=100)
INFO:tensorflow:Final test accuracy = 53.0% (N=385)
```

- learning rate = 0.02, training steps = 4000
```
INFO:tensorflow:2017-11-18 09:45:02.126555: Step 3999: Train accuracy = 98.0%
INFO:tensorflow:2017-11-18 09:45:02.126758: Step 3999: Cross entropy = 0.612478
INFO:tensorflow:2017-11-18 09:45:02.201436: Step 3999: Validation accuracy = 61.0% (N=100)
INFO:tensorflow:Final test accuracy = 56.9% (N=385)
```

- learning rate = 0.01, training steps = 8000
```
INFO:tensorflow:2017-11-18 09:59:39.834123: Step 7999: Train accuracy = 99.0%
INFO:tensorflow:2017-11-18 09:59:39.834319: Step 7999: Cross entropy = 0.607300
INFO:tensorflow:2017-11-18 09:59:39.905609: Step 7999: Validation accuracy = 56.0% (N=100)
INFO:tensorflow:Final test accuracy = 59.2% (N=385)
```

- learning rate = 0.02, training steps = 8000
```
INFO:tensorflow:2017-11-18 10:13:54.358437: Step 7999: Train accuracy = 100.0%
INFO:tensorflow:2017-11-18 10:13:54.358630: Step 7999: Cross entropy = 0.282326
INFO:tensorflow:2017-11-18 10:13:54.430193: Step 7999: Validation accuracy = 59.0% (N=100)
INFO:tensorflow:Final test accuracy = 59.7% (N=385)
```

- learning rate = 0.005, training steps = 16000
```
INFO:tensorflow:2017-11-18 11:03:02.746575: Step 15999: Train accuracy = 97.0%
INFO:tensorflow:2017-11-18 11:03:02.746776: Step 15999: Cross entropy = 0.704776
INFO:tensorflow:2017-11-18 11:03:02.817481: Step 15999: Validation accuracy = 58.0% (N=100)
INFO:tensorflow:Final test accuracy = 59.0% (N=385)
```

- learning rate = 0.02, training steps = 16000
```
INFO:tensorflow:2017-11-18 11:31:17.489760: Step 15999: Train accuracy = 100.0%
INFO:tensorflow:2017-11-18 11:31:17.489956: Step 15999: Cross entropy = 0.112020
INFO:tensorflow:2017-11-18 11:31:17.560669: Step 15999: Validation accuracy = 61.0% (N=100)
INFO:tensorflow:Final test accuracy = 60.3% (N=385)
```
