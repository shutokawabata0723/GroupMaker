# make_group
create team members just input number that you want to split.

## How to use

add member to `members.txt`

```txt:members.txt
Kira
Asuran
Shin
Runamaria
Meirin
Kagari
Haine
Rakusu
Amuro
Rei
Izahku
Dhiakka
Nikoru
...
[add name]
```


Run `python3 make_g.py`

you will be asked `how many groups you want?: `

Then please input number of group that you want.

each group members are shown like below.

```console:
how many groups you want?: 2
 1  ['Amuro', 'Kira', 'Haine', 'Rakusu', 'Shin', 'Asuran', 'Kagari']
 2  ['Nikoru', 'Izahku', 'Rei', 'Dhiakka', 'Meirin', 'Runamaria']
 ```

 ```console:
how many groups you want?: 6
 1  ['Rakusu', 'Runamaria', 'Haine']
 2  ['Rei', 'Meirin']
 3  ['Izahku', 'Dhiakka']
 4  ['Amuro', 'Nikoru']
 5  ['Asuran', 'Kagari']
 6  ['Shin', 'Kira']
 ```

 When other characters are detected, you need to input number again.

 ```console:
how many groups you want?: shuto
the input contains characters not only number. try again...
how many groups you want?: 3
 1  ['Asuran', 'Shin', 'Amuro', 'Rakusu', 'Kira']
 2  ['Rei', 'Dhiakka', 'Nikoru', 'Kagari']
 3  ['Haine', 'Runamaria', 'Meirin', 'Izahku']
```
