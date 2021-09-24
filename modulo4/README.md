# Passo a Passo

## Geração do objdump
A primeira coisa feita foi gerar o dump do binário `lame.370/lame` apenas com as instruções. O processo pode ser realizado executando a seguinte linha de comando:

    $ riscv64-unknown-linux-gnu-objdump -d --no-show-raw-insn ../lame3.70/lame > dump.txt

## Transformação do dump para um arquivo de trace do amnesia
Para a realização deste processo, foi escrito o script `dump_to_trace.py` que converte o dump para um trace utilizável no amnesia. Para executar o script basta executar o seguinte comando:

    $ python dump_to_trace.py dump.txt trace.txt