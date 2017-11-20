## List of characters

Currently, 100 characters are picked from 25 animation series.

1. Angel Beats!: Tachibana Kanade
2. Charlotte: Tomori Nao
3. Chuunibyou demo Koi ga Shitai!: Dekomori Sanae, Nibutani Shinka, Takanashi Rikka
4. Date A Live: Itsuka Kotori, Tobiichi Origami, Tokisaki Kurumi, Yatogami Tohka, Yoshino
5. Eromanga-sensei: Izumi Sagiri, Yamada Elf
6. Evangelion: Ayanami Rei, Souryuu Asuka Langley
7. Fate Series: Illyasviel von Einzbern, Matou Sakura, Miyu Edelfelt, Saber, Tohsaka Rin
8. Gochuumon wa Usagi desu ka?: Hoto Cocoa, Jouga Maya, Kafuu Chino, Kirima Sharo, Natsu Megumi, Tedeza Rize, Ujimatsu Chiya
9. K-On!: Akiyama Mio, Asahina Mikuru, Hirasawa Yui, Kotobuki Tsumugi, Nakano Azusa, Tainaka Ritsu
10. Kancolle: Hibiki, Kashima, Kongou, Shigure
11. Kiniro Mosaic: Alice Cartelet, Inokuma Youko, Komichi Aya, Kujou Karen, Oomiya Shinobu
12. Kono Subarashii Sekai ni Shukufuku wo!: Aqua, Dustiness Ford Lalatina, Megumin
13. Love Live!: Ayase Eli, Hoshizora Rin, Koizumi Hanayo, Kousaka Honoka, Minami Kotori, Nishikino Maki, Sonoda Umi, Toujou Nozomi, Yazawa Nico
14. Love Live! Sunshine!!: Kunikida Hanamaru, Kurosawa Dia, Kurosawa Ruby, Matsuura Kanan, Ohara Mari, Sakurauchi Riko, Takami Chika, Tsushima Yoshiko, Watanabe You
15. Madoka Magica: Akemi Homura, Kaname Madoka, Miki Sayaka, Sakura Kyouko, Tomoe Mami
16. New Game!: Sakura Nene, Suzukaze Aoba, Takimoto Hifumi, Yagami Kou
17. Nisekoi: Kirisaki Chitoge, Onodera Kosaki
18. Ore no Imouto ga Konnani Kawaii Wake ga Nai: Aragaki Ayase, Gokou Ruri, Kousaka Kirino
19. Re:Zero kara Hajimeru Isekai Seikatsu: Emilia, Ram, Rem
20. Saenai Heroine no Sodatekata: Hyoudou Michiru, Kasumigaoka Utaha, Katou Megumi, Sawamura Spencer Eriri
21. Steins;Gate: Makise Kurisu, Shiina Mayuri
22. Suzumiya Haruhi no Yuuutsu: Nagato Yuki, Suzumiya Haruhi
23. Sword Art Online: Asuna, Kirigaya Suguha, Leafa, Lisbeth, Silica, Sinon, Yui
24. Toaru Kagaku no Railgun: Misaka Mikoto, Saten Ruiko, Shirai Kuroko, Uiharu Kazari
25. Yahari Ore no Seishun Love Comedy wa Machigatteiru: Yuigahama Yui, Yukinoshita Yukino

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

- learning rate = 0.02 training steps = 4000 random factor (crop, brightness) = 10% (very slow!)
INFO:tensorflow:2017-11-19 16:51:37.128322: Step 3999: Train accuracy = 94.0%
INFO:tensorflow:2017-11-19 16:51:37.128522: Step 3999: Cross entropy = 0.745446
INFO:tensorflow:2017-11-19 16:51:37.200592: Step 3999: Validation accuracy = 54.0% (N=100)
INFO:tensorflow:Final test accuracy = 59.7% (N=385)

### Results (Additional)

In this experimentation, the number of images is not fixed to 30. Each category has around 30 to 45 images.

- learning rate = 0.02, training steps = 8000
```
INFO:tensorflow:2017-11-19 13:37:58.752268: Step 7999: Train accuracy = 99.0%
INFO:tensorflow:2017-11-19 13:37:58.752560: Step 7999: Cross entropy = 0.369550
INFO:tensorflow:2017-11-19 13:37:58.866312: Step 7999: Validation accuracy = 62.0% (N=100)
INFO:tensorflow:Final test accuracy = 64.0% (N=511)
```

- learning rate = 0.02, training steps = 40000
```
INFO:tensorflow:2017-11-20 03:10:50.680439: Step 39999: Train accuracy = 100.0%
INFO:tensorflow:2017-11-20 03:10:50.680629: Step 39999: Cross entropy = 0.071079
INFO:tensorflow:2017-11-20 03:10:50.752890: Step 39999: Validation accuracy = 64.0% (N=100)
INFO:tensorflow:Final test accuracy = 65.0% (N=511)
```

- learning rate = 0.03, training steps = 40000
```
INFO:tensorflow:2017-11-20 03:12:27.098684: Step 39999: Train accuracy = 100.0%
INFO:tensorflow:2017-11-20 03:12:27.098889: Step 39999: Cross entropy = 0.042718
INFO:tensorflow:2017-11-20 03:12:27.170470: Step 39999: Validation accuracy = 59.0% (N=100)
INFO:tensorflow:Final test accuracy = 64.8% (N=511)
```
