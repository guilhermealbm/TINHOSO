# GuimaraesRosaAPI

Standalone script (or Flask REST API that consumes this script) and returns one of many devil names used by Brazilian author Guimarães Rosa on his Magnum opus Grande Sertão: Veredas

Sabe quando você está escrevendo um texto e precisa de um sinônimo? Imagine, agora, que queira um sinônimo para o demônio; em especial, deseja um dos vários sinônimos utilizados por Guimarães Rosa no maravilhoso Grande Sertão: Veredas. É pra isso que esse código foi escrito!
Como script isolado ou integrado numa API REST escrita em Flask, GuimaraesRosaAPI conta com 94 sinônimos prontos para seu próximo pacto fáustico!

## Instalation

### Standalone script
1. Make sure you've python installed
2. Clone this repo

    `git clone https://github.com/guilhermealbm/GuimaraesRosaAPI`
3. Change into the directory of the project:

    `cd GuimaraesRosaAPI`
4. Run!

    `python devil_names.py`

### Flask REST API
1. Make sure you've python and Flask installed (Flask can be downloaded with pip)
2. Clone this repo

    `git clone https://github.com/guilhermealbm/GuimaraesRosaAPI`
3. Change into the directory of the project:

    `cd GuimaraesRosaAPI`
4. Run!

    `python start_api.py`
5. You can use the following routes:

    `/` - returns a random devil_name (GET)

    `/devil/<index>`- returns devil name by index (GET)

    `/all`- returns all devil names (GET)
    
    `/new` - add a new devil name (POST)

### Thanks
My special thanks to Wallyson Rodrigues De Souza work [Veredas-mortas: Um Fausto No Sertão Mineiro](https://repositorio.ufrn.br/jspui/bitstream/123456789/25767/1/VeredasmortasFausto_Souza_2018.pdf), which I got all the names used in the python script

> "Viver é um negócio muito perigoso"
> — Guimarães Rosa