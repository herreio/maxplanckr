# Prepare Raw Data

Set Up:

```sh
virtualenv -p python3 --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
```

Additional Requirements:

- [Firefox](https://www.mozilla.org/en-US/firefox/), [Gecko Driver](https://github.com/mozilla/geckodriver/releases/) and [Selenium](https://pypi.org/project/selenium/)
    - make sure you have [Gecko Driver](https://github.com/mozilla/geckodriver/releases/) available on your `PATH`


## Retrieve Publication Data

The following scripts are used to retrieve informations about entities from [MPG.PuRe](https://pure.mpg.de) and its named entity service [CoNE](https://pure.mpg.de/cone/) and finally to query the records.

- [`retrieve/cone_jour.py`](./retrieve/cone_jour.py)

```
100%|████████████████████████████████████████████| 7679/7679 [24:13<00:00,  5.40it/s]
```

- [`retrieve/cone_lang.py`](./retrieve/cone_lang.py)

```
100%|████████████████████████████████████████████| 8590/8590 [24:02<00:00,  5.74it/s]
```

- [`retrieve/cone_pers.py`](./retrieve/cone_pers.py)

```
100%|████████████████████████████████████████████| 60007/60007 [3:15:34<00:00,  5.36it/s]
```

- [`retrieve/pure_ctx.py`](./retrieve/pure_ctx.py)
- [`retrieve/pure_ous.py`](./retrieve/pure_ous.py)
- [`retrieve/pure_pub.py`](./retrieve/pure_pub.py)

```
100%|████████████████████████████████████████████| 219/219 [20:42<00:00,  3.14s/it]
```


## Crawling the Institute’s Metadata

The following scripts are used to crawl informations about the current Max Planck Institutes (MPIs), their research domains (`category`) and research areas (`tag`) from the website of the Max Planck Society.

- [`crawl/mpis_eng.py`](./crawl/mpis_eng.py)
- [`crawl/mpis_deu.py`](./crawl/mpis_deu.py)

Use these scripts by running:

```sh
python -m crawl
```


#### Mapping of MPIs to MPG.PuRe Entities

The following scripts can be used to map the crawled MPIs to their corresponding identifiers in MPG.PuRe and to find the associated contexts as well as categories and thematic tags of the institutes. (--> Important that you have done the [retrieval](#retrieve-publication-data) before!)

- [`crawl/map_mpis_eng.py`](./crawl/map_mpis_eng.py)
- [`crawl/map_mpis_deu.py`](./crawl/map_mpis_deu.py)
- [`crawl/map_mpis.py`](./crawl/map_mpis.py)

Use these scripts by running:

```sh
python -m crawl.map_mpis_eng
python -m crawl.map_mpis_deu
python -m crawl.map_mpis
```

This will create a mapping (`mpi_ous.json`) from institutes to identifiers at path `../extdata/retrieve/mpis/map/`. The mapping should be refined manually! Check if institutes not found have in fact corresponding identifiers in MPG.PuRe. After having done this you can run the post-mapping procedure:


```sh
python -m crawl.map_post
```

## Extract Count Data, Network Graph, Data Tables and Title Documents

```sh
python -m extract.graph
python -m extract.items
python -m extract.stats
python -m extract.titles
```
