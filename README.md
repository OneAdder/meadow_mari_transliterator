# Meadow Mari Transliterator

This script reads plain text file `text` (**not** `text.txt`) with Meadow Mari text in latin transcription and
transliterates it into the standard Meadow Mari cyrillic graphics.

The script is not packaged so, to install it just download the `meadow_mari_transliterator.py` into your
working directory and use it.

Usage example (Unix):
```
./meadow_mari_transliterator.py > result
```

Windows:
```
python3 meadow_mari_transliterator.py
```

This will create file `result` with transliteration of the file `text`.

You may also use it as library:
```python
>>> from meadow_mari_transliterator import latin_to_cyrillic
>>> text = \
... '''
... peš vet interesno: rvezevlak kö škenəštəm kuč'en šogalənət,
... kö üdramašvlakən joləštəm kuč'en šogalənət, kö eše iktažmom.
... '''
>>> latin_to_cyrillic(text)
'Пеш вет интересно: рвезе-влак кӧ шкеныштым кучен шогалыныт, кӧ ӱдрамашвлакын йолыштым кучен шогалыныт, кӧ еше иктажмом.'
```
