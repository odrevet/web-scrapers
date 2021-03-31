# axecop-downloader

```
Download episodes of axecop

usage: axecop.py [-h] --episode EPISODE

AxeCop Downloader.

optional arguments:
  -h, --help            show this help message and exit
  --episode EPISODE, -e EPISODE
                        Episode to download
```

# example

Download episode from 0 to 5
```sh
for episode in {0..5}; do python axecop.py -e $episode; done
```
