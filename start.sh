#!/bin/bash
array=(
https://www.universidadedobitcoin.com.br/
https://app.foxbit.com.br/
)

for i in "${array[@]}"; do
    python /aplicacoes/imageExtractor.py "$i"
done
