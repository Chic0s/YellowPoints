<h2>Les points Jaunes et les imprimantes ?</h2>

<p> 
Il existe des "points de repérage" permettant aux autorités de retrouver qui a utiliser l'imprimante. 

En effet, ces imprimantes impriment secrètement un motif de points jaunes. 

Invisible à l'oeil nu mais lorsqu'ils sont mis sous une lumière bleue, ils apparaitront. 

Nous allons voir comment faire apparaitre ces points avec Python ! 
</p>

```python
from PIL import Image

blue = Image.open("nomdufichier.png").split() [2]
blue.point(lambda x: (256-x)**2).show()
```

<p>
Ce petit script va utiliser la librairie PIL pour modifier le code couleur de l'image. 

Il suffit de décoder les points jaunes à l'aide de cette image (Attention au bit de parité) : 
</p> 

![points-jaunes-eff](https://user-images.githubusercontent.com/96829109/188459034-8d4a162b-b35b-4453-8309-7b0cce9408fd.jpg)

<h3> Enjoy ! 
