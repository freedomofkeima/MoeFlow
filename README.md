# MoeFlow

[![CircleCI](https://circleci.com/gh/freedomofkeima/MoeFlow/tree/master.svg?style=shield)](https://circleci.com/gh/freedomofkeima/MoeFlow/tree/master)

Repository for anime characters recognition website, powered by TensorFlow

## Requirements

- TensorFlow 1.4.0 (`pip install tensorflow==1.4.0` first)

## How to run

For first-timers:

```
$ virtualenv -p python3 venv  # Ensure python3 version is 3.5, otherwise TensorFlow might not work
$ . venv/bin/activate

```

After that, you can simply run it by:

```
$ pip install -e .
$ app
```

## License

This project itself is licensed under MIT License. 

Face recognition feature is developed by [nagadomi](https://github.com/nagadomi).

All images are owned by their respective creators.
