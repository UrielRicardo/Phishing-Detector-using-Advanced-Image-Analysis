#!/bin/bash
array=(
http://vinicblog.blogspot.com.br/2010/01/o-que-significa-o-logotipo-do-bradesco.html
https://qi.edu.br/
https://www.brandsoftheworld.com/logo/bradesco-4

)

for i in "${array[@]}"; do
    python /root/facul/imageExtractor.py "$i"
done

