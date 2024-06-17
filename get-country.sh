#!/bin/bash

DOMAIN_LIST="
baidu.com
amazon.com
amazon.co.jp
amazon.in
imdb.com
amazonaws.com
amazon.de
amazon.co.uk
hao123.com
onlinesbi.com
iqoption.com
zhihu.com
avito.ru
craigslist.org
aliyun.com
scol.com.cn
momoshop.com.tw
amazon.it
uniqlo.tmall.com
amazon.ca
subject.tmall.com
amazon.es
sahibinden.com
amazon.fr
ups.com
hurriyet.com.tr
goodreads.com
amazon.cn
n11.com
spao.tmall.com
gap.tmall.com
crabsecret.tmall.com
lee.tmall.com
banvenez.com
gosuslugi.ru
citi.com
popads.net
aimer.tmall.com
tonlion.tmall.com
ivi.ru
news18.com
milliyet.com.tr
ria.ru
langsha.tmall.com
earthmusic.tmall.com
nike.tmall.com
yna.co.kr
scofield.tmall.com
amazon.com.br
usps.com
basichouse.tmall.com
ameritrade.com
qiannaimei.tmall.com
gmarket.co.kr
etrade.com
threegun.tmall.com
bershka.tmall.com
sputniknews.com
hollisterco.tmall.com
lachapelle.tmall.com
zhaopin.com
runoob.com
corriere.it
gucn.tmall.com
maniform.tmall.com
newbalance.tmall.com
anta.tmall.com
lining.tmall.com
calvinklein.tmall.com
gainreel.tmall.com
fairwhale.tmall.com
mynet.com
cisco.com
honeys.tmall.com
discoveryexpedition.tmall.com
verizonwireless.com
52pojie.cn
peacebird.tmall.com
semir.tmall.com
eland.tmall.com
it.tmall.com
septwolves.tmall.com
kolonsport.tmall.com
forever21.tmall.com
amazon.com.au
dickies.tmall.com
marksandspencer.tmall.com
haberturk.com
esprit.tmall.com
urfs.tmall.com
bild.de
imis.tmall.com
jackjones.tmall.com
triumph.tmall.com
sabah.com.tr
zol.com.cn
jeanswest.tmall.com
newegg.com
rbc.ru
topshop.tmall.com
audible.com
sci-hub.tw
"

for domain in $DOMAIN_LIST
do
  echo -e "\n$domain:"
  whois $domain | grep 'Country'
done