# lame-riscv
Algoritmo LAME (Lame Ain't an MP3 Encoder) para ser compilador para RISC-V. O algoritmo converte arquivos wmv para mp3.
OBS: o algoritmo em si não foi escrito por mim, ele foi retirado da página do [MiBench](https://vhosts.eecs.umich.edu/mibench/source.html) no arquivo `consumer.tar.gz`.

# Baixar arquivos
Para baixar os arquivos do repositório basta executar o comando:

    $ git clone https://github.com/mymatsubara/lame-riscv.git

# Compilação
Para compilação é necessário instalar um compilador riscv. Você pode fazer executando o seguinte comando:

    $ sudo apt-get install gcc-riscv64-linux-gnu

Em seguida basta mudar entrar na pasta `lame3.70` e executar o comando:

    $ make

Agora você tem disponível o binário `lame3.70\lame` compilado para RISC-V

# Execução
Talvez você precise de um emulador de RISC-V para executar o binário. Um possível emulador é o qemu que pode ser instalado executando o seguinte comando:

    $ sudo apt-get install qemu-user

Assim que o emulador estiver instalado, você pode executar o seguinte comando para converter o arquivo `small.wav` para `output_small.mp3`:

    $ qemu-riscv64 lame3.70/lame small.wav output_small.mp3


