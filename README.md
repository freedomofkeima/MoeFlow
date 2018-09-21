# MoeFlow

[![CircleCI](https://circleci.com/gh/freedomofkeima/MoeFlow/tree/master.svg?style=shield)](https://circleci.com/gh/freedomofkeima/MoeFlow/tree/master)

Repository for anime characters recognition website, powered by TensorFlow.

Demonstration page (Alpha version): [MoeFlow Website](https://freedomofkeima.com/moeflow/).

MoeFlow is featured in:
- PyCon ID 2017 | [Presentation](https://freedomofkeima.com/pyconid2017.pdf)
- [PyCon JP 2018](https://pycon.jp/2018/en/event/sessions) | [Presentation](https://freedomofkeima.com/pyconjp2018.pdf) | [Video](https://www.youtube.com/watch?v=Oh-raRnQoUA)

## Project Introduction

This project is related to [freedomofkeima/transfer-learning-anime](https://github.com/freedomofkeima/transfer-learning-anime).

### Background

This project is heavily inspired from characters indexing website such as [saucenao](https://saucenao.com/) and [iqdb](https://www.iqdb.org/). In general, character indexing websites work well since character arts are generally limited in terms of number compared to real-life photos.

<img alt="iqdb_status" src="screenshots/iqdb_status.png" width="600">

However, there are cases where character indexing websites will not work well, e.g.: the image is cropped or altered.

**Full Image** (Top: Saucenao, Bottom: MoeFlow)

<img alt="saucenao_full_image" src="screenshots/saucenao_from_full_image_2_characters.png" width="600">

<img alt="moeflow_full_image" src="screenshots/full_image_2_characters.png" width="600">

**Altered Image**

<img alt="saucenao_full_image" src="screenshots/saucenao_from_altered_2_characters.png" width="600">

<img alt="moeflow_full_image" src="screenshots/altered_2_characters.png" width="600">

Or, there are cases where you want to recognize a character from a photo.

(Top: Saucenao, Middle: iqdb, Bottom: MoeFlow)

<img alt="saucenao_photo" src="screenshots/saucenao_from_photo.png" width="600">

<img alt="iqdb_photo" src="screenshots/iqdb_from_photo.png" width="600">

<img alt="moeflow_photo" src="screenshots/from_photo.png" width="600">

### Transfer Learning

This project only uses [~~30~~* 60 images per character](100_class_traning_note.md) for learning, which are very low in number for image recognition learning. However, this number is chosen since the majority of characters has a limited number of arts.

In [yande.re](https://yande.re/tag?name=&order=count&type=4), there are around 35000 registered character tags. However, top 1000 characters only have 70+ images while top 2000 characters only have 40+ images.

(*) The number of dataset is increased from ~30 to ~60 and the overall accuracy is increased by 5% to 10% (from 60% - 65% to 70%).

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

After that, you need to download MoeFlow model via `models/download_model.sh` (~ 100 MB).

## How to run

After running steps above, you can simply run it by:

```
$ export MOEFLOW_MODEL_PATH='/path/to/MoeFlow/models'
$ pip install -e .
$ app
```

If your application is configured to run in a relative path, e.g.: [https://freedomofkeima.com/moeflow/](https://freedomofkeima.com/moeflow/), then you can set static URL path via `export MOEFLOW_RELATIVE_URL_PATH='/moeflow/'`.

## License

This project itself is licensed under MIT License. 

Face recognition feature is developed by [nagadomi](https://github.com/nagadomi).

All images are owned by their respective creators.
