THE GMB dataset
===============

The GMB dataset can be downloaded from:

http://gmb.let.rug.nl/data.php

Specifically:

http://gmb.let.rug.nl/releases/gmb-1.0.0.zip

Changes
-------

Be aware of the following modifications:

1. There was only one instance of label "ART", in:
   "The Who is currently touring in support of [Endless Wire]_ART, its
   first album since 1982."

   This label was removed [located in p01/d0488]

2. To Split data into the sub-domains CIA, VOA and MASC,
   use the following:

    grep -lrnw . -e "Voice of America" | cut -d'/' -f-3 | cut -c 3- | xargs -I '{}' mkdir -p VOA/'{}'; mv ./'{}' VOA/'{}'

    grep -lrnw . -e "Voice of America" | cut -d'/' -f-3 | cut -c 3- | xargs -I '{}' mv ./'{}' VOA/'{}'

3. There are only five instances of "TTL", so these were removed. They were in:
   - IDB [President] Luis Alberto Moreno -> changed TTL to PER [p16/d0527]
   - [President] Bush signed a new anti-genetic [p73/d0102/] -> TTL to PER
   - [Professor] Comerio talks about the scope [p75/d0108/] -> TTL to PER
   - Mounting calls for [Senator] Hillary Clinton [p60/d0292] -> TTL to PER
   - [Rep.] Tony Hall, D-Ohio, urges the United (MASC) [p03/d0686] -> TTL to PER

   Note - all except for p03/d0686 were in VOA.

