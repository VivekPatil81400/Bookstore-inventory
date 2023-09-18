# Bookstore-inventory

This project's task is to implement utilities that are going to be part of a bookshop’s inventory system. As these
utilities will be integrated into a larger system.

Each item in the bookshop’s catalogue can be identified by its unique Catalogue Identification Number
(CIN). A CIN is a sequence of 14 digits that follows a fixed structure: The first two digits identify the type
of publication (e.g., “17” for book or “42” for a magazine), the next 10 digits form an article number, and
the last 2 digits form a checksum that can be used to validate the CIN. Leading zeros are included as
part of the CIN.

The checksum is computed by taking the first 12 digits of CIN, multiplying each individual digit by its
position (note: the position number starts at one), calculating the sum of all those multiplications, and,
finally, by computing the modulo 97 of that sum. For instance, for the CIN 1700 03 72214424, you can
validate its checksum, 24, as follows:
(1*1 + 2*7 + 3*0 + 4*0 + 5*0 + 6*3 + 7*7 + 8*2 + 9*2 + 10*1 + 11*4 + 12*4) % 97 = 24

**Clone the repository:** git clone https://github.com/VivekPatil81400/Django-CRM.git

**Install dependencies:** pip install -r requirements.txt
