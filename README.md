# Docker harjoitus 1

## Projektin kuvaus

Molemmat asiakas ja palvelin ovat toteutettu uv python projekteina. palvelin luo 1kb satunnaista tekstiä ja talletaan tämän tiedostoon. Asiakas pyytää tiedoston, josta palvelin antaa headereissa checksumin, jonka asiakas voi tarkistaa. Palvelin konttiin voidaan määrittää portti --port atribuutilla. Asiakkaaseen voidaan määrittää palvelimen osoite antamalla sen imagen jälkeen. Konteille määritetään verkko, jonka avulla ne voivat kommunikoida keskenään. Konteille määritetään voluumit mihin ne tallentavat tietojaan.

## Palvelin kontin muodostus

Suorita projektin juuresta

```bash
bash server.sh
```

## Asiakas kontin muodostus

Suorita projektin juuresta

```bash
bash client.sh
```

## Tiedostojen tarkastus

### server

```bash
sudo cat /var/lib/docker/volumes/servervol/_data/randomletters.txt 
```

### client

```bash
sudo cat /var/lib/docker/volumes/clientvol/_data/received.txt
```
