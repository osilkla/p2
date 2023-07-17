# P2-Scraping

This repository allow to scrap books data from book.toscrap.com with Python and BeautifulSoup.
- It will produce a CSV file for each books categories containing book's information.
- A folder with book's cover will also be generated, group by category. 

# Prerequisites 

- **Clone** the project with
```
git clone git@github.com:osilkla/p2.git
```
- (optional) create a v-env 
 ```
pip install virtualenv
python -m venv env
``` 
`source env/bin/activate` (macOS and Linux) or `env\Scripts\activate` (Windows)

- Then you have to install dependancies from  **requirement.txt**.

```
pip install -r requirements.txt
```

## How to use it

The script will allow you to scrap:

- All books
- All books of a chosen **category**
- All books **from** a chosen category (this option can be useful if the first option crashed for example)

To start :

```
python3 app/index.py
```
You should see the following :
<img width="643" alt="Screenshot 2023-07-17 at 17 00 17" src="https://github.com/osilkla/p2/assets/43600487/4ac0cc41-d94b-4c31-9438-7442ab2245b7">

Then if you choose "Category" or "From" option you should see a menu, to select a "category" (use arrow key to navigate and enter to validate choice)

<img width="495" alt="Screenshot 2023-07-17 at 17 01 03" src="https://github.com/osilkla/p2/assets/43600487/a239cd7e-1603-4546-b220-4ab3b21dc21b">

otherwise, if you choose "All", the script start  scraping books on the entire website.


