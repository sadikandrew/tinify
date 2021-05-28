# tinify

#### Automatically shrink JPEGs and PwwwNGs using https://tinypng.com/ APIs

- Run `pip install --upgrade tinify` to install the tinify package to utilize the tinyPNG APIs

- Use [TinyPNG – Developer API](https://tinypng.com/developers) to obtain an API key

- Edit tinify.py - replace the `XXX... `  with your obtained API key on the following line

- ```python
  tinify.key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #insert API KEY HERE 
  ```

- Run tinify.py once to initalize your folder structure

- Paste your images in the unoptimized folder

- Run tinify.py once again to automatically optimize your images' size
