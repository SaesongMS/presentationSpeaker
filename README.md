# tts-laby

## Instalacja

Do dzialania potrzebujecie pyTorcha, ja postawilem sobie wirtualne srodowisko w projekcie i tam zainstalowalem pytorcha. Do dzialanie pyTorcha potrzebujecie tez CUDA(ewentualnie mozna zainstalowac wersje CPU, ale to bedzie dzialac wolniej).
- https://developer.nvidia.com/cuda-gpus - sprawdzcie czy wasza karta obsluguje CUDA
- https://developer.nvidia.com/cuda-downloads - CUDA
- https://code.visualstudio.com/docs/python/python-tutorial - jak zainstalowac wirtualne srodowisko w VS Code
- https://pytorch.org/get-started/locally/ - dokladna moja wersja(pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121)

Plik test.py jest do sprawdzenia czy wszystko dziala, przykladowy wynik:
```
True
1
0
<torch.cuda.device object at 0x000001CCE8A34290>
NVIDIA GeForce RTX 3060 Ti
```
