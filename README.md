# MoeFlow

[![CircleCI](https://circleci.com/gh/freedomofkeima/MoeFlow/tree/master.svg?style=shield)](https://circleci.com/gh/freedomofkeima/MoeFlow/tree/master)

Repository for anime characters recognition website, powered by TensorFlow

## Requirements

- TensorFlow 1.4.0 (`pip install tensorflow==1.4.0` first)
- [nagadomi/animeface-2009](https://github.com/nagadomi/animeface-2009)

## How to create initial environment

Python Environment:

```
$ virtualenv -p python3 venv  # Ensure python3 version is 3.5, otherwise TensorFlow might not work
$ . venv/bin/activate
$ pip install tensorflow==1.4.0
```

Since `nagadomi/animeface-2009` is an independent project, you need to clone it somewhere in your local directory. Note that the project requires Ruby, ImageMagick, and gcc to run.

After you finish installing it, go to `detect.rb` and update the `require` part (line 4) accordingly.

## How to run

After running steps above, you can simply run it by:

```
$ pip install -e .
$ app
```

## License

This project itself is licensed under MIT License. 

Face recognition feature is developed by [nagadomi](https://github.com/nagadomi).

All images are owned by their respective creators.
